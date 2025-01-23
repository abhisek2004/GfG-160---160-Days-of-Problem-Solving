class Solution:
    def touchedXaxis(self, arr):
        # code here
        position = 0
        count = 0
        for value in arr:
            prev_position = position
            position += value

            if (prev_position > 0 and position <= 0) or (prev_position < 0 and position >= 0):
                count += 1

        return count
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.touchedXaxis(arr)
        print(ans)
        print("~")

# } Driver Code Ends
