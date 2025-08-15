#User function Template for python3
class Solution:
	def isRepeat(self, s):
		# code here
		temp=s+s
		temp=temp[1:-1]
		
		if s in temp:
		    return 1
		return 0