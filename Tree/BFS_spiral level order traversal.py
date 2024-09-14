#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        ans=[]
        if not root:
            return ans
        while q:
            qlen=len(q)
            qlist=[]
            for _ in range(qlen):
                temp=q.popleft()
                qlist.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ans.append(qlist)
        return ans
