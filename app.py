import os
import random
import subprocess
import datetime
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from .env
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO = os.getenv("GITHUB_REPO")
GITHUB_PAT = os.getenv("GITHUB_PAT")  # Leave empty if using SSH
REPO_PATH = os.getenv("REPO_PATH")
BRANCH = os.getenv("BRANCH", "main")  # Default to 'main' branch

# Commit settings
MIN_COMMITS = int(os.getenv("MIN_COMMITS", 1))  # Default: 1 commit
MAX_COMMITS = int(os.getenv("MAX_COMMITS", 7))  # Default: 7 commits

# Time range for commit
START_HOUR = int(os.getenv("START_HOUR", 0))   # Default: 12 AM
END_HOUR = int(os.getenv("END_HOUR", 23))      # Default: 11 PM

# Validate required environment variables
if not all([GITHUB_USERNAME, GITHUB_REPO, REPO_PATH]):
    print("Error: Missing required environment variables in .env file.")
    exit(1)

# Change directory to the repository
os.chdir(REPO_PATH)

# Generate random number of commits
num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)

for _ in range(num_commits):
    # Generate a random time within the specified range
    random_hour = random.randint(START_HOUR, END_HOUR)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    # Get today's date and set random time
    commit_date = datetime.datetime.now().replace(
        hour=random_hour, minute=random_minute, second=random_second
    )
    commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Create/modify a dummy file
    with open("auto_commit.txt", "a") as file:
        file.write(f"Auto commit on {commit_date_str}\n")

    # Add, commit with a random timestamp
    subprocess.run(["git", "add", "auto_commit.txt"])
    subprocess.run(["git", "commit", "--date", commit_date_str, "-m", f"Automated commit {commit_date_str}"])

# Determine GitHub remote URL (HTTPS with PAT or SSH)
if GITHUB_PAT:
    GITHUB_REMOTE = f"https://{GITHUB_USERNAME}:{GITHUB_PAT}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
else:
    GITHUB_REMOTE = f"git@github.com:{GITHUB_USERNAME}/{GITHUB_REPO}.git"

# Push to GitHub
subprocess.run(["git", "push", GITHUB_REMOTE, BRANCH])
