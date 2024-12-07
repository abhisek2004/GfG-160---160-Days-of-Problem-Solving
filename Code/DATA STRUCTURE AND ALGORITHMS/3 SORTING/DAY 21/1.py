class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        # code here
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break
        return h


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")