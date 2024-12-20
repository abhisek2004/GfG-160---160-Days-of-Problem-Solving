class Solution:
    def medianOf2(self, a, b):
        c = a+b
        c.sort()
        if len(c) % 2 != 0:
            return c[len(c)//2]
        else:
            aa = c[len(c)//2]+c[(len(c)//2)-1]
            return aa/2


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ob = Solution()

        if len(arr2) == 1 and arr2[0] == 0:
            arr2 = []
        ans = ob.medianOf2(arr1, arr2)
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)
        print("~")
