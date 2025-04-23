class Solution:
    def singleNum(self, arr):
        hist = {}
        for ele in arr:
            hist[ele] = hist.get(ele, 0) + 1
        res = []
        for k, v in hist.items():
            if v == 1:
                res += [k]
        return sorted(res)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
