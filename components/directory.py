from lib2to3.pytree import Node
from .file import *
from .__node__ import FSNode


class Directory(FSNode):
    def __init__(self, parent, name) -> None:
        super().__init__(parent, name)
        self.name = name
        self.content = {"": self}

    def __getitem__(self, name: str) -> FSNode or None:
        if name == ".":
            return self
        elif name == "..":
            if not self.parent:
                return self
            return self.parent
        else:
            r = self.content.get(name)
            if not r:
                raise QueryError(name)
            return r

    def __setitem__(self, name: str, content: FSNode) -> None:
        self.content[name] = content

    def full_path(self):
        if not self.parent:
            return ''
        else:
            return f"{self.parent.full_path()}/{self.name}"

    def add_dir(self, name):
        self.content[name] = d = Directory(self, name)
        return d

    def add_file(self, name):
        self.content[name] = f = File(self, name)
        return f
