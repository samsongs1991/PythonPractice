class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = list()

    def __repr__(self):
        return f'< Node {self.value} >'

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    @parent.setter
    def parent(self, node):
        if self.parent is node:
            return
        if self.parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            node.parent = self

    def remove_child(self, node):
        if node in self.children:
            self._children.remove(node)
            node.parent = None

    def depth_search(self, value):
        if self.value is value:
            return self
        for node in self.children:
            result = node.depth_search(value)
            if result is not None:
                return result
        return None

    def breadth_search(self, value):
        q = [self]
        while len(q) > 0:
            node = q.pop(0)
            if node.value is value:
                return node
            q.extend(node.children)
        return None
