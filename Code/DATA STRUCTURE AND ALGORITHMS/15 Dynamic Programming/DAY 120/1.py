class Solution:
    def minCoins(self, coins, sum):
        i = float('inf')
        dp = [i]*(sum+1)
        dp[0] = 0

        for c in coins:
            for j in range(c, sum+1):
                dp[j] = min(dp[j], 1+dp[j-c])
        return dp[sum] if dp[sum] != i else -1
# {
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends
