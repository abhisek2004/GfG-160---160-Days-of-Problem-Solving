class Solution:
    def search(self, arr, key):
        if (arr.count(key) > 0):
            n = arr.index(key)
            return n
        return -1


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")
