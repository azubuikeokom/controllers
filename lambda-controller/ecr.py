class ECR:
    def __init__(self,event):
        self.event = event

    def getImageURI(self) -> str:
        ecr_repo = event['detail']['repository-name']
        image_tag = event['detail']['image-tag']
        image_uri = f"{ecr_repo}:{image_tag}"
        return image_uri