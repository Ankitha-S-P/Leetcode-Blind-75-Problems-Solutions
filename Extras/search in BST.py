#https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node,val):
            if not node:
                return None
            if node.val==val:
                return node
            if val<node.val:
                return search(node.left,val)
            if val>node.val:
                return search(node.right,val) 
        return search(root,val)             
