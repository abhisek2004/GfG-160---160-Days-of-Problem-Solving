import functools


class Solution:
    def findLargest(self, arr):
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
        arr = list(map(str, arr))
        arr.sort(key=functools.cmp_to_key(compare))
        result = ''.join(arr)
        return '0' if result[0] == '0' else result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findLargest(arr)
        print(ans)
        print("~")
