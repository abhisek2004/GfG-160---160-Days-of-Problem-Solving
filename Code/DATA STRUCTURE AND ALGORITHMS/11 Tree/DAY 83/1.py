# User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node


class Solution:
    def buildTree(self, inorder, preorder):
        # code here

        in_map = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0

        def constructTree(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = Node(root_val)

            in_index = in_map[root_val]

            root.left = constructTree(left, in_index - 1)
            root.right = constructTree(in_index + 1, right)

            return root

        return constructTree(0, len(inorder) - 1)
# {
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends
