#User function Template for python3
class Solution:
    # Function to find a continuous sub-array which adds up to a given number.
    def subarray_sum(self, arri, total_sum):
        # Your code here
        l=0
        r=0
        n=len(arri)
        
        arr=[]
        sum=0
        
        while r<n:
            sum+=arri[r]
            while total_sum<sum and l<=r:
                sum-=arri[l]
                l+=1
            if total_sum==sum and l<=r:
                arr.append(l+1)
                arr.append(r+1)
                return arr
            r+=1
        return []
            