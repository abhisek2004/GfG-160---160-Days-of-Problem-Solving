import math


class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        buy1, sell1 = float('inf'), 0
        buy2, sell2 = float('inf'), 0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        return sell2

# {
 # Driver Code Starts
# Initial template for Python 3


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
