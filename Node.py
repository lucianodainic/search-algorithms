class Node:
    def __init__(self, state, parent=None, manh=None):
        self.parent = parent
        self.state = state
        self.children = []
        self.manh = manh
    
    def insert(self, node):
        self.children.append(node)

    def print_tree(self):
        if self.children :
            for i in self.children:
                i.print_tree()
        print(self.state)

    def print_tree_by_parent(self):
        if self.parent :
            self.parent.print_tree_by_parent()
        print(self.state)