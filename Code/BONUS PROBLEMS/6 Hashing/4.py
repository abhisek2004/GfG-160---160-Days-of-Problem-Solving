from collections import defaultdict


class Solution:
    def countSum(self, arr, target):
        # code her
        count = 0
        n = len(arr)
        pair = {}
        for i in range(n):
            for j in range(i+1, n):
                curr = arr[i]+arr[j]
                com = target-curr
                if com in pair:
                    count += pair[com]
            for j in range(i):
                curr = arr[i]+arr[j]
                if curr in pair:
                    pair[curr] += 1
                else:
                    pair[curr] = 1
        return count


# {
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        target = int(input())
        obj = Solution()
        print(obj.countSum(arr, target))
        print("~")

# } Driver Code Ends
