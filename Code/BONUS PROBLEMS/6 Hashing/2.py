class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        indices = {}
        max_dist = 0
        for i, val in enumerate(arr):
            if val in indices:
                max_dist = max(max_dist, i - indices[val])
            else:
                indices[val] = i
        return max_dist


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))
        print("~")
# } Driver Code Ends
