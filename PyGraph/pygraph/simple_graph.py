import abc
from pygraph.graph import Node, Graph

class SimpleGraph(Graph):
    """description of class"""
    _nodes={}
    _edges={}

    def __init__(self):
        pass

    def print()->str:
        pass

    def get_node(self, options):
        if 'id' in options:
            return get_node_by_id(self, options['id'])

    def get_node_by_id(self, nodeId)->Node:
        return self._nodes[nodeId].org_obj

    def add_node(self, nodeId, NodeObj):
        self._nodes[nodeId] = Node(nodeId, NodeObj)

