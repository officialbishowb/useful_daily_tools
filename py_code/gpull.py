import subprocess
import argparse

def git_pull(path):
    subprocess.run(['git', 'pull'], cwd=path)

def main():
    parser = argparse.ArgumentParser(description="Do a Git pull from a specified path.")
    parser.add_argument("-path", required=True, help="Path to the Git repository")
    
    args = parser.parse_args()

    path = args.path

    git_pull(path)
    
    
if __name__ == "__main__":
    main()
    
