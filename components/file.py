from .__node__ import FSNode


class QueryError(Exception):
    pass


class File(FSNode):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def __getitem__(self, item):
        raise QueryError(item)
