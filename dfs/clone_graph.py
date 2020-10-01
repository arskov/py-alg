"""
133	 Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        visited = {}
        
        def dfs(cur, new_node):
            print(cur.val, new_node.val)
            if cur.neighbors:
                new_node.neighbors = []
            for child in cur.neighbors:
                if child.val in visited:
                    new_node.neighbors.append(visited[child.val])
                else:
                    new_child = Node(child.val)
                    visited[child.val] = new_child
                    new_node.neighbors.append(new_child)
                    dfs(child, new_child)
        
        clone_node = Node(node.val)
        visited[node.val] = clone_node
        dfs(node, clone_node)
        return clone_node
            