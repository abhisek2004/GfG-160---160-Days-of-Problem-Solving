# User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque


class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        def preorder(node):
            if not node:
                arr.append(-1)
            else:
                arr.append(node.data)
                preorder(node.left)
                preorder(node.right)
        arr = []
        preorder(root)
        return arr

    # Function to deserialize a list and construct the tree.

    def deSerialize(self, arr):
        def de():
            nonlocal index
            if index >= len(arr) or arr[index] == -1:
                index += 1
                return None
            node = Node(arr[index])
            index += 1
            node.left = de()
            node.right = de()
            return node
        index = 0
        return de()


# {
 # Driver Code Starts
# Initial Template for Python 3
# Initial Template for Python 3
# Contributed by Suman Rana


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def _deleteTree(node):
    if (node == None):
        return

    # first delete both subtrees
    _deleteTree(node.left)
    _deleteTree(node.right)
    node.left = None
    node.right = None
    # then delete the node


# Deletes a tree and sets the root as NULL
def deleteTree(node_ref):
    _deleteTree(node_ref)
    node_ref = None


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        root = buildTree(input())
        ob = Solution()
        A = ob.serialize(root)
        deleteTree(root)
        root = None
        r = ob.deSerialize(A)
        inorder(r)
        print()

        print("~")
# } Driver Code Ends
