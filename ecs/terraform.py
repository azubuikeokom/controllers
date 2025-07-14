class Terraform:
    def __init__(self):
        pass
    def plan(self):
        """Plan terraform changes"""
        subprocess.run(["terraform","plan"],check=True,cwd=REPO_DIR)
    def apply(self):
        pass 
