class Solution:

    def countPS(self, s):
        # code here
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 2:  # Only consider substrings of length ≥ 2
                    count += 1
                left -= 1
                right += 1
            return count

        total_count = 0
        for i in range(len(s)):
            # Odd-length palindromes
            total_count += expand_around_center(i, i)
            # Even-length palindromes
            total_count += expand_around_center(i, i + 1)

        return total_count

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends
