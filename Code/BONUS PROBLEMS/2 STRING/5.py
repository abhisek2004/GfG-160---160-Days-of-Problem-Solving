class Solution:
    def longestPrefixSuffix(self, s):
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[-1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str_input = input()
        ob = Solution()
        print(ob.longestPrefixSuffix(str_input))
        print("~")
  # Longest Prefix Suffix
