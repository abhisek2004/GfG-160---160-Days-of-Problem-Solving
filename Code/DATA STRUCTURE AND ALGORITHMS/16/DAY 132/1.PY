# User function Template for python3

import sys
import io
import atexit


class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        n = len(arr)
        a = 0
        arr.sort()
        dep.sort()
        j = 0
        b = 0
        for i in range(n):
            while j < n and dep[j] < arr[i]:
                b -= 1
                j += 1
            b += 1
            a = max(a, b)
        return a


# {
 # Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends
