from .file import *
from .__node__ import FSNode


class Directory(FSNode):
    def __init__(self, parent) -> None:
        super().__init__(parent)
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
