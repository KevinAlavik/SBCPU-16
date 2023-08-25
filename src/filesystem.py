class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

class Filesystem:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, path, content=""):
        components = path.split("/")
        current_dir = self.root

        for component in components[:-1]:
            if component not in current_dir.subdirectories:
                current_dir.subdirectories[component] = Directory(component)
            current_dir = current_dir.subdirectories[component]

        filename = components[-1]
        current_dir.files[filename] = File(filename, content)

    def read_file(self, path):
        components = path.split("/")
        current_dir = self.root

        for component in components[:-1]:
            if component in current_dir.subdirectories:
                current_dir = current_dir.subdirectories[component]
            else:
                return None

        filename = components[-1]
        if filename in current_dir.files:
            return current_dir.files[filename].content
        else:
            return None

    def write_file(self, path, content):
        components = path.split("/")
        current_dir = self.root

        for component in components[:-1]:
            if component in current_dir.subdirectories:
                current_dir = current_dir.subdirectories[component]
            else:
                return False

        filename = components[-1]
        if filename in current_dir.files:
            current_dir.files[filename].content = content
            return True
        else:
            return False

    def delete_file(self, path):
        components = path.split("/")
        current_dir = self.root

        for component in components[:-1]:
            if component in current_dir.subdirectories:
                current_dir = current_dir.subdirectories[component]
            else:
                return False

        filename = components[-1]
        if filename in current_dir.files:
            del current_dir.files[filename]
            return True
        else:
            return False
