class Solution:
    def sentencePalindrome(self, s):
        sen = ""
        for i in s:
            if i.isalpha():
                sen += i.lower()
            elif i.isdigit():
                sen += i
        return sen == sen[::-1]
        # your code here


if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        s = input()
        ob = Solution()
        if ob.sentencePalindrome(s):
            print("true")
        else:
            print("false")
