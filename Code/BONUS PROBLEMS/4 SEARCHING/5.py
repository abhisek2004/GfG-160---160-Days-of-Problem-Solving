class Solution:
    def kokoEat(self, arr, k):
        def canEatAll(s):
            hours_needed = 0
            for pile in arr:
                hours_needed += (pile + s - 1) // s
            return hours_needed <= k
        low, high = 1, max(arr)
        result = high
        while low <= high:
            mid = (low + high) // 2
            if canEatAll(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kokoEat(arr, k)
        print(ans)
        tc -= 1
