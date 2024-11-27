class Solution:
    def singleDigit(self, n):
        if n == 0:
            return 0
        if n % 9 == 0:
            return 9
        else:
            return n % 9


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.singleDigit(N)
        print(ans)
        print("~")
