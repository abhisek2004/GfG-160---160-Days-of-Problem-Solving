class Solution:

    def maxProduct(self, arr):
        # code here

        MAX = 0
        i = 0
        if len(arr) == 1:
            return arr[0]
        while i < len(arr):
            I = i
            NEG = 0
            temp = 1
            while arr[i] != 0:

                if arr[i] < 0:
                    NEG += 1
                temp *= arr[i]
                i += 1
                if i == len(arr):
                    break
            J = i
            if I != J:
                # temp=1
                if NEG % 2 == 0:
                    # for j in range(I,J):
                    #     temp*=arr[j]
                    MAX = max(MAX, temp)
                elif NEG % 2 == 1:
                    t1 = 1
                    t2 = 1
                    # for j in range(I,J):
                    #     temp*=arr[j]
                    for k in range(I, J):
                        if arr[k] > 0:
                            t1 *= arr[k]
                        else:
                            t1 *= arr[k]
                            break
                    for k in range(J-1, I-1, -1):
                        if arr[k] > 0:
                            t2 *= arr[k]
                        else:
                            t2 *= arr[k]
                            break
                    if J-I > 1:
                        MAX = max(MAX, abs(temp//t1), abs(temp//t2), t1, t2)
            i = J+1
        return MAX


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1
