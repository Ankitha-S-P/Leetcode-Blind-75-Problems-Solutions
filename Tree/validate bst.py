#https://leetcode.com/problems/validate-binary-search-tree/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root,low,high):
            if not root:
                return True
            return root.val>low and root.val<high and validate(root.left,low,root.val) and validate(root.right,root.val,high)
        return validate(root,float('-inf'),float('inf'))
