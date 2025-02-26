class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        result = [0] * n
        left = [-1] * n
        right = [n] * n

        s = []

        for i in range(n):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            if s:
                left[i] = s[-1]
            s.append(i)

        s.clear()

        for i in range(n - 1, -1, -1):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            if s:
                right[i] = s[-1]
            s.append(i)

        for i in range(n):
            window_size = right[i] - left[i] - 1
            result[window_size - 1] = max(result[window_size - 1], arr[i])

        for i in range(n - 2, -1, -1):
            result[i] = max(result[i], result[i + 1])

        return result


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends
