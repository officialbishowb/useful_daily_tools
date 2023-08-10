import os
import subprocess
import argparse

def clone_github_repo(repo_url):
    destination_dir = 'F:\\git_repos\\'

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    try:
        # Change the current working Directory
        os.chdir(destination_dir)
        # Clone the repository
        subprocess.check_output(['git', 'clone', repo_url])
        print(f"Repository cloned successfully into '{destination_dir}'")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Clone GitHub repositories.')
parser.add_argument('git_url', metavar='GIT_URL', type=str, help='URL of the GitHub repository')

args = parser.parse_args()

# Clone the GitHub repository
clone_github_repo(args.git_url)
