

class Solution:
    def nextLargerElement(self, arr):
        stack, res = [], [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])
        return res

# {
 # Driver Code Starts
# Initial Template for Python 3


t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends
