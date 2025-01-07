class Solution:
    def sumClosest(self, arr, target):
        # code here
        i = 0
        j = len(arr)-1
        res = []
        closet = float('inf')
        arr.sort()
        while i < j:
            current_sum = arr[i]+arr[j]
            if abs(target-current_sum) < abs(target-closet):
                closet = current_sum
                res = [arr[i], arr[j]]

            if current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1
            else:
                break
        return res
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
