# GitCommitHistoryToCSV

## Description
GitCommitHistoryToCSV is a Python script for extracting Git commit logs into a CSV format. It parses commit history from a Git repository, excluding merge commits, and provides a structured CSV output.

## Features
- Excludes merge commits for more relevant data.
- Parses commits by the specified Git user's username.
- Generates a CSV file with detailed commit information, including files changed, insertions, and deletions.
- Automatically names output files based on the repository name.

## Prerequisites
- Python 3
- Pandas library

## Installation
1. Clone the repository: `git clone https://github.com/5a9awneh/GitCommitHistoryToCSV.git`
2. Navigate to the script directory: `cd GitCommitHistoryToCSV`
3. Install required packages: `pip install -r requirements.txt`

## Configuration
Before running the script, ensure to set the `author_username` variable in `main.py` to your GitHub username. This username is used to filter commits by the author.

## Usage
1. Run the script: `python main.py`
2. Enter the full path to your Git repository when prompted.
3. A CSV file named `<repository_name>_commit_history.csv` will be generated in the script's directory.

## Output Format
The CSV file includes:
- Commit ID
- Author
- Date
- Time
- Message
- Files Changed
- Insertions (+)
- Deletions (-)

## Contributing
Contributions are welcome. Please fork the repository and submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
