class Solution:
    def minCostClimbingStairs(self, cost):
        # Write your code here
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[n-1], cost[n-2])


# {
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends
