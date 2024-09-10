#https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def pre(node1,node2):
            if node1 is None or node2 is None:
                return node1==node2
            return node1.val==node2.val and pre(node1.left,node2.left) and pre(node1.right,node2.right) 
            
        return pre(p,q) 
