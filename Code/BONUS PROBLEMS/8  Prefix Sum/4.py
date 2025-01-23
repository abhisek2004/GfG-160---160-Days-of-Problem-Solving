# {
# Driver Code Starts
# Initial Template for Python 3
from collections import defaultdict


# } Driver Code Ends

class Solution:
    def subCount(self, arr, k):
        rm = {0: 1}
        ps = 0
        c = 0

        for i in arr:
            ps += i
            r = ps % k

            if r < 0:
                r += k

            if r in rm:
                c += rm[r]

            rm[r] = rm.get(r, 0)+1

        return c


# {
 # Driver Code Starts.

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        print(ob.subCount(arr, d))
        tc -= 1
        print("~")

# } Driver Code Ends
