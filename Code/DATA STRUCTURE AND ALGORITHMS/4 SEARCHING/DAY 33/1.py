import bisect


class Solution:
    def is_possible(self, arr, n, k, curr_min):
        students_required = 1
        curr_sum = 0
        for i in range(n):
            if arr[i] > curr_min:
                return False
            if curr_sum + arr[i] > curr_min:
                students_required += 1
                curr_sum = arr[i]
                if students_required > k:
                    return False
            else:
                curr_sum += arr[i]
        return True

    def findPages(self, arr, k):
        n = len(arr)
        sum_of_pages = sum(arr)
        if n < k:
            return -1
        start, end = 0, sum_of_pages
        result = float('inf')
        while start <= end:
            mid = (start + end) // 2
            if self.is_possible(arr, n, k, mid):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1
        return result


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")
