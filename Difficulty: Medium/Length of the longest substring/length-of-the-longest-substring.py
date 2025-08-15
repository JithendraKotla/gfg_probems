#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):
        # code here
        l=0
        r=0
        n=len(s)
        d={}
        maxi=-1
        while r<n:
            if s[r] in d and d[s[r]]>=l:
                l=d[s[r]]+1
            
            d[s[r]]=r
            maxi=max(maxi, r-l+1)
            
            r+=1
            
           
        return maxi