class Solution:

    def camelCase(self, arr, pat):
        res = []
        for word in arr:
            j = 0
            for i in range(len(word)):
                if word[i].isupper():
                    if j < len(pat) and word[i] == pat[j]:
                        j += 1
                    elif j < len(pat):
                        break
            if j == len(pat):
                res.append(word)
        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(str, input().split()))
        pat = input()
        ob = Solution()
        ans = ob.camelCase(arr, pat)
        ans.sort()
        if not ans:  # Check if ans is empty
            print("[]")
        else:
            for i in ans:
                print(i, end=" ")
            print()
