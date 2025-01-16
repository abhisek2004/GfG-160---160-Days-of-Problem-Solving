class Solution:
    def maxLen(self, arr):
        # code here
        prefix_sum = {0: -1}
        current_sum = 0
        max_length = 0

        for i in range(len(arr)):
            current_sum += -1 if arr[i] == 0 else 1

            if current_sum in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum])
            else:
                prefix_sum[current_sum] = i

        return max_length
# {
 # Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends
