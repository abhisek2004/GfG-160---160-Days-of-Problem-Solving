class Solution:
    def computeLPSArray(self, pat):
        m = len(pat)
        lps = [0] * m
        length = 0
        i = 1

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
        return lps

    def search(self, pat, txt):
        m = len(pat)
        n = len(txt)
        lps = self.computeLPSArray(pat)
        result = []
        i = 0
        j = 0

        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == m:
                result.append(i - j)
                j = lps[j - 1]

            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()
