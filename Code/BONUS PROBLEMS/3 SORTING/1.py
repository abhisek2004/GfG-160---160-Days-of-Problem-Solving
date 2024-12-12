class Solution:
    def minSum(self, arr):
        n1, n2 = "", ""

        arr.sort()

        for i in range(len(arr)):
            if i % 2 == 0:
                n1 += str(arr[i])
            else:
                n2 += str(arr[i])

        n1 = n1[::-1]
        n2 = n2[::-1]

        ans = ""
        i, j, carry = 0, 0, 0

        while i < len(n1) or j < len(n2):
            sum_ = carry
            if i < len(n1):
                sum_ += int(n1[i])
                i += 1
            if j < len(n2):
                sum_ += int(n2[j])
                j += 1

            carry = sum_ // 10
            ans += str(sum_ % 10)

        if carry:
            ans += str(carry)

        ans = ans.rstrip('0')

        return ans[::-1]


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")
