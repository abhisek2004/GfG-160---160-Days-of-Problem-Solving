class Solution:
    def subarraySum(self, arr, target):
        l = 0
        su = 0
        for i in range(len(arr)):
            su += arr[i]
            while su > target and l < i:
                su -= arr[l]
                l += 1
            if su == target:
                return [l+1, i+1]
        return [-1]
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
