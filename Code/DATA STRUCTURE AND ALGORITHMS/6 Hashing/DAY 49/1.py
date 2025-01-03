class Solution:
    def subarrayXor(self, arr, k):
        # code here
        mp = {}
        mp[0] = 1
        xr = 0
        cnt = 0
        for i in arr:
            xr ^= i
            if xr ^ k in mp:
                cnt += mp[xr ^ k]

            if xr in mp:
                mp[xr] += 1
            else:
                mp[xr] = 1
        return cnt


# {
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
