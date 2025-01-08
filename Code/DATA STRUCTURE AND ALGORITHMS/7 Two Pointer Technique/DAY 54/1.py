class Solution:
    def countTriangles(self, arr):
        if len(arr) < 3:
            return 0
        arr.sort()
        fside = 0
        sside = len(arr) - 2
        tside = len(arr) - 1
        count = 0
        while tside > 1:
            if fside < sside:
                if arr[fside]+arr[sside] > arr[tside]:
                    count = count + (sside - fside)
                    sside = sside - 1
                else:
                    fside = fside + 1
            else:
                tside -= 1
                sside = tside - 1
                fside = 0
        return count
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends
