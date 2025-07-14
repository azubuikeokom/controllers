from git_repo import Repo
from dotenv import load_dotenv
import ecr
import os

load_dotenv()

def lambda_handler(event, context):
    """"Process imcoming ECR image upload event"""
    my_ecr = ecr.ECR(event)
    image_uri = my_ecr.getImageURI()
    REPO_URL = os.getenv("REPO_URL")
    repo = Repo(REPO_URL)
    repo.clone()
    repo.updateProjectVariables(image_uri)

    

