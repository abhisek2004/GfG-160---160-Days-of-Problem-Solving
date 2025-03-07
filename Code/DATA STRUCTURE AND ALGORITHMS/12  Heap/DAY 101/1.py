# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def calculateSpan(self, arr):
        # write code here
        stk = []
        lst = [0]*len(arr)
        for i in range(len(arr)):
            while stk and arr[stk[-1]] <= arr[i]:
                lst[i] += lst[stk[-1]]
                stk.pop()
            lst[i] += 1
            stk.append(i)

        return lst


# {
 # Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends
