# GitCommitHistoryToCSV

## Description
GitCommitHistoryToCSV is a Python script that automates the extraction of Git commit logs into a CSV file. It's designed to parse the commit history of a given Git repository and convert it into a well-structured CSV format, making it easier for analysis and reporting.

## Features
- Extracts commit logs from any Git repository.
- Filters commits by the current Git user's username.
- Generates a CSV file with detailed commit information.
- Works with repositories containing multiple branches.
- Automatically names files based on the repository name.

## Prerequisites
Before running this script, make sure you have Python installed on your system. This script is compatible with Python 3.

## Installation
1. Clone the repository: `git clone https://github.com/5a9awneh/GitCommitHistoryToCSV.git`
2. Navigate to the script directory: `cd GitCommitHistoryToCSV`

## Usage
1. Run the script: `python main.py`
2. When prompted, enter the full path to your Git repository.
3. The script will generate a CSV file in the script's directory, named `<repository_name>_commit_history.csv`.

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
This project is licensed under the [MIT License](LICENSE).
