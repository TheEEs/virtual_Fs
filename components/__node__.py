class FSNode:
    def __init__(self, parent):
        self.permissions = 0o600
        self.parent = parent
        self.owner = FSNode.MACHINE.current_user