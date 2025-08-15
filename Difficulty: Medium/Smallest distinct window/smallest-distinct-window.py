#User function Template for python3

class Solution:
    def findSubString(self, str):
        # code here
        str_set_len=len(set(str))
        mini=len(str)
        
        l=0
        r=0
        d={}
        n=len(str)
        while r<n:
            d[str[r]]=d.get(str[r],0)+1
            
            while len(d)==str_set_len:
                mini=min(mini,r-l+1)
                d[str[l]]-=1
                if d[str[l]]==0:
                    del d[str[l]]
                l+=1
            r+=1
        return mini
            
            
    
    
    