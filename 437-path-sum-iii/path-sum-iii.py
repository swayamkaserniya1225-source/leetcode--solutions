# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.prefix=0
        dict1={0:1}
        self.count=0
        def pathsumr(root):
            if root:
                self.prefix+=root.val
                if self.prefix-targetSum in dict1:
                    self.count+=dict1[self.prefix-targetSum]
                dict1[self.prefix]=dict1.get(self.prefix,0)+1
                pathsumr(root.left)
                pathsumr(root.right)
                dict1[self.prefix]-=1
                self.prefix-=root.val
        pathsumr(root)
        return self.count

        