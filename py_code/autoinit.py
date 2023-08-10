import argparse
import subprocess

def initialize_repo(url, branch="main", commit_msg="Initial commit"):
    # Initialize a Git repository
    subprocess.run(["git", "init"])

    # Add the remote URL
    subprocess.run(["git", "remote", "add", "origin", url])

    # Set the default branch
    subprocess.run(["git", "checkout", "-b", branch])

    # Create an initial commit
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_msg])

    # Push to the remote repository
    subprocess.run(["git", "push", "-u", "origin", branch])

def main():
    parser = argparse.ArgumentParser(description="Initialize and push a Git repository.")
    parser.add_argument("-url", required=True, help="Remote repository URL")
    parser.add_argument("-branch", default="main", help="Default branch (def: main)")
    parser.add_argument("-msg", default="Initial commit", help="Commit message (def: 'Initial commit')")
    
    args = parser.parse_args()

    url = args.url
    branch = args.branch
    commit_msg = args.msg

    initialize_repo(url, branch, commit_msg)
    print("Repository initialized and pushed successfully.")

if __name__ == "__main__":
    main()
