# GitHub User Activity Tracker

A Python command-line tool that fetches and displays a GitHub user's recent public activity using the GitHub API.  
It presents the activity in a colorized table using [Rich](https://github.com/Textualize/rich).

---

## Features

- Fetches a GitHub user's latest public events.
- Displays:
  - **Event type** (e.g., PushEvent, WatchEvent)
  - **Repository name**
  - **Relative time** (e.g., "3 hours ago", "yesterday", "last week")
- Colorized terminal output for better readability.
- Graceful handling of API errors, timeouts, and invalid input.

---

## Requirements

- Python 3.7+
- [Rich](https://github.com/Textualize/rich) for beautiful console output.
- [Requests](https://requests.readthedocs.io/) for making API calls.

---

## Installation

1. Clone this repository or copy the script into a file (e.g., `github_activity.py`):

git clone https://github.com/your-username/github-activity-tracker.git
cd github-activity-tracker
Install the required dependencies:

pip install requests rich
Usage
Run the script:

python github_activity.py
When prompted, enter a valid GitHub username:

Enter Username : torvalds
Example output:

┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃   Event Type  ┃        Repository       ┃     Date     ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   PushEvent   │ octocat/Hello-World     │ 2 hours ago  │
│  WatchEvent   │ python/cpython          │ yesterday    │
│ CreateEvent   │ yourname/new-repo       │ last week    │
└───────────────┴─────────────────────────┴──────────────┘
Error Handling
The script handles:

Invalid usernames (prints the GitHub API error message)

Network issues

Timeouts

Invalid JSON responses

API Rate Limits
GitHub's API allows 60 unauthenticated requests per hour.
If you need more, create a personal access token and update the script to use authentication.

License
This project is licensed under the MIT License.

https://roadmap.sh/projects/github-user-activity
