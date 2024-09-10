#https://leetcode.com/problems/subtree-of-another-tree/
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(node1,node2):
            if not node1 or not node2:
                return node1==node2
            return node1.val==node2.val and same(node1.left,node2.left) and same(node1.right,node2.right)

        if not root or not subRoot:
            return root==subRoot
        q=deque()
        q.append(root)   
        while q:
            temp=q.popleft()
            if temp.val==subRoot.val and same(temp,subRoot):
                return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False
