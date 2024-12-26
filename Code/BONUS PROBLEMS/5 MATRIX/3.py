class Solution:
    def generateMatrix(self, rowSum, colSum):
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix


def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Read first array (row sums)
        row = list(map(int, input().split()))

        # Read second array (column sums)
        col = list(map(int, input().split()))

        # Create copies of the row and col arrays to pass to the Solution
        row_copy = row.copy()
        col_copy = col.copy()

        # Solve using the class
        ob = Solution()
        ans = ob.generateMatrix(row_copy,
                                col_copy)  # Use copies of row and col

        # Validate the result
        n, m = len(ans), len(ans[0]) if ans else 0
        if n != len(row) or m != len(col):
            print("false")
            print("~")
            continue

        # Check row sums
        is_valid = True
        for i in range(n):
            if sum(ans[i]) != row[i]:  # Check against the original row sum
                is_valid = False
                break

        # Check column sums
        if is_valid:
            for j in range(m):
                if sum(ans[i][j] for i in range(
                        n)) != col[j]:  # Check against the original column sum
                    is_valid = False
                    break

        if is_valid:
            print("true")
        else:
            print("false")

        print("~")


if __name__ == "__main__":
    main()
