class Solution:
    def productExceptSelf(self, arr):
        # code here
        pref = 1
        res = []
        for i in range(len(arr)):
            res.append(pref)
            pref *= arr[i]
        suff = 1
        for i in range(len(arr)-1, -1, -1):
            res[i] *= suff
            suff *= arr[i]
        return res
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
