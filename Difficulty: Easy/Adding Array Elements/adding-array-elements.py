import heapq
class Solution:
    
    def minOperations(self, arr, n, k):
        # code here
        heap=[]
        for i in arr:
            heapq.heappush(heap,i)
        res=0
        
        while heap[0]<k:
            if len(heap)<2:
                return -1
            
            c1=heapq.heappop(heap)
            c2=heapq.heappop(heap)
            
            heapq.heappush(heap,c1+c2)
            res+=1
            
        return res
            
        



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().minOperations(arr, n, k)
        print(ans)
        tc -= 1


        print("~")
# } Driver Code Ends