class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
    def __init__(self):
        self.L=[]
    def inorderTraversal(self, root: TreeNode):
        if root != None:
            self.inorderTraversal(root.left)
            self.L.append(root.val)
            self.inorderTraversal(root.right)
        return self.L
		
if __name__ == "__main__":
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	result = Solution().inorderTraversal(root)
	print(result)
