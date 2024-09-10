#https://leetcode.com/problems/binary-tree-postorder-traversal/
#recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post(node):
            if node is None:
                return
            post(node.left)
            post(node.right)
            ans.append(node.val)
        ans=[]
        post(root)
        return ans        
