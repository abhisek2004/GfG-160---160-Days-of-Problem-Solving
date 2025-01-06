class Solution:
    def numOfSubset(self, arr):
        arr.sort()
        count = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + 1:
                count += 1
        return count
# {
 # Driver Code Starts


def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        ob = Solution()
        print(ob.numOfSubset(nums))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
