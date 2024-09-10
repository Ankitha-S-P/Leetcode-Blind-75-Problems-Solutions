#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=deque()
        q.append(root)
        if not root:
            return ans
        while q:
            level=[]
            qlen=len(q)
            for i in range(qlen):
                temp=q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right) 
            ans.append(level)
        return ans
