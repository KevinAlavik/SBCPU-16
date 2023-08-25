from os import system, name

class Commands:
    @staticmethod
    def ls(filesystem, args):
        if len(args) == 0:
            args = ['/']
        for path in args:
            components = path.split("/")
            current_dir = filesystem.root
            if components[0] == '':
                components.pop(0)  # Remove empty first component
            for component in components:
                if component == '':
                    continue  # Skip empty component
                if component in current_dir.subdirectories:
                    current_dir = current_dir.subdirectories[component]
                else:
                    print(f"Directory '{component}' not found.")
                    break
            else:
                print(f"Contents of '{path}':")
                for name in current_dir.subdirectories:
                    print(f"  {name}/")
                for name in current_dir.files:
                    print(f"  {name}")

    @staticmethod
    def cat(filesystem, args):
        if len(args) != 1:
            print("Usage: cat <filename>")
            return
        content = filesystem.read_file(args[0])
        if content is not None:
            print(content)
        else:
            print(f"File '{args[0]}' not found.")

    @staticmethod
    def echo(filesystem, args):
        if len(args) < 1:
            print("Usage: echo <content>")
            return
        content = " ".join(args)  # Join elements into a single string
        print(content)


    @staticmethod
    def rm(filesystem, args):
        if len(args) != 1:
            print("Usage: rm <filename>")
            return
        if filesystem.delete_file(args[0]):
            print(f"File '{args[0]}' deleted.")
        else:
            print(f"File '{args[0]}' not found.")

    @staticmethod
    def clear(filesystem, args):
        if name == 'posix':
            system('clear')
        elif name == 'nt':
            system('cls')

    @staticmethod
    def help(filesystem, args):
        print("Available commands:")
        print("ls [path]      List contents of a directory")
        print("cat <filename> Display the content of a file")
        print("echo <content> > <filename> Create a new file with content")
        print("rm <filename>  Delete a file")
        print("clear          Clear the screen")
        print("help           Display this help message")
