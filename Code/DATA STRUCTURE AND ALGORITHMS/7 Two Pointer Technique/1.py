class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        char_set = set()
        start = 0
        max_len = 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_len = max(max_len, end - start + 1)
        return max_len
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
