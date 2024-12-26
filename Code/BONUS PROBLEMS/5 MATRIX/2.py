class Solution:
    def spiralFill(self, n, m, arr):
        res = [[0 for _ in range(m)] for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, m - 1
        index = 0
        while index < len(arr):
            for j in range(left, right + 1):
                if index < len(arr):
                    res[top][j] = arr[index]
                    index += 1
            top += 1
            for i in range(top, bottom + 1):
                if index < len(arr):
                    res[i][right] = arr[index]
                    index += 1
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if index < len(arr):
                        res[bottom][j] = arr[index]
                        index += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if index < len(arr):
                        res[i][left] = arr[index]
                        index += 1
                left += 1
        return res


class Array:

    @staticmethod
    def input(A, n):
        A[:] = list(map(int, input().split()))

    @staticmethod
    def print(A):
        print(" ".join(map(str, A)))


class Matrix:

    @staticmethod
    def input(A, n, m):
        for i in range(n):
            A.append(list(map(int, input().split())))

    @staticmethod
    def print(A):
        for row in A:
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        arr = [0] * (n * m)
        Array.input(arr, n * m)

        obj = Solution()
        res = obj.spiralFill(n, m, arr)

        Matrix.print(res)
        print("~")
