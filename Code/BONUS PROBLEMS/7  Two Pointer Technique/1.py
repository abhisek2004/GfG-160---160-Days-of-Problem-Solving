class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        for a in range(len(arr) - 2):
            b = a + 1
            c = len(arr) - 1
            while b < c:
                s = arr[a] + arr[b] + arr[c]
                if s == target:
                    return True
                elif s < target:
                    b += 1
                else:
                    c -= 1
        return False


# {
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array
        target = int(input().strip())  # Read the target sum
        ob = Solution()
        print("true"
              if ob.hasTripletSum(arr, target) else "false")  # Output result
        tc -= 1

# } Driver Code Ends
