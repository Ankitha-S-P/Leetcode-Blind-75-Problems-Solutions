#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root or count[0]>=k:
                return
            inorder(root.left)
            count[0]+=1
            if count[0]==k:
                ans[0]=root.val
                return
            inorder(root.right)
        count=[0]
        ans=[0]
        inorder(root) 
        return ans[0]
