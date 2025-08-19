#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        
        t=0
        wt=0
        
        for i in bt:
            
            wt+=t
            t+=i
        return wt//len(bt)