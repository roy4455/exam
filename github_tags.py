from github import Github, GithubException
import sys
import os

#github_token = sys.argv[2]
commit_id = sys.argv[1]

# Create github object
#gh_obj = Github(github_token)
gh_obj = Github(os.environ['GITHUB_CREDENTIALS_USR'], os.environ['GITHUB_CREDENTIALS_PSW'])

# Get repo
repo = gh_obj.get_repo('roy4455/exam')

# Get tags
tags = repo.get_tags()

print("Total tags found: %s" % tags.totalCount)
if tags.totalCount > 0:
    latest_tag = tags[0]
    
    print("Latest tag found: %s" % latest_tag.name)

    # Get patch version
    current_version = int(latest_tag.name.split('.').pop())

    # Increment patch version
    new_version = current_version + 1

    # New tag
    new_tag = '.'.join(latest_tag.name.split('.')[:-1]) + '.' + str(new_version)

    print("Creating new tag: %s" % new_tag)

    try:
        # Create tag
        created_tag = repo.create_git_tag(tag=new_tag, message=new_tag, type="commit", object=commit_id)
        
        # Create git reference
        repo.create_git_ref('refs/tags/{}'.format(created_tag.tag), created_tag.sha)
        print("Created tag: %s successfully!" % new_tag)
    except GithubException as e:
        print("Failed to create tag because of below exception..")
        print(e)
        sys.exit(1)
