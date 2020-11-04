class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    from collections import deque
    #Write your code here
    if not root:
        return
    q = deque()
    v = dict()
    q.append((root, 0))
    while q:
        pair = q.popleft()
        hight = pair[1]
        node = pair[0]
        if not hight in v:
            v[hight] = node.info
        if node.left:
            q.append((node.left, hight - 1))
        if node.right:
            q.append((node.right, hight + 1))
    for i in sorted(v):
        print(v[i], end = " ")
            


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)