import abc

class Node:
    """description of class"""

    def __init__(self, id, nodeObj = None):
        self.id = id
        self.org_obj = nodeObj


class Edge:
    """description of class"""

    def __init__(self, id):
        self.id = id


class Graph:
    @abc.abstractmethod
    def get_node(self, *options)->Node:
        pass
    
    @abc.abstractmethod
    def add_node(self, props)->Node:
        ## props- a dict of the node properties
        pass

    @abc.abstractmethod
    def del_node(self, *options)->Node:
        pass
        

