# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        # code here
        left=0
        n=len(arr)
        pivot=0
        right=sum(arr[1:])
        while pivot <n-1 and left!=right:
            pivot+=1
            right-=arr[pivot]
            left+=arr[pivot-1]
        if left==right:
            return pivot+1
        else:
            return -1
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.equilibriumPoint(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends