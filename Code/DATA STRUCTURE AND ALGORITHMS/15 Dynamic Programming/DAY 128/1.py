import sys


class Solution:
    def countWays(self, digits):
        # Code here
        if not digits or digits[0] == '0':
            return 0

        n = len(digits)

        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            od = int(digits[i-1])
            td = int(digits[i-2:i])

            if 1 <= od <= 9:
                dp[i] += dp[i-1]

            if 10 <= td <= 26:
                dp[i] += dp[i-2]

        return dp[n]
# {
 # Driver Code Starts
# Initial Template for Python 3

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends
