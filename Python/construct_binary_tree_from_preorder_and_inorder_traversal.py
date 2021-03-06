"""
preorder:
    visit
    left
    right

inorder:
    left
    visit
    right

for in order everything in the left subtree is to the left of the root
we know every node is unique so we can find the parent of each subtree since we know in the other traversal what is to the left and right

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
[3,9,20,null,null,15,7]


preorder we see 3
  before 3 of inorder is the left subtree
9 is the parent of the left subtree
in preorder we skip until something in right subtree and get 20
  20 is parent of right subtree
    and so on...

the problem is how long we take to get to the middle or the parent of each subtree
    we repeat this process for each subtree which is O(N^2) in the case we have a skewed tree
    instead we can use hashmap, mape the {value at a given index: the index itself}

the idea is to quickly find the "middle" index to split our inorder into two subtrees since we immediately see it in preorder
then we build each subtree in the same manner by recursively splitting our inorder

        [9,3,15,20,7]
     [9]      3     [15,20,7]
      9            [15] 20 [7]
                      15    7

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        return self.buildOutSubTrees(0, 0, len(inorder) - 1, preorder, inorder, inorder_map)
    
    def buildOutSubTrees(self, preorderStart, inorderStart, inorderEnd, preorder, inorder, inorder_map):
        
        if preorderStart > len(preorder) - 1 or inorderStart > inorderEnd:
            return None
        
        # create current node
        root = TreeNode(preorder[preorderStart])
        
        """
        inordermid = 0
        for i in range(inorderStart, inorderEnd + 1):
            if root.val == inorder[i]:
                inordermid = i
        """
        inordermid = inorder_map[root.val]
            
        # build left subtree
        root.left = self.buildOutSubTrees(preorderStart + 1, inorderStart, inordermid - 1, preorder, inorder, inorder_map)
        
        # build right subtree
        root.right = self.buildOutSubTrees(preorderStart + (inordermid - inorderStart + 1), inordermid + 1, inorderEnd, preorder, inorder, inorder_map)
        
        return root
    
# O(N) time complexity, where N is the size of the given array, since we take advantage of constant lookup time when looking for middle value from the inorder list.
# O(N) space complexity since we are using a hashmap to store the inorder array, mapping values to index.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildOutSubTrees(0, 0, len(inorder) - 1, preorder, inorder)

    def buildOutSubTrees(self, preorderStart, inorderStart, inorderEnd, preorder, inorder):
        
        if preorderStart > len(preorder) - 1 or inorderStart > inorderEnd:
            return None
        
        # create current node
        root = TreeNode(preorder[preorderStart])
        
        # find the index in which the left subtree and right subtree nodes are located given the value of the parent
        inordermid = 0
        for i in range(inorderStart, inorderEnd + 1):
            if root.val == inorder[i]:
                inordermid = i
            
        # build left subtree
        root.left = self.buildOutSubTrees(preorderStart + 1, inorderStart, inordermid - 1, preorder, inorder)
        
        # build right subtree
        root.right = self.buildOutSubTrees(preorderStart + (inordermid - inorderStart + 1), inordermid + 1, inorderEnd, preorder, inorder)
        
        return root
    
# O(N^2) time complexity where N is the length of the given list. In a right skewed tree we will have to keep searching to the end for the index of the parent of subtrees in the inorder array.
# O(1) space complexity if we do not consider the recursive call stack.
