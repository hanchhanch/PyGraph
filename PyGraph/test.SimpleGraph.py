import unittest

from Graph import *
from PyGraph.SimpleGraph import SimpleGraph

class Test_test(unittest.TestCase):
    def test_A(self):
        g= SimpleGraph()
        node = {'id':'id1','label':'label1'}
        g.add_node(node['id'],  node)
        self.assertEqual(node['id'], g.get_node_by_id(node['id'])['id'])


if __name__ == "__main__" :
    unittest.main()
