class Solution:
    def isSubsetSum(self, arr, target_sum):
        n = len(arr)
        dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

        # Base Case: A sum of 0 is always possible with an empty subset
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] > j:  # Cannot include current element
                    dp[i][j] = dp[i - 1][j]
                else:  # Either include or exclude the current element
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        return dp[n][target_sum]  # Correct return statement

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
