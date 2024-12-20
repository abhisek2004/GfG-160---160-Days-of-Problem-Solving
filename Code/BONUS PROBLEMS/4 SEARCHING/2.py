class Solution:
    def findMaximum(self, arr):
        res = -1
        if arr[-1] > arr[0] and arr[-1] > arr[-2]:
            return arr[-1]
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return arr[high]


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")
