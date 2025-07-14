"""
An ECS controller to ensure ecs service managed by terraform is close to declarative
Author: Azubuike Okom
"""
import re 
import sys
import subprocess 
import os
import json 
import git
import boto3
from dotenv import load_dotenv
import random
from github import Github
from github import Auth 

load_dotenv()
REPO_DIR = os.getenv("REPO_DIR")
AUTH_TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("GIT_USERNAME")
TERRAFORM_PROJECTS = os.getenv("TERRAFORM_PROJECTS")
DATA_DIR = os.getenv("DATA_DIR")

class Repo:
    def __init__(self,repo_url:str):
        self.repo_url = repo_url

    def clone(self,branch:str="master") -> None:
        """ clone repo with master as the default branch"""
        local_repo = self.getLocalRepoFromURL()
        remote_url = self.recontructRepoURL()
        try:
            if os.path.exists(os.path.join(REPO_DIR,local_repo)):
                print(f"path:{os.path.join(REPO_DIR,local_repo)} already exists")
                sys.exit()
            else:
                self.cloned_repo = git.Repo.clone_from(remote_url,os.path.join(REPO_DIR,local_repo),branch=branch)
        except Exception as e:
            print(f"Exception: {e}")

    def getLocalRepoFromURL(self) -> str:
        """get repo name from url"""
        return self.repo_url.split("/")[-1].split(".")[0]
    
    def recontructRepoURL(self) -> str:
        """insert username and token to repo https url"""
        credential = USERNAME+":"+AUTH_TOKEN
        url_tokens = self.repo_url.split("/")
        domain = url_tokens[2]
        new_domain = credential+"@"+domain
        url_tokens[2] = new_domain
        recontructed_repo_url = "/".join(url_tokens)
        return recontructed_repo_url
    
    def createPR(self) -> None:
        """Creates a PR"""
        pass
    
    def mergePR(self,branch:str="main") -> None:
        """Merge PR to main by default"""
        pass
    
    def stageAndCommit(self,commit_message:str="Update terraform files") -> None:
        """Stage and commit changes to the repo"""
        try:
            commit_message = commit_message+" "+str(random.randint(1000,9999))
            self.cloned_repo.git.add(A=True)
            self.cloned_repo.index.commit(commit_message)
        except Exception as e:
            print(f"Error staging and committing changes: {e}")

    def pushChanges(self,branch:str="ecs-controller") -> None:
        """Push changes to the remote repo"""
        try:
            self.cloned_repo.git.push("origin", branch)
        except Exception as e:
            print(f"Error pushing changes: {e}")

    def updateProjectVariables(self,project_name:str,image_uri:str) -> None:
        """Update project variables in terraform files"""
        try:
            project_dir = os.path.join(REPO_DIR,project_name)
            if not os.path.exists(project_dir):
                print(f"Project directory {project_dir} does not exist.")
                return
            
            for root, dirs, files in os.walk(project_dir):
                for file in files:
                    if file.startswith("variables") and file.endswith(".tf"):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r') as f:
                            content = f.read()
                            content = re.sub(r'\d{12}\.dkr\.ecr\.[a-z0-9-]+\.amazonaws\.com/[a-zA-Z0-9-_]+(?::[a-zA-Z0-9._-]+)?', image_uri, content)
                        
                        with open(file_path, 'w') as f:
                            f.write(content)
        except Exception as e:
            print(f"Error updating project variables: {e}")        




    