
from typing import List


class Solution:
    def LongestBitonicSequence(self, n : int, arr : List[int]) -> int:
        # code here
        n=len(arr)
        dp1=[1]*n
        dp2=[1]*n
        
        for i in range(n):
            for prev_ind in range(i):
                if arr[i]>arr[prev_ind] and dp1[i]<1+dp1[prev_ind]:
                    dp1[i]=1+dp1[prev_ind]
        maxi=0
        for i in range(n-1,-1,-1):
            for prev_ind in range(n-1,i,-1):
                if arr[i]>arr[prev_ind] and dp2[i]<1+dp2[prev_ind]:
                    dp2[i]=1+dp2[prev_ind]
          
        maxi = 0

   
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                maxi = max(maxi, dp1[i] + dp2[i] - 1)
    
        return maxi
        
        
