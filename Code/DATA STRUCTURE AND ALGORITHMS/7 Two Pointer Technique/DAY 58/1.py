import math
import collections


class Solution:
    def maxWater(self, ns):
        left = collections.defaultdict(int)
        for i in range(len(ns)):
            left[i] = max(ns[i], left[i - 1])

        right = collections.defaultdict(int)
        for i in range(len(ns) - 1, -1, -1):
            right[i] = max(ns[i], right[i + 1])

        water = 0
        for i in range(len(ns)):
            water += min(left[i], right[i]) - ns[i]

        return water
# {
 # Driver Code Starts
# Initial template for Python 3


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
