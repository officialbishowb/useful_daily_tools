import subprocess
import argparse
import datetime
import os

def git_push(comment):
    if not comment:
        comment = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subprocess.run(['git', 'add', '.'], cwd=os.getcwd())
    subprocess.run(['git', 'commit', '-m', comment], cwd=os.getcwd())
    subprocess.run(['git', 'push'], cwd=os.getcwd())

def main():
    parser = argparse.ArgumentParser(description="Do a Git push from the current directory.")
    parser.add_argument("-msg", help="Commit message")
    
    args = parser.parse_args()

    comment = args.msg

    git_push(comment)
    
    
if __name__ == "__main__":
    main()
