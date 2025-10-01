#User function Template for python3

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        from collections import deque
        q=deque()
        
        dist=[float("inf") for _ in range(10**5)]
        
        dist[start]=0
        
        q.append((start,0))  #node, steps
        
        mod = 10**5
        
        while q:
            node , steps= q.popleft()
            
            for i in arr:
                num=(node * i) % mod
                
                if steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    
                    q.append((num,steps+1))
        if dist[end]==float("inf"):
            return -1
        return dist[end]
        
            