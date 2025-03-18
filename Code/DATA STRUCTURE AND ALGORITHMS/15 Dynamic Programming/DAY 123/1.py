import sys


class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False  # Odd sum cannot be split equally

        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always achievable

        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


# {
 # Driver Code Starts

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
