from .__node__ import FSNode


class QueryError(Exception):
    pass


class File(FSNode):
    def __init__(self, parent,name) -> None:
        super().__init__(parent,name)

    def __getitem__(self, item):
        raise QueryError(item)
