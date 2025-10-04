'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        from collections import deque
        
        q=deque()
        
        d={}
        res=[]
        q.append((root,0))
        
        while q:
            node,line=q.popleft()
            
            if node.left:
                q.append((node.left,line-1))
            
            if node.right:
                q.append((node.right,line+1))
            if line in d:
                continue
            
            if line not in d:
                d[line]=[]
            
            d[line].append(node.data)
        for x in sorted(d.keys()):
            res.append(d[x][0])
        return res
            
                
            
        