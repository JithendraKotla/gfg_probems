#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        d={}
        
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        for i in b:
            if i not in d or d[i] == 0:
                return False
            else:
                d[i] -= 1

        return True
                
      
    
    
    
