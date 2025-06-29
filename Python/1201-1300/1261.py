# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements(object):
    def __init__(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        """
        self.tree_info = set()  # 用來儲存樹中的所有數值，方便 O(1) 查找
        root.val = 0  # 設定根節點為 0

        def fix_tree(node: TreeNode):
            self.tree_info.add(node.val)  # 將當前節點值存入集合

            if node.left:  # 修復左子節點
                node.left.val = node.val * 2 + 1
                fix_tree(node.left)
            if node.right:  # 修復右子節點
                node.right.val = node.val * 2 + 2
                fix_tree(node.right)

        fix_tree(root)  # 開始修復

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.tree_info
