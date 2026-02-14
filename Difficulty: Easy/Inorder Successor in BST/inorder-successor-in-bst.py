'''
class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        sucess=-1
        
        while root:
            if root.data>x.data:
                sucess=root.data
                root=root.left
            else:
                root=root.right
        return sucess
            