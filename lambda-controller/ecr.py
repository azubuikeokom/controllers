class ECR:
    """Take in ECR Image Update event to return Image Repo properties"""
    def __init__(self,event):
        self.event = event

    def getImageURIAndRepoName(self) -> str:
        ecr_repo = self.event['detail']['repository-name']
        image_tag = self.event['detail']['image-tag']
        image_uri = f"{ecr_repo}:{image_tag}"
        return (image_uri,ecr_repo)

