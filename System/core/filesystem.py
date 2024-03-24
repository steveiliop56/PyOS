import os

class filesystem():
    def __init__(self, username):
        self.username = username
        self.homePath = "Filesystem/home/"
        self.userPath = f"Filesystem/home/{self.username}/"

        if not os.path.exists(self.homePath):
            os.mkdir(self.homePath)

        if not os.path.exists(self.userPath):
            os.mkdir(self.userPath)

    def pathExists(self, path):
        return os.path.exists(self.userPath + path)
    
    def getFiles(self):
        files = os.listdir(self.userPath)
        for i in range(len(files)):
            if os.path.isdir(os.path.join(self.userPath, files[i])):
                files[i] = files[i] + "/"
        return files

    def createFile(self, name, contents, path=""):
        if not path or path == "" or path.isSpace():
            writePath = self.userPath + name
        else:
            writePath = self.userPath + path + name
        f = open(writePath, "a")
        f.write(contents)
        f.close()

    def removeFile(self, path):
        try:
            os.remove(self.userPath + path)
            return True
        except:
            return False
        
    def removeDirectory(self, path):
        try:
            os.rmdir(self.userPath + path)
            return True
        except:
            return False

    def makeDirectory(self, path):
        os.mkdir(self.userPath + path)