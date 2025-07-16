class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        
        #code here
        if len(arr)<k:
            return -1
        def check(arr,mid):
            students=1
            pagesstudent=0
            n=len(arr)
            for i in range(n):
                if arr[i]+pagesstudent<=mid:
                    pagesstudent+=arr[i]
                else:
                    pagesstudent=arr[i]
                    students+=1
            return students
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            if check(arr,mid)>k:
                low=mid+1
            else:
                high=mid-1
        return low
            
            
