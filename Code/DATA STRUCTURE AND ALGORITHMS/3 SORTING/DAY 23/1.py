class Solution:
    def mergeOverlap(self, arr):
        # Code here
        arr.sort(key=lambda x: x[0])
        res = []
        res.append([arr[0][0], arr[0][1]])
        for i in range(1, len(arr)):
            u1, v1 = res[-1][0], res[-1][1]
            u2, v2 = arr[i][0], arr[i][1]
            if v1 >= u2:
                res[-1][1] = max(v1, v2)
            else:
                res.append([u2, v2])
        return res


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()
