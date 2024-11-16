# User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        x = list(set(arr))
        if len(x) > 1:
            x.sort()
            return x[-2]
        else:
            return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
