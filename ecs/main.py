"""
An ECS controller to ensure ecs service managed by terraform is close to declarative
Author: Azubuike Okom
"""
import re 
import sys 
import os
import json 
import git
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR")
AUTH_TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("GIT_USERNAME")

class Repo:
    def __init__(self,repo_url:str):
        self.repo_url = repo_url

    def clone(self,branch:str="master") -> None:
        """ clone repo with master as the default branch"""
        local_repo = self.getLocalRepoFromURL()
        remote_url = self.recontructRepoURL()
        try:
            if os.path.exists(os.path.join(DATA_DIR,local_repo)):
                print(f"path:{os.path.join(DATA_DIR,local_repo)} already exists")
                sys.exit()
            else:
                self.cloned_repo = git.Repo.clone_from(remote_url,os.path.join(DATA_DIR,local_repo),branch=branch)
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



    
class Terraform:
    def __init__(self):
        pass
    def plan(self):
        pass 
    def apply(self):
        pass 


class AWS:
    def __init__(self):
        pass