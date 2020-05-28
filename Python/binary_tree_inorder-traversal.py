#Time:  O(n)
#Space: O(1)
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
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
class Solution1:
	def preorder(self,root):
		result,curr = [],root
		while curr:
			if curr.left == None:
				result.append(curr.val)
				curr = curr.right
			else:
    			
if __name__ == "__main__":
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	result = Solution().inorderTraversal(root)
	print(result)
