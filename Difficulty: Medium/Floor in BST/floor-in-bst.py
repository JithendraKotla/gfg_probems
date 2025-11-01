#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        floor=-1
        while (root):
            if root.data == x:
                floor = root.data
                return floor
            elif root.data<x:
                floor=root.data
                root=root.right
            else:
                root=root.left
        return floor