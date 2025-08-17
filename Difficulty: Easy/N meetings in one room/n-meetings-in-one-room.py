#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        arr=[]
        for i in range(len(start)):
            arr.append([start[i],end[i],i+1])
        
        arr.sort(key= lambda x: (x[1],x[0]))
        
        endTime=arr[0][1]
        c=1
        
        for i in range(1,len(arr)):
            if arr[i][0]>endTime:
                c+=1
                endTime=arr[i][1]
            
        return c
            