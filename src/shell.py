from commands import Commands
from filesystem import Filesystem

class Shell:
    def __init__(self, cpu):
        self.cpu = cpu
        self.filesystem = Filesystem()
        self.setup()
        self.commands = {
            "ls": Commands.ls,
            "cat": Commands.cat,
            "echo": Commands.echo,
            "rm": Commands.rm,
            "clear": Commands.clear,
            "help": Commands.help
        }

    def setup(self):
        self.filesystem.create_file("welcome.txt", "Welcome to SBCPU-16")
        self.filesystem.create_file("-", "test")

    def run(self):
        print("**** SBCPU-16 ****")
        print(f"{len(self.cpu.memory)} free bytes")
        while True:
            command = input("> ").strip()
            if command == "exit":
                break
            parts = command.split()
            if command == "":
                continue
            if parts[0] in self.commands:
                self.commands[parts[0]](self.filesystem, parts[1:])
            else:
                print("Command not found.")