class Solution:
    def closest3Sum(self, arr, target):
        low_dif = float("inf")
        max_target = float("-inf")
        size = len(arr)
        arr.sort()
        for i, num in enumerate(arr):
            l, r = i+1, size-1
            while l < r:
                s = num + arr[l] + arr[r]
                abs_val = abs(target-s)
                if low_dif > abs_val:
                    low_dif = abs_val
                    max_target = s
                elif low_dif == abs_val:
                    max_target = max(max_target, s)
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return max_target
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        print(ob.closest3Sum(arr, target))
        print("~")

# } Driver Code Ends
