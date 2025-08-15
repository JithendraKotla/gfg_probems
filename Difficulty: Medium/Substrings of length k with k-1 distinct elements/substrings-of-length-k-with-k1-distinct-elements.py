class Solution:
    def substrCount(self, s, k):
        # code here
        l=0
        r=0
        n=len(s)
        
        cnt=0
        
        d={}
        
        while r<n:
            d[s[r]]=d.get(s[r],0)+1
            
            while r-l+1>k:
                d[s[l]]-=1
                if d[s[l]]==0:
                    del d[s[l]]
                l+=1
            
            if len(d)==k-1 and r-l+1==k:
                cnt+=1
            r+=1
            
        return  cnt
                
            