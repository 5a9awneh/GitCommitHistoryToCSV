import subprocess
import pandas as pd
import re
import csv
from datetime import datetime
from os.path import basename, isdir
import os


def get_repo_name(repo_dir):
    repo_name = basename(repo_dir)
    return repo_name


def get_current_git_username(repo_dir):
    result = subprocess.run(
        ["git", "-C", repo_dir, "config", "user.name"], capture_output=True, text=True
    )
    if result.returncode != 0:
        print("Error fetching current Git username:", result.stderr)
        return None

    return result.stdout.strip()


def generate_commit_log(repo_dir, author, output_file_name):
    git_command = [
        "git",
        "-C",
        repo_dir,
        "log",
        "--all",
        f"--author={author}",
        "--reverse",
        "--shortstat",
    ]
    result = subprocess.run(git_command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running Git command:", result.stderr)
        return None

    with open(output_file_name, "w") as file:
        file.write(result.stdout)
    return output_file_name


def parse_commit_log(file_path):
    with open(file_path, "r") as file:
        commit_text = file.read()

    commit_blocks = commit_text.split("commit ")[1:]
    parsed_commits = []

    for block in commit_blocks:
        pattern = r"^([\da-f]+)\nAuthor: (.+?) <.+?>\nDate: (.+?)\n\n(.+?)\n\n (\d+) files? changed, (\d+) insertions?\(\+\), (\d+) deletions?\(-\)"
        match = re.search(pattern, block, re.DOTALL)

        if match:
            (
                commit_id,
                author,
                date_time_str,
                message,
                files_changed,
                insertions,
                deletions,
            ) = match.groups()
            date_time_str = date_time_str.strip()

            try:
                date_time_obj = datetime.strptime(
                    date_time_str, "%a %b %d %H:%M:%S %Y %z"
                )
                date = date_time_obj.strftime("%d/%m/%Y")
                time = date_time_obj.strftime("%H:%M:%S %z")
            except ValueError as e:
                print(f"Error parsing date and time: {e}")
                date = "Invalid Date"
                time = "Invalid Time"

            clean_message = message.strip()
            parsed_commits.append(
                {
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
    repo_dir = input("Enter the path to your Git repository: ").strip()
    if not isdir(repo_dir):
        print("Invalid directory. Please enter a valid Git repository directory.")
        return

    repo_name = get_repo_name(repo_dir)
    author_username = get_current_git_username(repo_dir)
    if author_username:
        git_output_file = f"{repo_name}_commit_history.txt"
        csv_output_file = f"{repo_name}_commit_history.csv"

        commit_log_file = generate_commit_log(
            repo_dir, author_username, git_output_file
        )
        if commit_log_file:
            df = parse_commit_log(commit_log_file)
            df.to_csv(csv_output_file, index=False, quoting=csv.QUOTE_NONNUMERIC)
            print(f"CSV file created: {csv_output_file}")

            # Delete the txt file after successful CSV generation
            os.remove(commit_log_file)
            print(f"Deleted temporary file: {git_output_file}")
    else:
        print(
            "Failed to identify the current Git user. Ensure you are in a Git repository directory."
        )


if __name__ == "__main__":
    main()
