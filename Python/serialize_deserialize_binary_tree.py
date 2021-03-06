# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Serialize
pre order traversal
    when we do not have a node add "x"
join with a comma

ex.
              1
             / \
            2   3
               / \
              4   5 

the parentheses are there to help but return (1, (2, x, x), (3, (4, x, x), (5, x, x))) 
    -> "1,2,x,x,3,4,x,x,5,x,x"

O(N) time since we visit each node once


Deserialize
use a queue to reconstruct the tree
    discard the "x" when we see it
    
queue = [1,2,x,x,3,4,x,x,5,x,x]

1                           root
(2, x, x)                   left
(3, (4, x, x), (5, x, x))   right

O(N) time since we visit each element of data once

"""
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # if a node is empty, add 'x' to string
        if not root:
            return "x"
        
        return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(queue):
            
            if queue[0] == "x":
                queue.popleft()
                return None
            
            root = TreeNode(queue.popleft())
            
            root.left = dfs(queue)
            root.right = dfs(queue)
            return root
            
        queue = deque(data.split(","))
        return dfs(queue)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
