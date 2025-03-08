class Solution:
    def longestPalindrome(self, s):
        # code here

        k = ""
        maxx = 0

        def solve(l, r):
            nonlocal k, maxx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxx < (r-l+1):
                    maxx = r-l+1
                    k = s[l:r+1]
                l -= 1
                r += 1
            return
        for i in range(len(s)):
            solve(i, i)
            solve(i, i+1)
        return k
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends
