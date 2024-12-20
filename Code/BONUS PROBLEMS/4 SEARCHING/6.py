class Solution:
    def minDaysBloom(self, m, k, arr):
        if len(arr) < m*k:
            return -1

        def check(x):
            bouquet, flowers = 0, 0

            for i in arr:
                if x >= i:
                    flowers += 1
                    if flowers == k:
                        bouquet += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquet >= m:
                    return True
            return False
        l, u = min(arr), max(arr)
        res = -1
        while l <= u:
            mid = (l+u)//2
            if check(mid):
                res = mid
                u = mid-1
            else:
                l = mid+1
        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        m = int(input())
        k = int(input())
        ob = Solution()
        res = ob.minDaysBloom(m, k, arr)
        print(res)
        print("~")
