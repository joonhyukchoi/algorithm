# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from collections import deque

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         q = deque()
#         arr = []
#         q.append(root)
#         while q:
#             now = q.popleft()
#             if now == None:
#                 arr.append('null')
#                 continue
#             arr.append(now.val)
#             q.append(now.left)
#             q.append(now.right)
#         l = len(arr)
#         count = 0
#         while l != 0:
#             l = l // 2
#             count += 1
#         index = 1
#         while index < 2 ** (count - 2):
#             num = index + 1
#             print(arr[index:index + (num // 2)], arr[num * 2 - 2:num * 2 - (num // 2 + 2):-1])
#             if arr[index:index + (num // 2)] == \
#             arr[num * 2 - 2:num * 2 - (num // 2 + 2):-1]:
#                 pass
#             else:
#                 return False
#             index = num * 2 - 1
#         return True
            
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode):
            if left == None and right == None:
                return True
            elif left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            else:
                if left.val == right.val:
                    return isMirror(left.left, right.right) and isMirror(left.right, right.left)
                else:
                    return False
        if root == None:
            return False
        return isMirror(root.left, root.right)
    
            
            