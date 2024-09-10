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
    # 2 stack   
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack1=[root]
        stack2=[]
        if root is None:
            return stack2
        while stack1:
            temp=stack1.pop()
            if temp.left:
                stack1.append(temp.left)
            if temp.right:
                stack1.append(temp.right)
            stack2.append(temp.val)
        stack2.reverse()     
        return stack2 
