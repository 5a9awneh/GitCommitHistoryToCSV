# GitCommitHistoryToCSV

<!-- BADGES:START -->
[![License](https://img.shields.io/github/license/5a9awneh/GitCommitHistoryToCSV)](LICENSE) [![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)](https://www.python.org/) [![Last Commit](https://img.shields.io/github/last-commit/5a9awneh/GitCommitHistoryToCSV)](https://github.com/5a9awneh/GitCommitHistoryToCSV/commits/main) [![Output](https://img.shields.io/badge/output-CSV-blue?style=flat)](https://github.com/5a9awneh/GitCommitHistoryToCSV) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat)](http://makeapullrequest.com) [![Runs Locally](https://img.shields.io/badge/runs_locally-privacy--first-green?style=flat)](https://github.com/5a9awneh/GitCommitHistoryToCSV) [![Human in the Loop](https://img.shields.io/badge/human--in--the--loop-%E2%9C%93-brightgreen?style=flat)](https://github.com/5a9awneh/GitCommitHistoryToCSV)
<!-- BADGES:END -->

## 📄 Description

```mermaid
flowchart TD
    Start([python main.py]) --> Args[Parse arguments\nrepo path + optional --author]
    Args --> Val{Valid Git\nrepository?}
    Val -->|❌ Not a repo| Err([Exit with error])
    Val -->|✅ Valid| Log[Run git log\n--no-merges --stat]
    Log --> Parse[Parse commit fields\nHash, Author, Date, Message]
    Parse --> Filter{--author\nflag set?}
    Filter -->|Yes| FA[Filter commits\nby author name]
    Filter -->|No| All[Include all authors]
    FA --> Write[Write CSV\nrepo_commit_history.csv]
    All --> Write
    Write --> Debug[Log to debug.log]
    Debug --> Done([✅ CSV ready])

    style Val fill:#7a5500,color:#fff
    style Filter fill:#7a5500,color:#fff
    style Err fill:#8b1a1a,color:#fff
    style Done fill:#2d6a2d,color:#fff
```

GitCommitHistoryToCSV is a Python script that automates the extraction of Git commit logs into a CSV file. It's designed to parse the commit history of a given Git repository, with an option to filter by a specific author, and convert it into a structured CSV format for analysis and reporting.

## ✨ Features
- Extracts commit logs from any Git repository.
- Option to filter commits by a specific author or include all authors.
- Excludes merge commits for clearer data analysis.
- Generates a CSV file with detailed commit information.
- Automatically names files based on the repository name.
- Comprehensive logging of operations and errors for troubleshooting - see `debug.log` for detailed information.
- Command-line interface for easy script execution and automation.

## 📋 Prerequisites
- Python 3
- Pandas library

## 📥 Installation
1. Clone the repository: `git clone https://github.com/5a9awneh/GitCommitHistoryToCSV.git`
2. Navigate to the script directory: `cd GitCommitHistoryToCSV`
3. Install required packages: `pip install -r requirements.txt`

## 🚀 Usage
Run the script from the command line by providing the path to the Git repository:

`python main.py "/path/to/your Git repository" --author "author's GitHub username"`

Replace `"/path/to/your Git repository"` with the full path to your Git repository. If your path includes spaces, ensure it is enclosed in quotes.

The `--author` flag is optional and allows you to filter commits by a specific author. If omitted, commits from all authors will be included.

The script will generate a CSV file in the script's directory, named `<repository_name>_commit_history.csv`.

## 📊 Output Format
The generated CSV file contains the following columns:
- Repository URL
- Branch
- Commit ID
- Author
- Date
- Time
- Message
- Files Changed
- Insertions (+)
- Deletions (-)

## 🤝 Contributing
Contributions to this project are welcome. Feel free to fork the repository and submit pull requests.

## 📄 License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
