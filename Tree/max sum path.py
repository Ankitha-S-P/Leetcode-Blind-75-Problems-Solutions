#https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findmax(node,maxx):
            if not node:
                return 0
            left=max(0,findmax(node.left,maxx))
            right=max(0,findmax(node.right,maxx))
            maxx[0]=max(maxx[0],node.val+left+right)  
            return node.val+max(left,right) 
        maxx=[float('-inf')]      
        findmax(root,maxx)
        return maxx[0]
