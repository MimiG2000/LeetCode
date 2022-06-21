# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #same idea for alpha-beta-pruning
    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        return self.BST_helper(root, -float('inf'), float('inf'))
    
            
    def BST_helper(self,root, left, right):
        
            if root == None:    #leaf
                return True
            
            if left>=root.val or right<=root.val:   #no BST
                return False
            
            return self.BST_helper(root.left, left, root.val) and self.BST_helper(root.right, root.val, right)      
        
        