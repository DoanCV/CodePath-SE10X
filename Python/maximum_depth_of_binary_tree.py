from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are looking for the maximum depth

same idea as tree level traversal but we do not keep track of the nodes at each level, instead we keep track of the depth and return it once we are at the bottom
"""

def find_maximum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  depth = 0
  while queue:
    depth += 1
    curr_level_size = len(queue)

    for _ in range(curr_level_size):
      curr_node = queue.popleft()

      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)
      
  return depth

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we have to visit every node once.
# O(N) space complexity since in the worst case the bottom level will have N/2 nodes which is asymptotically N.

"""
DFS iterative solution
We use a stack and store (node, depth)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Iterative DFS, using a stack
        """
        maxDepth = 0
        if root is None:
            return maxDepth
        
        stack = []
        stack.append((root, 1))
        
        while stack:
            
            # pop from stack to get current node and depth
            curr_node, curr_depth = stack.pop()
            
            if curr_node is None:
                continue
            
            # check if leaf node
            # if it has children, push into stack with depth + 1
            if curr_node.left or curr_node.right:
                stack.append((curr_node.left, curr_depth + 1))
                stack.append((curr_node.right, curr_depth + 1))
        
            # check if depth is greater than maxDepth, if so update
            if curr_depth > maxDepth:
                maxDepth = curr_depth
        
        # return maxDepth
        return maxDepth
      
"""
DFS recursive solution
Compare left and right subtree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return 1 + max(left,right)
