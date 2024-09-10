class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            height=1+max(depth(node.left),depth(node.right))
            return height
        return depth(root)    
