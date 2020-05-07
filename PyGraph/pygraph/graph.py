import abc

class Node:
    """description of class"""

    def __init__(self, node_data = {}, id = ""):
        self.id = id
        self.data = node_data


class Edge:
    """description of class"""

    def __init__(self, source_node_id:str, target_node_id:str, edge_data = {}, id = ""):
        self.source_id = source_node_id
        self.target_id = target_node_id
        self.data = edge_data
        if 'source_id' not in self.data:
            self.data['source_id'] = self.source_id
            self.data['target_id'] = self.target_id
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
        

