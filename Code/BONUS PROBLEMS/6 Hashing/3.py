class Solution:
    def countPairs(self, arr, k):
        # code here
        dic = {}
        c = 0
        for el in arr:
            if (el+k) in dic:
                c += dic[el+k]
            if (el-k) in dic:
                c += dic[el-k]
            dic[el] = dic.get(el, 0)+1
        return c
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairs(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
