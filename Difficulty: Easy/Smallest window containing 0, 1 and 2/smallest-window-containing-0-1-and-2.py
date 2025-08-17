#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        # Code here
        l=0
        r=0
        n=len(s)
        
        d={}
        res=""
        mini=float("inf")
        
        while r<n:
            d[s[r]]=d.get(s[r],0)+1
            
            while len(d)==3:
                if r-l+1<mini:
                    mini=r-l+1
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
           
                
                  
            
            r+=1
        if mini!=float("inf"):
            return mini
        else:
            return -1