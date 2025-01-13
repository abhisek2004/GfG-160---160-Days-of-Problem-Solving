# {
# Driver Code Starts

# } Driver Code Ends

class Solution:
    def minRemovals(self, arr, k):
        if sum(arr) < k:
            return -1
        s1 = 0
        n = len(arr)
        i = 0
        while i < n and s1 < k:
            s1 += arr[i]
            i += 1
        i -= 1
        j = n-1
        mini = 10**6
        if s1 == k:
            mini = i+1
        while i >= 0:
            s1 -= arr[i]
            i -= 1
            while j > i and s1 < k:
                s1 += arr[j]
                j -= 1
            if s1 == k:
                mini = min(mini, i+n-j)
        return mini if mini != 10**6 else -1


# {
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.minRemovals(arr, k))

        print("~")
# } Driver Code Ends
