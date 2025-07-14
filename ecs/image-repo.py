class ECR:
    def __init__(self):
        self.client = boto3.client('ecr')
        
    def checkImageForChange(self,ecr_repo:str) -> bool:
        """Check if there is a change in the image in the ecr repo"""
        try:
            output = subprocess.check_output(["aws","ecr","describe-images","--repository-name",ecr_repo,"--query","'imageDetails[*].imageTags[0]'"],text=True)
            image_tags = json.loads(output)
            if not image_tags:
                return False
            latest_image_tag = image_tags[0]
            if re.match(r"^\d+\.\d+\.\d+$", latest_image_tag):
                return True
            else:
                return False
        except subprocess.CalledProcessError as e:
            print(f"Error checking ECR image: {e}")
            return False
        
    def getLatestImageDigest(self,ecr_repo:str) -> str:
        """Get the latest image digest from the ecr repo"""
        try:
            output = subprocess.check_output(["aws","ecr","describe-images","--repository-name",ecr_repo,"--query","'imageDetails[0].imageDigest'"],text=True)
            image_digest = json.loads(output)
            return image_digest
        except subprocess.CalledProcessError as e:
            print(f"Error getting ECR image digest: {e}")
            return ""