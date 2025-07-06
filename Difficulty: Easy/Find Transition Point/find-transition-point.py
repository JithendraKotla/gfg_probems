class Solution:
    def transitionPoint(self, arr): 
        # Code here
        low=0
        high=len(arr)-1
        first=-1
        
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==1:
                first=mid
                high=mid-1
            else:
                low=mid+1
        return first
                