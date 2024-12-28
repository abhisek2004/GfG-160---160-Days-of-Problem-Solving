# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
class Solution:
    def findTriplets(self, arr):
        res_set = set()
        n = len(arr)
        mp = {}
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in mp:
                    mp[pair_sum] = []
                mp[pair_sum].append((i, j))

        for i in range(n):
            rem = -arr[i]
            if rem in mp:
                pairs = mp[rem]
                for p in pairs:
                    if p[0] != i and p[1] != i:
                        curr = tuple(sorted([i, p[0], p[1]]))
                        res_set.add(curr)
        return [list(triplet) for triplet in res_set]

# {
 # Driver Code Starts.


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
