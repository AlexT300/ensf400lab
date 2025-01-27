from github import Github

# or using an access token
g = Github("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")
repo = g.get_repo("jabezchowdhury/ensf400lab")

## Complete your tasks from here

# Get all branches
branches = repo.get_branches()
for branch in branches:
    print(f"Branch name: {branch.name}")

# Get all pull requests
pulls = repo.get_pulls(state='all', sort='created', direction='desc')
for pr in pulls:
    print(f"PR Title: {pr.title}, Created by: {pr.user.login}, URL: {pr.html_url}")

# Get a list of commits you have created in your main branch.
main_branch = repo.get_branch("main")
commits = repo.get_commits(sha=main_branch.name)

for commit in commits:
    print(f"Commit SHA: {commit.sha}, Message: {commit.commit.message}")

