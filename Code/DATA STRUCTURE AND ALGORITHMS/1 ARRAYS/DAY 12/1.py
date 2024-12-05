import math


class Solution:

    def missingNumber(self, arr):
        for i in range(len(arr)):
            if arr[i] <= 0 or arr[i] > len(arr):
                arr[i] = len(arr)+1
        # print(arr)

        for i in range(len(arr)):
            if abs(arr[i]) > len(arr):
                continue
            idx = abs(arr[i])-1
            # print(idx)
            if arr[idx] > 0:
                arr[idx] *= -1
        # print(arr)
        for i in range(len(arr)):
            if arr[i] > 0:
                return i+1
        return len(arr)+1


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()
