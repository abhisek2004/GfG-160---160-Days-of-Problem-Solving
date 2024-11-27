class Solution:
    def getLastMoment(self, n, left, right):
        return max(max(left, default=0), n - min(right, default=n))


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1

        # Reading the length of the plank
        n = int(input().strip())

        # Reading positions of ants moving left
        left = [int(x) for x in input().strip().split()]

        # Reading positions of ants moving right
        right = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.getLastMoment(n, left, right)

        print(result)
        print("~")
