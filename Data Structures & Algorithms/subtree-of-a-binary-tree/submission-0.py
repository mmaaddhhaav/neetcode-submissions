# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if p is None and q is None:
                return p == q
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            left = sameTree(p.left, q.left)
            if left == False:
                return False
            right = sameTree(p.right, q.right)
            if right == False:
                return False
            return left and right
        def has_subTree(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            return has_subTree(root.left) or has_subTree(root.right)
        return has_subTree(root)