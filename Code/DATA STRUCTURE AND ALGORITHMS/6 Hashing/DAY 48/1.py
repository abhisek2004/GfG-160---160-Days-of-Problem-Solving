import atexit
from collections import deque
import sys
import io


class Solution:
    def countSubarrays(self, arr, k):
        prefix_sum_count = {}
        prefix_sum_count[0] = 1
        prefix_sum = 0
        c = 0
        for i in arr:
            prefix_sum += i
            if prefix_sum - k in prefix_sum_count:
                c = c+prefix_sum_count[prefix_sum-k]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(
                prefix_sum, 0)+1
        return c
# {
 # Driver Code Starts
# Initial Template for Python 3


# Contributed by : Nagendra Jha
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code En
