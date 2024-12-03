class Solution:
    def minChar(self, s):
        def computelps(pat, lps):
            m = len(pat)
            i = 1
            length = 0
            lps[0] = 0

            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

        s1 = s + "#" + s[::-1]
        lps = [0] * len(s1)
        computelps(s1, lps)
        return len(s) - lps[-1]


if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")
