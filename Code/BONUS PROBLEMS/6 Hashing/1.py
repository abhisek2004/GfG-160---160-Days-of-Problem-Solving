class Solution:
    def romanToDecimal(self, s):
        values = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for char in reversed(s):
            curr = values[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
        print("~")

# } Driver Code Ends
