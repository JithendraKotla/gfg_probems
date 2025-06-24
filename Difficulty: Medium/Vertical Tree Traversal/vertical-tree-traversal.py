from collections import deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        # Dictionary to store nodes by their horizontal distance (hd)
        hd_map = {}
        
        # Queue for BFS: stores tuples of (node, hd)
        queue = deque()
        queue.append((root, 0))
        
        # Track the minimum hd to iterate later
        min_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            
            if hd not in hd_map:
                hd_map[hd] = []
            hd_map[hd].append(node.data)
            
            min_hd = min(min_hd, hd)
            
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Construct the result by iterating from min_hd to max_hd
        res = []
        i = min_hd
        while i in hd_map:
            res.append(hd_map[i])
            i += 1
        
        return res