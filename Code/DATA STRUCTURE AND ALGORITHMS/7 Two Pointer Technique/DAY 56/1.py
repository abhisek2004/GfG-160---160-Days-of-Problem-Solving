from collections import defaultdict
import sys


class Solution:
    def countDistinct(self, arr, k):
        di = {}
        for i in range(k):
            if arr[i] in di:
                di[arr[i]] += 1
            else:
                di[arr[i]] = 1
        sol = []
        sol.append(len(di))
        l = len(di)
        for i in range(1, len(arr)-k+1):
            # print(di)
            if di[arr[i-1]] == 1:
                l -= 1
                di.pop(arr[i-1])
            else:
                di[arr[i-1]] -= 1
            if arr[i+k-1] in di:
                di[arr[i+k-1]] += 1
            else:
                l += 1
                di[arr[i+k-1]] = 1
            sol.append(l)
        return sol


# {
 # Driver Code Starts
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends
