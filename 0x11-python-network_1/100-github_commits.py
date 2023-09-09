#!/usr/bin/python3
"""List the 10 most recent commits on the given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    i = requests.get(url)
    commits = i.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                commits[a].get("sha"),
                commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass