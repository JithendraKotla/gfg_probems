from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root):
        # code here:
        
        res=[]
        
        path=[]
        
        def pathi(node):
            if node is None:
                return 
            path.append(node.data)
            
            if node.left is None and node.right is None:
                res.append(path[:])
            else:
            
                pathi(node.left)
                pathi(node.right)
            path.pop()
        pathi(root)
        return res
                
        
        
            
        