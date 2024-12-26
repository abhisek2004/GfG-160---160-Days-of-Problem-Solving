class Solution:
    def rotateMatrix(self, mat):
        for i in range(len(mat)):
            mat[i] = mat[i][::-1]
            c = 1
        for i in range(len(mat)//2):
            mat[i], mat[i-c] = mat[i-c], mat[i]
            c += 2


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ob.rotateMatrix(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")
