class Solution:
    def findMinOperation(self, mat):
        n = len(mat)
        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        target_sum = max(max(row_sums), max(col_sums))
        operations = 0
        for i in range(n):
            for j in range(n):
                required_increase = target_sum - row_sums[i]
                row_sums[i] += required_increase
                operations += required_increase
        return operations


t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    sol = Solution()
    print(sol.findMinOperation(matrix))
    print("~")
