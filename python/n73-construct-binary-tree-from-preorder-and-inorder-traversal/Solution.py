"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(inorder) == 0:
            return None
        head        = TreeNode(preorder[0])
        ind         = inorder.index(head.val)       
        left, right = inorder[: ind], inorder[ind + 1: ]
        head.left   = self.buildTree(preorder[1: ind + 1], left)
        head.right  = self.buildTree(preorder[ind + 1: ], right)
        return head
