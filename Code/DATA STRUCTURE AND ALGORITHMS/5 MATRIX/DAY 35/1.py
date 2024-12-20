class Solution:
    def spirallyTraverse(self, matrix):
        if not matrix:
            return []
        result = []
        top, bottom = 0, len(matrix)-1
        left, rigth = 0, len(matrix[0])-1

        while top <= bottom and left <= rigth:
            for i in range(left, rigth+1):
                result.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                result.append(matrix[i][rigth])
            rigth -= 1
            if top <= bottom:
                for i in range(rigth, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= rigth:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")
