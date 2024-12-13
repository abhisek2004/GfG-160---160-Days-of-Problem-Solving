class Solution:
    def minIncrements(self, arr):
        arr.sort()  # Sort the array to handle duplicates sequentially
        increments = 0

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                increments += (arr[i - 1] + 1 - arr[i])
                arr[i] = arr[i - 1] + 1

        return increments


if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))
        print("~")
        T -= 1
