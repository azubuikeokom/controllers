class Fs:
    def __init__(self):
        pass
    
    def getFiles(self,dir_path:str) -> list:
        """Get all files in a directory"""
        try:
            return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        except FileNotFoundError as e:
            print(f"Directory not found: {e}")
            return []
    
    def readFile(self,file_path:str) -> str:
        """Read a file and return its content"""
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return ""
    
    def writeFile(self,file_path:str,content:str) -> None:
        """Write content to a file"""
        try:
            with open(file_path, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")
    
    def createDir(self,dir_path:str) -> None:
        """Create a directory if it does not exist"""
        try:
            os.makedirs(dir_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory: {e}")