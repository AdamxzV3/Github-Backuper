import os
import shutil
import zipfile
import requests
import json

# Define the webhook URL and message data
webhook_url = 'REPLACEMEWITHYOURWEBHOOOKPLEASEORTHIWONTWORKIGLOLSOJUSTREPLACEMETHANKYOU'
webhook_data = {
    'username': 'GitHub Backup Bot',
    'avatar_url': 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png',
    'embeds': []
}

# Ask the user for the GitHub username
github_name = input("Enter the GitHub username: ")

# Get the list of repositories for the given user or organization
response = requests.get(f"https://api.github.com/users/{github_name}/repos")
repos = [repo["name"] for repo in response.json()]

# Create a new folder to store the backups
backup_folder = os.path.join(os.getcwd(), "github_backups")
os.makedirs(backup_folder, exist_ok=True)

# Clone each repository, add a README.txt file, and zip it up
for repo in repos:
    repo_url = f"https://github.com/{github_name}/{repo}.git"
    repo_backup_path = os.path.join(backup_folder, repo)
    shutil.rmtree(repo_backup_path, ignore_errors=True)
    os.system(f"git clone {repo_url} {repo_backup_path}")
    
    # Add a README.txt file to the repository
    readme_file = os.path.join(repo_backup_path, "README.txt")
    with open(readme_file, "w") as f:
        f.write("Made by CodePulse")
    
    backup_file = os.path.join(backup_folder, f"{repo}.zip")
    with zipfile.ZipFile(backup_file, "w", zipfile.ZIP_DEFLATED) as backup:
        for foldername, subfolders, filenames in os.walk(repo_backup_path):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                backup.write(filepath, os.path.relpath(filepath, repo_backup_path))

    # Remove the local copy of the repository
    shutil.rmtree(repo_backup_path, ignore_errors=True)

    # Create an embed for the backup and add it to the webhook data
    embed = {
        'title': repo,
        'url': f'https://github.com/{github_name}/{repo}',
        'description': f'Backup for {repo}',
        'color': 0x00ff00,
        'fields': [
            {'name': 'GitHub URL', 'value': f'https://github.com/{github_name}/{repo}'},
            {'name': 'Backup URL', 'value': f'{backup_file}', 'inline': True}
        ],
        'footer': {'text': 'Backup created by CodePulse'}
    }
    webhook_data['embeds'].append(embed)

    # Send the webhook data to the Discord server for this repository
    response = requests.post(webhook_url, data=json.dumps({'embeds': [embed]}), headers={'Content-Type': 'application/json'})
    if response.status_code == 204:
        print(f"Webhook Sented Sucesfully.")
    else:
        if response.status_code == 400:
             print(f"Error sending webhook for {repo} ({response.status_code}): {response.text}")
        

# Remove the unzipped repository folders
for repo in repos:
    repo_folder = os.path.join(backup_folder, repo)
    shutil.rmtree(repo_folder, ignore_errors=True)

# Remove the backup zip files
for repo in repos:
    backup_file = os.path.join(backup_folder, f"{repo}.zip")
