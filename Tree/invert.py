
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if not node:
                return
            temp=node.left
            node.left=node.right
            node.right=temp
            reverse(node.left)
            reverse(node.right)
        reverse(root)
        return root
