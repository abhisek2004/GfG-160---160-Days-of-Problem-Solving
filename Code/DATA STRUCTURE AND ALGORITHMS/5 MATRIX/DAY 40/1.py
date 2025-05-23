import sys


class Solution:
    def setMatrixZeroes(self, mat):
        rowlength = len(mat)
        collength = len(mat[0])
        row = [0]*rowlength
        col = [0]*collength
        for i in range(rowlength):
            for j in range(collength):
                if mat[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(rowlength):
            for j in range(collength):
                if row[i] == 1 or col[j] == 1:
                    mat[i][j] = 0
        return mat


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")
