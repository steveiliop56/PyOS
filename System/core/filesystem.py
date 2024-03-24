import os
import colorama as c

c.init(autoreset=True)

class filesystem():
    def __init__(self, username):
        self.username = username
        self.fsPath = "Filesystem"
        self.homePath = f"${self.fsPath}home"
        self.userPath = f"{self.fsPath}/home/{self.username}"

        if not os.path.exists(self.homePath):
            os.mkdir(self.homePath)

        if not os.path.exists(self.userPath):
            os.mkdir(self.userPath)

    def pathExists(self, path):
        return os.path.exists(f"{self.userPath}/{path}")
    
    def validatePath(self, path):
        newDir = path.split("/").pop(-1)
        os.chdir(newDir.join("/"))
        if self.username == "root":
            if os.getcwd().find(self.fsPath) == -1:
                print(c.Fore.YELLOW + "You can't exit the filesystem!")
                return False
            return True
        else:
            if os.getcwd().find(self.userPath) == -1:
                return False
            return True
    
    def getFiles(self):
        files = os.listdir(self.userPath)
        for i in range(len(files)):
            if os.path.isdir(os.path.join(f"{self.userPath}/{files[i]}")):
                files[i] = files[i] + "/"
        return files

    def createFile(self, name, contents, path=""):
        try:
            if not path or path == "" or path.isSpace():
                writePath = f"{self.userPath}/{name}"
            else:
                writePath = f"{self.userPath}/{path}/{name}"
            if self.validatePath(writePath):
                f = open(writePath, "a")
                f.write(contents)
                f.close()
                return True
            raise Exception
        except:
            return False

    def removeFile(self, path):
        try:
            deletePath = f"{self.userPath}/{path}"
            if self.validatePath(deletePath):
                os.remove(deletePath)
                return True
            raise Exception
        except:
            return False
        
    def removeDirectory(self, path):
        try:
            deletePath = f"{self.userPath}/{path}"
            if self.validatePath(deletePath):
                os.rmdir(deletePath)
                return True
            raise Exception
        except:
            return False

    def makeDirectory(self, path):
        try:
            makePath = f"{self.userPath}/{path}"
            if self.validatePath(makePath):
                os.mkdir(makePath)
                return True
            raise Exception
        except:
            return False