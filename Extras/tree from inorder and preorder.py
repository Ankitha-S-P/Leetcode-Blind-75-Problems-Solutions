#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inod={}
        pre={}
        for i in range(len(inorder)):
            inod[inorder[i]]=i  
        def build(i,j,k):
            if i>j:
                return None
            index=inod[preorder[k]]
            size=index-i   
            root=TreeNode(preorder[k])
            root.left=build(i,index-1,k+1)
            root.right=build(index+1,j,k+size+1)
            return root
        return build(0,len(inorder)-1,0)
