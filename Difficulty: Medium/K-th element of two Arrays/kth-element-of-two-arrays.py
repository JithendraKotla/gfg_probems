#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        pass
        i=0
        j=0
        m=len(a)
        n=len(b)
        d=0
        arr=[0]*(m+n)
        while i<m and j<n:
            if a[i]<b[j]:
                arr[d]=a[i]
                i+=1
            else:
                arr[d]=b[j]
                j+=1
            d+=1
        while i<m:
            arr[d]=a[i]
            i+=1
            d+=1
        while j<n:
            arr[d]=b[j]
            j+=1
            d+=1
        return arr[k-1]
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends