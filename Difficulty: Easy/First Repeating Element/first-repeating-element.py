class Solution:
    def firstRepeated(self,arr):
        freq = {}
        # Count frequencies
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        
        # Find first element with freq > 1
        for i in range(len(arr)):
            if freq[arr[i]] > 1:
                return i + 1   # 1-based index
        return -1