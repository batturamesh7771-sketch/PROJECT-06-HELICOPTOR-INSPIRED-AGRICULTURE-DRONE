"""
Project 06: GitHub Deployment Helper Script
"""
import os
import subprocess
import sys

GITHUB_USER = "batturamesh7771-sketch"
REPO_NAME = "PROJECT-06-HELICOPTOR-INSPIRED-AGRICULTURE-DRONE"

def push(token):
    remote_auth_url = f"https://{GITHUB_USER}:{token}@github.com/{GITHUB_USER}/{REPO_NAME}.git"
    remote_clean_url = f"https://github.com/{GITHUB_USER}/{REPO_NAME}.git"
    cmds = [
        ["git", "add", "."],
        ["git", "commit", "-m", "Update Project 06 Agriculture Drone Repository"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "set-url", "origin", remote_auth_url],
        ["git", "push", "-u", "origin", "main"],
        ["git", "remote", "set-url", "origin", remote_clean_url],
    ]
    for c in cmds:
        res = subprocess.run(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "push" in c and res.returncode != 0:
            print(f"Push failed: {res.stderr}")
            return False
    return True

if __name__ == "__main__":
    token = os.environ.get("GITHUB_TOKEN") or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not token:
        print("Please provide GITHUB_TOKEN as an environment variable or argument.")
        sys.exit(1)
    if push(token):
        print("Successfully pushed to GitHub!")
    else:
        sys.exit(1)
