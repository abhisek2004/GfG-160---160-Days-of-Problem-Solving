from collections import defaultdict


class Solution:
    def groupShiftedString(self, arr):
        def get_key(s):
            if len(s) == 1:
                return (0,)
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i])-ord(s[i-1])) % 26
                key.append(diff)
            return tuple(key)

        groups = defaultdict(list)
        for s in arr:
            key = get_key(s)
            groups[key].append(s)
        return list(groups.values())

# {
 # Driver Code Starts


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        sol = Solution()
        result = sol.groupShiftedString(arr)
        for group in result:
            group.sort()
        result.sort(key=lambda x: x[0])
        for group in result:
            print(" ".join(group))
        print("~")

# } Driver Code Ends
