#https://leetcode.com/problems/binary-tree-preorder-traversal/
# recursion
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def pre(node):
            if node is None:
                return
            ans.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return ans 

#iterative preorder using stack
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=deque()
        if root is None:
            return ans
        q.append(root)
        while q:
            temp=q.pop()
            ans.append(temp.val)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)
        return ans
