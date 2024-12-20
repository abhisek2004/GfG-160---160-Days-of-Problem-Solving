import bisect


class Solution:
    def lowerBound(self, arr, target):
        for i in range(len(arr)):
            if arr[i] >= target:
                return i
        return len(arr)


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.lowerBound(A, D)
        print(ans)
        print("~")
