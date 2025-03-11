import sys
import io
import atexit


class Solution:
    def countWays(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1, 2
        for i in range(3, n+1):
            curr = b+a
            a, b = b, curr
        return b

# {
 # Driver Code Starts
# Initial Template for Python 3


sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends
