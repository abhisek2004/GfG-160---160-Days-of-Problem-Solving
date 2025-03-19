from collections import deque


class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        if k >= n//2:
            profit = 0
            for i in range(1, n):
                if arr[i] > arr[i-1]:
                    profit += arr[i]-arr[i-1]
            return profit
        else:
            prev_dp = [0]*n
            for i in range(1, k+1):
                cur_dp = [0]*n
                maxi = -arr[0]
                for i in range(1, n):
                    cur_dp[i] = max(cur_dp[i-1], arr[i]+maxi)
                    maxi = max(maxi, prev_dp[i]-arr[i])
                prev_dp = cur_dp.copy()
            return prev_dp[-1]


# {
 # Driver Code Starts

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends
