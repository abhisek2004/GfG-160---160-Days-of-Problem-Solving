
class Solution:
    def lis(self, arr):
        # code here
        dp = [1 for _ in range(len(arr))]
        for ind in range(1, len(arr)):
            for prev in range(0, ind+1):
                pick = 0
                if arr[prev] < arr[ind]:
                    dp[ind] = max(dp[ind], 1+dp[prev])
        return max(dp)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends
