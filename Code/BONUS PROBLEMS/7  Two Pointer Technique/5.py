class Solution:
    def exactlyK(self, arr, k):
        def atMostK(k):
            count = {}
            left = 0
            result = 0
            for right in range(len(arr)):
                count[arr[right]] = count.get(arr[right], 0) + 1
                while len(count) > k:
                    count[arr[left]] -= 1
                    if count[arr[left]] == 0:
                        del count[arr[left]]
                    left += 1
                result += right - left + 1
            return result
        return atMostK(k) - atMostK(k - 1)


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.exactlyK(arr, k))
        print("~")

# } Driver Code Ends
