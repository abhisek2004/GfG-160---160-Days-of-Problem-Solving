
class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        # code here
        n1 = len(s1)
        n2 = len(s2)
        n = 0
        if n1 == n2:
            s1 = ''.join(sorted(s1))
            s2 = ''.join(sorted(s2))
            for i in range(n1):
                if s1[i] != s2[i]:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")
