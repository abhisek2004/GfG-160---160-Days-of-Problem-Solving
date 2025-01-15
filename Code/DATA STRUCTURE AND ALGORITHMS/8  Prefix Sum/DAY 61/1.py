class Solution:
    def longestSubarray(self, arr, k):
        # code here
        l = 0
        d = {}
        s = 0

        for i in range(len(arr)):
            s += arr[i]
            if s == k:
                l = max(i+1, l)
            if s-k in d:
                l = max(l, i-d[s-k])
            if s not in d:
                d[s] = i
        return l
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
