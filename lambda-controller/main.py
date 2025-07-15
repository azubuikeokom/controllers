from git_repo import Repo
from dotenv import load_dotenv
import ecr
import os



def lambda_handler(event, context):
    """"Process imcoming ECR image upload event"""
    my_ecr = ecr.ECR(event)
    image_uri, repo_name = my_ecr.getImageURIAndRepoName()
    REPO_URL = os.getenv("REPO_URL")
    repo = Repo(REPO_URL)
    project = repo.modifyProjectName(repo_name)
    repo.clone()
    repo.updateProjectVariables(project,image_uri)



