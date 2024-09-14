#https://leetcode.com/problems/maximum-width-of-binary-tree/

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([[root,0]])
        width=0
        while q:
            width=max(width,q[-1][1]-q[0][1]+1)
            qlen=len(q)
            minn=q[0][1]
            for _ in range(qlen):
                temp=q.popleft()
                if temp[0].left:
                    q.append([temp[0].left,2*(temp[1]-minn)+1])
                if temp[0].right:
                    q.append([temp[0].right,2*(temp[1]-minn)+2])           
        return width 
