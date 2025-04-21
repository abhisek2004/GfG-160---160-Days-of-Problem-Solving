from functools import reduce


class Solution:
    def missingNum(self, arr):
        # code here
        return reduce(lambda x, y: x ^ y, arr) ^ reduce(lambda x, y: x ^ y, range(1, len(arr)+2))

# {
 # Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends
