# GitCommitHistoryToCSV

## Description
GitCommitHistoryToCSV is a Python script that automates the extraction of Git commit logs into a CSV file. It's designed to parse the commit history of a given Git repository, with an option to filter by a specific author, and convert it into a structured CSV format for analysis and reporting.

## Features
- Extracts commit logs from any Git repository.
- Option to filter commits by a specific author or include all authors.
- Excludes merge commits for clearer data analysis.
- Generates a CSV file with detailed commit information.
- Automatically names files based on the repository name.

## Prerequisites
- Python 3
- Pandas library

## Installation
1. Clone the repository: `git clone https://github.com/5a9awneh/GitCommitHistoryToCSV.git`
2. Navigate to the script directory: `cd GitCommitHistoryToCSV`
3. Install required packages: `pip install -r requirements.txt`

## Usage
1. Run the script: `python main.py`
2. Enter the full path to your Git repository.
3. Optionally, specify an author's GitHub username to filter commits.
4. The script will generate a CSV file in the script's directory, named `<repository_name>_commit_history.csv`.

## Output Format
The generated CSV file contains the following columns:
- Commit ID
- Author
- Date
- Time
- Message
- Files Changed
- Insertions (+)
- Deletions (-)

## Contributing
Contributions to this project are welcome. Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
