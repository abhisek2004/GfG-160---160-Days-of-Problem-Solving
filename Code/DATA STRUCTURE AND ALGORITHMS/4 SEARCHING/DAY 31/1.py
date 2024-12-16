class Solution:

    def kthElement(self, a, b, k):
        n, m = len(a), len(b)

        def kth_in_arrays(a, b, k):
            if len(a) > len(b):
                return kth_in_arrays(b, a, k)

            if len(a) == 0:
                return b[k - 1]

            if k == 1:
                return min(a[0], b[0])

            i = min(len(a), k // 2)
            j = min(len(b), k // 2)

            if a[i - 1] > b[j - 1]:
                return kth_in_arrays(a, b[j:], k - j)
            else:
                return kth_in_arrays(a[i:], b, k - i)

        return kth_in_arrays(a, b, k)


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()
