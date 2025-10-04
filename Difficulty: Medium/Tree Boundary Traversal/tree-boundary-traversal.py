'''
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        
        def isLeaf(node):
            return node.left is None and node.right is None
        arr=[]
        # code here
        def leftBoundary(node):
            if not isLeaf(node):
                arr.append(node.data)
                if node.left:
                    leftBoundary(node.left)
                else:
                    leftBoundary(node.right)
        res=[]
        def addLeaves(node):
            if isLeaf(node):
                res.append(node.data)
                return
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)

        arr1=[]
        
        
        def rightBoundary(node):
            if not isLeaf(node):
                arr1.append(node.data)
                if node.right:
                    rightBoundary(node.right)
                else:
                    rightBoundary(node.left)
        final_ans=[]
        
        if not root:
            return final_ans
        if isLeaf(root):
            return [root.data]
        final_ans.append(root.data)
        if root.left:
            leftBoundary(root.left)
        final_ans.extend(arr)
        addLeaves(root)
        final_ans.extend(res)
        if root.right:
            rightBoundary(root.right)
        final_ans.extend(arr1[::-1])
        return final_ans
        
        