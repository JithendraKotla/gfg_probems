class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        arr=[]
        
        for i in range(len(val)):
            arr.append([val[i],wt[i]])
        
        
        arr.sort(key=lambda x: x[0] / x[1], reverse=True)
        
        totalsum=0
        totalweight=0
        
        n=len(arr)
        
        for i in range(n):
            if totalweight + arr[i][1]<capacity:
                totalsum+=arr[i][0]
                totalweight+=arr[i][1]
            else:
                totalsum+= (capacity-totalweight)* (arr[i][0]/arr[i][1])
                break
        return totalsum
        