import math


class Solution:
    def maxWater(self, arr):
        maxi = 0
        st, end = 0, len(arr)-1
        while (st < end):
            maxi = max(maxi, (end-st)*min(arr[st], arr[end]))
            if arr[st] < arr[end]:
                st += 1
            else:
                end -= 1
        return (maxi)
# {
 # Driver Code Starts
# Initial template for Python 3


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
