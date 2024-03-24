import os

class filesystem():
    def __init__(self, username):
        self.username = username
        self.home_path = "Filesystem/home/"
        self.user_path = f"Filesystem/home/{self.username}/"

        if not os.path.exists(self.home_path):
            os.mkdir(self.home_path)

        if not os.path.exists(self.user_path):
            os.mkdir(self.user_path)

    def path_exists(self, path):
        return os.path.exists(self.user_path + path)
    
    def get_files_folders(self):
        files = os.listdir(self.user_path)
        for i in range(len(files)):
            if os.path.isdir(os.path.join(self.user_path, files[i])):
                files[i] = files[i] + "/"
        return files

    def create_file(self, name, contents, path=""):
        if not path or path == "" or path.isSpace():
            write_path = self.user_path + name
        else:
            write_path = self.user_path + path + name
        f = open(write_path, "a")
        f.write(contents)
        f.close()

    def delete(self, path):
        try:
            os.remove(self.user_path + path)
            return True
        except:
            return False
        
    def remove_directory(self, path):
        try:
            os.rmdir(self.user_path + path)
            return True
        except:
            return False

    def make_directory(self, path):
        os.mkdir(self.user_path + path)