# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    This solution outputs the post order traversal of a tree iteratively.
    It does so by adding the root in the first position of the list
    then it adds the left and the right child to the stack named 'q'
    it then pops out the right child and then appends that to the list.
    It then pops out the left child and then adds that to the list.

    In the end we get a list of the form: [left, right, root]
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        q = [root]
        res = []
        while q:
            node = q.pop()
            if not node:
                continue
            res.insert(0, node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    '''
    This solution outputs the post order traversal of a tree recursively.
    This is a very trivial solution.
    It first checks out the left tree and then the right tree and then finally the root node
    It prints out in the form: [left, right, root]
    '''
    def printPostorder(self, root: TreeNode):

        if root:
            # First recur on left child
            self.printPostorder(root.left)

            # the recur on right child
            self.printPostorder(root.right)

            # now print the data of node
            print(root.val, "->")