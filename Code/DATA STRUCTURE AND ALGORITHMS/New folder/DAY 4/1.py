class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        k = n - 2
        while k >= 0 and arr[k] >= arr[k + 1]:
            k -= 1
        if k == -1:
            arr.reverse()
            return
        l = n - 1
        while arr[l] <= arr[k]:
            l -= 1
        arr[k], arr[l] = arr[l], arr[k]
        arr[k + 1:] = reversed(arr[k + 1:])


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()
