'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

import sys
from collections import deque


class Solution:
    def height(self, root, ans):
        # base case
        if not root:
            return 0
        # recursive case
        LH = self.height(root.left, ans)
        RH = self.height(root.right, ans)
        ans[0] = max(ans[0], LH + RH)
        return max(LH, RH) + 1

    def diameter(self, root):
        ans = [0]  # Using a list to store the reference to an integer
        self.height(root, ans)
        return ans[0]

# {
 # Driver Code Starts
# Initial Template for Python 3


# Contributed by Sudarshan Sharma

sys.setrecursionlimit(500000)


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


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        k = Solution().diameter(root)
        print(k)

        print("~")

# } Driver Code Ends
