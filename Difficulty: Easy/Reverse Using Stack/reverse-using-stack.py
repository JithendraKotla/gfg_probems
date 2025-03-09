#{ 
 # Driver Code Starts

# } Driver Code Ends

def reverse(S):
    st=[]
    for i in range(len(S)):
        st.append(S[i])
    
    res=""
    while st:
        res+=st.pop()
    return res
    
    #Add code here


#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
        print("~")
# } Driver Code Ends