from distutils.cmd import Command
from components import file_system

from components.file_system import FileSystem
from .user import User
from components import File, FileSystem, FSNode


class PermissionError(Exception):
    pass


class Machine:

    file_system : FileSystem = None

    def __init__(self) -> None:
        self.current_user = User("root")

my_machine = Machine()
FSNode.MACHINE = my_machine
my_machine.file_system = FileSystem()
