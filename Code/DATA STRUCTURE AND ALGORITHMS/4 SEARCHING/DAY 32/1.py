import bisect


class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        low, high = 1, stalls[-1] - stalls[0]
        result = 0
        while low <= high:
            mid = (low + high) // 2
            cows_placed = 1
            last_stall = stalls[0]
            for stall in stalls[1:]:
                if stall - last_stall >= mid:
                    cows_placed += 1
                    last_stall = stall
                    if cows_placed == k:
                        break
            if cows_placed >= k:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
