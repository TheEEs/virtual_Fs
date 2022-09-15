class FSNode:
    def __init__(self, parent,name):
        self.name = name
        self.permissions = 0o600
        self.parent = parent
        self.owner = FSNode.MACHINE.current_user