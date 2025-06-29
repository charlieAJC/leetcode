# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution(object):
#     def recoverFromPreorder(self, traversal: str):
#         """
#         :type traversal: str
#         :rtype: Optional[TreeNode]
#         """

#         def getFirstIntInStr(t: str):
#             ind = 0
#             res = ""
#             for char in t:
#                 if char.isdigit():
#                     res += char
#                     ind += 1
#                 else:
#                     break
#             return [int(res), t[ind:]]

#         def get_first_dash_group_count(t: str):
#             sum = 0
#             for char in t:
#                 if char == "-":
#                     sum += 1
#                 else:
#                     break
#             return sum

#         def build_tree(tree: TreeNode):
#             if traversal:
#                 depth = get_first_dash_group_count(traversal)
#                 tree.val, traversal = getFirstIntInStr(traversal)
#                 if depth in stack:
#                     while depth in stack:
#                         stack.pop()
#                 else:
#                     stack.append()


#         stack = []
#         tree = TreeNode()
#         build_tree(tree)

#         # print(traversal.split("-", 1))
#         # return getFirstIntInStr(traversal)


# ===========================================================================
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        index = 0
        stack = []

        while index < len(S):
            depth = 0
            # 計算當前節點的深度
            while index < len(S) and S[index] == "-":
                depth += 1
                index += 1

            # 取得數字部分
            num_start = index
            while index < len(S) and S[index].isdigit():
                index += 1
            value = int(S[num_start:index])

            # 創建當前節點
            node = TreeNode(value)

            # 如果 stack 長度大於 depth，表示需要回到上一層
            while len(stack) > depth:
                stack.pop()

            # 根據 stack[-1] 設定新節點為左子或右子
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            # 將當前節點加入 stack
            stack.append(node)

        return stack[0]  # 返回根節點


# traversal = "1-2--3--4-5--6--7"
# Output: [1, 2, 5, 3, 4, 6, 7]

# traversal = "1-2--3---4-5--6---7"
# Output: [1, 2, 5, 3, None, 6, None, 4, None, 7]

traversal = "1-401--349---90--88"
# Output: [1, 401, None, 349, 88, 90]

print(Solution().recoverFromPreorder(traversal))
