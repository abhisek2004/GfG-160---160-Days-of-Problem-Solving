class Solution:
    def kthMissing(self, arr, k):
        # code here.
        n = len(arr)
        index = 0
        i = 1
        while i <= arr[-1] or k > 0:
            if index < n and i == arr[index]:
                index += 1
            else:
                k -= 1
                if k == 0:
                    return i
            i += 1
        return arr[-1] + k


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")
