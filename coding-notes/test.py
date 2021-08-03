class treeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, root):
        if not root:
            return True

        return self.isSymmetricalTree(root.left, root.right)

    def isSymmetricalTree(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self.isSymmetricalTree(left.left, right.right) and self.isSymmetricalTree(left.right, right.left)

if __name__ == '__main__':
    root1 = treeNode(1)
    root1.left = treeNode(8)
    root1.right = treeNode(8)

    res = Solution().isSymmetrical(root1)
    print(res)
