class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        l=0
        r=0
        n=len(s)
        d={}
        maxLen=-1
        while r<n:
            d[s[r]]= d.get(s[r], 0) + 1
            
            while (len(d)>k):
                d[s[l]]-=1
                if (d[s[l]]==0):
                    del d[s[l]]
                l+=1
            if (len(d)==k):
                maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen