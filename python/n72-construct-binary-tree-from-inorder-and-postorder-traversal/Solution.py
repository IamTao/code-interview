"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
         if len(inorder) == 0:
             return None
        ind = inorder.index(postorder[-1])
        parent = TreeNode(postorder[-1])
        parent.left = self.buildTree(inorder=inorder[:ind], postorder=postorder[: ind])
        parent.right = self.buildTree(inorder=inorder[ind + 1:], postorder=postorder[ind: -1])
        return parent
