import sys


class Solution:
    def findMaxSum(self, arr):
        # code here
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]

        prev2, prev1 = arr[0], max(arr[0], arr[1])

        for i in range(2, len(arr)):
            current = max(prev1, arr[i] + prev2)
            prev2, prev1 = prev1, current

        return prev1

# {
 # Driver Code Starts


sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends
