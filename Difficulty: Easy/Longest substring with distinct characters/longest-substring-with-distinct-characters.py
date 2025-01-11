#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        MAX_CHAR=26
        if len(s) == 0 or len(s) == 1:
            return len(s)
    
        res = 0
        vis = [False] * MAX_CHAR
    
      
        left = 0
        right = 0
        while right < len(s):
    
            
            while vis[ord(s[right]) - ord('a')] == True:
                vis[ord(s[left]) - ord('a')] = False
                left += 1
    
            vis[ord(s[right]) - ord('a')] = True
    
            res = max(res, (right - left + 1))
            right += 1
    
        return res
            
               


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends