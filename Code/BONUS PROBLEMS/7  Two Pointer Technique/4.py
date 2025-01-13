class Solution:
    def atMostK(self, arr, k):
        from collections import defaultdict

        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # If distinct elements exceed k, shrink the window
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Add the number of valid subarrays ending at `right`
            count += (right - left + 1)

        return count


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.atMostK(arr, k))
        print("~")

# } Driver Code Ends
