#User function Template for python3

class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        # code here
        st=[]
        for i in range(len(s)):
            if not st:
                st.append(s[i])
            
            if st[-1]!=s[i]:
                st.append(s[i])
            
            else:
                continue
        return "".join(st)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        obj = Solution()
        print(obj.removeConsecutiveDuplicates(str(input())))
        print("~")
# } Driver Code Ends