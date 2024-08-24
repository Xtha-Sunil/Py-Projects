from github import Github
from datetime import datetime
import json
import os

# Get the current date in YYYY-MM-DD format
today_date = datetime.today().strftime("%Y-%m-%d")

# Get the API key from the repository secret
api_key = os.environ['api_key']
g = Github(api_key)

# GitHub username and repository
username = "Xtha-Sunil"
repo_name = "Greenify"
repo = g.get_repo(f"{username}/{repo_name}")

# Load the required number of commits from the JSON file
with open("./commit_data.json", "r") as file:
    data = json.load(file)
    # Get the number of commits for today's date,  default = 0
    commit_count = int(data.get(today_date, 0))

# Create the required number of files in the repository
for i in range(commit_count):
    file_path = f"{today_date}/file{i}.txt"
    file_content = "Automation is helpful."

    try:
        repo.create_file(
            path=file_path,
            message=f"Creating file {i}",
            content=file_content
        )
        print(f"Created file: {file_path}")
    except Exception as e:
        print(f"Failed to create file: {file_path}. Error: {e}")
