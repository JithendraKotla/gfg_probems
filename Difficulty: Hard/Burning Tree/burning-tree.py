'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        # code here
        q=deque()
        
        q.append(root)
        parent_map={}
        
        while q:
            node=q.popleft()
            
            if node.data==target:
                target_add=node
            
            if node.left:
                q.append(node.left)
                parent_map[node.left]=node
            if node.right:
                q.append(node.right)
                parent_map[node.right]=node
            
        q1=deque()
        
        q1.append(target_add)
        
        vis=set()
        vis.add(target_add)
        maxi=0
        
        while q1:
            f1=0
            len_q=len(q1)
            
            for _ in range(len_q):
                node=q1.popleft()
                
                if node.left and node.left not in vis:
                    f1=1
                    q1.append(node.left)
                    vis.add(node.left)
                
                if node.right and node.right not in vis:
                    f1=1
                    q1.append(node.right)
                    vis.add(node.right)
                
                if node in parent_map and parent_map[node] not in vis:
                    f1=1
                    q1.append(parent_map[node])
                    vis.add(parent_map[node])
                
            if f1:
                maxi+=1
            else:
                break
        return maxi
            
                    
            
            
            
