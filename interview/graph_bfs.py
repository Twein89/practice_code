from collections import deque
from graph import State, Graph

class GraphBfs(Graph):

    def bfs(self, root, visit_func):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        root.visited_state = State.visited
        while queue:
            node = queue.popleft()
            visit_func(node)
            for adj_node in node.adj_nodes.values():
                if adj_node.visited_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visited_state = State.visited

class GraphDfs(Graph):

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visited_state = State.visited
        for node in root.adj_nodes.values():
            if node.visited_state == State.unvisited:
                self.dfs(node, visit_func)





class Results:
    def __init__(self):
        self.result = []

    def __repr__(self):
        return str(self.result)

    def add_result(self, node):
        self.result.append(node.key)

class TestBfs(object):

    def __init__(self):
        self.results = Results()


    def test_bfs(self):
        nodes = []
        # graph = GraphBfs()
        graph = GraphDfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        # graph.bfs(nodes[0], self.results.add_result)
        # print(self.results)
        graph.dfs(nodes[0], self.results.add_result)
        print(self.results)

if __name__ == '__main__':
    test = TestBfs()
    test.test_bfs()


