class Solution:
    def rowWithMax1s(self, arr):
        # code here
        def lowerbound(arr,n,x):
            low=0
            high=n-1
            ans=n
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>=x:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        cnt_max=0
        index=-1
        n=len(arr)
        for i in range(n):
            cnt_ones=len(arr[i])-lowerbound(arr[i],len(arr[i]),1)
            if cnt_ones>cnt_max:
                cnt_max=cnt_ones
                index=i
        return index
        
                