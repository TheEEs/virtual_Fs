from .directory import *
from .file import *


class FileSystem:
    def __init__(self) -> None:
        self.rootfs = Directory(None)
        self.current_working_directory = self.rootfs

    def find_path(self, path: str):
        if path.startswith("/"):
            r = self.rootfs
        else:
            r = self.current_working_directory
        try:
            for p in path.split("/"):
                r = r[p]
        except QueryError:
            raise QueryError(path)
        return r

    def cd(self, path: str) -> None:
        r = self.find_path(path)
        if type(r) is Directory:
            self.current_working_directory = r
        else:
            raise QueryError(path)
