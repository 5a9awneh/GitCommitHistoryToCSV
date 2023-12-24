import subprocess
import pandas as pd
import re
import csv
from datetime import datetime
from os.path import basename, isdir
import os
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),  # Save logs to a file
        logging.StreamHandler(),  # Print logs to the console
    ],
)


def get_repo_name(repo_dir):
    repo_name = basename(repo_dir)
    return repo_name


def generate_commit_log(repo_dir, author, output_file_name):
    git_command = [
        "git",
        "-C",
        repo_dir,
        "log",
        "--all",
        "--no-merges",
        "--reverse",
        "--shortstat",
    ]
    if author:
        git_command.append(f"--author={author}")
    result = subprocess.run(git_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running Git command:", result.stderr)
        return None

    with open(output_file_name, "w") as file:
        file.write(result.stdout)
    return output_file_name


def get_repo_details(repo_dir):
    command_get_url = ["git", "-C", repo_dir, "config", "--get", "remote.origin.url"]
    command_get_branch = ["git", "-C", repo_dir, "branch", "--show-current"]
    repo_url = subprocess.run(
        command_get_url, capture_output=True, text=True
    ).stdout.strip()
    repo_branch = subprocess.run(
        command_get_branch, capture_output=True, text=True
    ).stdout.strip()
    return repo_url, repo_branch


def parse_commit_log(file_path, repo_url, repo_branch):
    with open(file_path, "r") as file:
        commit_text = file.read()

    commit_blocks = commit_text.split("commit ")[1:]
    parsed_commits = []

    for block in commit_blocks:
        parts = block.split("\n\n", 2)
        if len(parts) < 3:
            continue

        header, message, change_stats = parts
        match = re.match(
            r"^([\da-f]+)\nAuthor: (.+?) <(.+?)>\nDate: (.+?)$", header, re.DOTALL
        )
        if match:
            commit_id, author, author_email, date_time_str = match.groups()

        # Process change stats more flexibly
        files_changed = insertions = deletions = "0"
        stats_pattern = r"(\d+) files? changed"
        insertions_pattern = r"(\d+) insertions?\(\+\)"
        deletions_pattern = r"(\d+) deletions?\(-\)"

        stats_match = re.search(stats_pattern, change_stats)
        insertions_match = re.search(insertions_pattern, change_stats)
        deletions_match = re.search(deletions_pattern, change_stats)

        if stats_match:
            files_changed = stats_match.group(1)
        if insertions_match:
            insertions = insertions_match.group(1)
        if deletions_match:
            deletions = deletions_match.group(1)

        # Date and time parsing
        date_time_str = date_time_str.strip()
        try:
            date_time_obj = datetime.strptime(date_time_str, "%a %b %d %H:%M:%S %Y %z")
            date = date_time_obj.strftime("%d/%m/%Y")
            time = date_time_obj.strftime("%H:%M:%S %z")
        except ValueError as e:
            print(f"Error parsing date and time for commit {commit_id}: {e}")
            date = "Invalid Date"
            time = "Invalid Time"

        clean_message = message.strip()
        parsed_commits.append(
            {
                "Repository URL": repo_url,
                "Branch": repo_branch,
                "Commit ID": commit_id,
                "Author": author,
                "Date": date,
                "Time": time,
                "Message": clean_message,
                "Files Changed": files_changed,
                "Insertions (+)": insertions,
                "Deletions (-)": deletions,
            }
        )

    return pd.DataFrame(parsed_commits)


def main():
    repo_dir = input("Enter the path to your local Git repository: ").strip()
    if not isdir(repo_dir):
        logging.error(
            "Invalid directory. Please enter a valid Git repository directory."
        )
        return

    try:
        repo_name = get_repo_name(repo_dir)
        repo_url, repo_branch = get_repo_details(repo_dir)
    except Exception as e:
        logging.error("Failed to obtain repository details: %s", str(e))
        return

    author_choice = input("Filter by specific author? (y/n): ").strip().lower()
    author_username = ""
    if author_choice == "y":
        author_username = input("Enter author's GitHub username: ").strip()

    try:
        git_output_file = f"{repo_name}_commit_history.txt"
        csv_output_file = f"{repo_name}_commit_history.csv"

        commit_log_file = generate_commit_log(
            repo_dir, author_username, git_output_file
        )
        if commit_log_file:
            df = parse_commit_log(commit_log_file, repo_url, repo_branch)
            df.to_csv(csv_output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
            logging.info(f"CSV file created: {csv_output_file}")

    except Exception as e:
        logging.error("An error occurred while generating the CSV file: %s", str(e))
    finally:
        if commit_log_file and os.path.exists(commit_log_file):
            os.remove(commit_log_file)
            logging.info(f"Deleted temporary file: {git_output_file}")


if __name__ == "__main__":
    main()
