#!/usr/bin/env python3

"""
Sorts projects in README.md with GitHub links by commit activity, from oldest
to newest. This can help identify dead or inactive projects for removal.
"""

import os
import re
from datetime import datetime

import github


def main():
    """Main process."""

    # Read contents of README.md file
    contents = open("README.md", "r").read()
    gh_pattern = r"https?:\/\/github\.com\/([\w\.\-]+\/[\w\.\-]+)"
    gh_repos = list(set(re.findall(gh_pattern, contents)))

    # Create GitHub object for API queries, using token if available
    token = None
    if os.path.isfile(".gh_token"):
        with open(".gh_token", "r") as openfile:
            token = openfile.read().strip()
    g = github.Github(token)

    # Iterate through repos and build results array with last updated date
    results = []
    for idx, gh_repo in enumerate(gh_repos):
        print("Processing %s (%d of %d)..." % (gh_repo, idx + 1, len(gh_repos)))
        try:
            repo = g.get_repo(gh_repo)
            result = {
                "repo": gh_repo,
                "updated": datetime.strftime(repo.updated_at, "%Y-%m-%dT%H:%M:%S"),
            }
            # print("  %s" % repo.updated_at)
        except github.GithubException:
            # If repo doesn't exist, set updated to an empty string
            result = {"repo": gh_repo, "updated": ""}
            # print("  Error reading repo information. Repo may no longer exist.")
        results.append(result)

    # Print the results
    print("\nFound %d GitHub repositories. Sorted by date updated:" % len(gh_repos))
    results = sorted(results, key=lambda x: x["updated"])
    print("\n".join(([x["repo"] + " " + x["updated"] for x in results])))


if __name__ == "__main__":
    main()
