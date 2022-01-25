from Node import Node
class Edge:
    def __init__(self, node, connected_node) -> None:
        self.node = node
        self.connected_node = connected_node
        pass
    def set_node(self, new_node):
        self.node = new_node
    def set_connected_node(self, new_node):
        self.connected_node = new_node
    def get_node(self):
        return self.node
    def get_connected_node(self, node:Node):
        if(node!=self.connected_node):
            return self.connected_node
        else:
            return self.node