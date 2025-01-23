from typing import List


class Solution:
    def zeroSumSubmat(self, mat):
        r, c = len(mat), len(mat[0])
        ms = 0

        for i in range(r):
            cs = [0]*c

            for j in range(i, r):
                for k in range(c):
                    cs[k] += mat[j][k]

                ps = 0
                pm = {0: -1}

                for k in range(c):
                    ps += cs[k]

                    if ps in pm:
                        w = k-pm[ps]
                        h = j-i+1
                        ms = max(ms, w*h)
                    else:
                        pm[ps] = k

        return ms
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        r = int(input())
        c = int(input())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t = [int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j] = t[j]
        ans = ob.zeroSumSubmat(matrix)
        print(ans)
        print("~")

# } Driver Code Ends
