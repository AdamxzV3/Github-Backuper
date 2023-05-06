<div align="center">
  
  ![GitHub Backup Bot Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

  # GitHub Backup Bot :robot: :floppy_disk:

  A Python script that backs up all repositories of a given GitHub user or organization, adds a README file to each repository, creates a zip file of each repository, and sends the backup information to a Discord server via webhook.

  :warning: This script uses the `git` command-line tool to clone repositories, so it must be installed on your system.

  ## Usage

  1. Clone the repository and install the required Python packages:
     ```
     git clone https://github.com/AdamxzV3/github-backup-bot.git
     cd github-backup-bot
     pip install -r requirements.txt
     ```
  
  2. Run the script and enter the GitHub username or organization name when prompted:
     ```
     python backup.py
     ```
  
  3. The backups will be stored in a new folder named `github_backups` in the same directory as the script.
  
  ## License

  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

  Made with :heart: by CodePulse

</div>
