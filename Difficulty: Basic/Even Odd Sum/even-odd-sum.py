#User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        e=0
        o=0
        for i in range(len(Arr)):
            if i%2==0:
                e+=Arr[i]
            else:
                o+=Arr[i]
        return e,o


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])
# } Driver Code Ends