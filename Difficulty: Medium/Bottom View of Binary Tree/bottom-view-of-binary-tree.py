'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        
        d={}
        
        from collections import deque
        q=deque()
        
        q.append((root,0))  
        
        while q:
            node, line = q.popleft()
            
            if node.left:
                q.append((node.left,line-1))
            if node.right:
                q.append((node.right,line+1))
            
            if line not in d:
                d[line]={}
            if line in d:
                d[line]=node.data
        res=[]
        
        for x in sorted(d.keys()):
            res.append(d[x])
        return res
        
        
        