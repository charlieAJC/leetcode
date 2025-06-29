class Solution:
    def checkTree(self, root) -> bool:
        return root.val == root.left.val + root.right.val
