from commands import Commands
from filesystem import Filesystem
from shell import Shell
from cpu import SBUCPU

if __name__ == "__main__":
    filesystem = Filesystem()
    cpu = SBUCPU()
    shell = Shell(cpu)
    shell.run()
