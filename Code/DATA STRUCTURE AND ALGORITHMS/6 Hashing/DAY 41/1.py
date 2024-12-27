# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
from collections import defaultdict


class Solution:
    def countPairs(self, arr, target):
        ans = 0
        mm = defaultdict(int)
        for x in arr:
            if target - x in mm:
                ans += mm[target - x]
            mm[x] += 1
        return ans

# {
 # Driver Code Starts.


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
