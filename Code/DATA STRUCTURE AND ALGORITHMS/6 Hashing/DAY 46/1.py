import atexit
import sys
import io


class Solution:

    # arr[] : the input array

    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        myset = (set)()
        mx = 1
        cur = 1
        for i in arr:
            myset.add(i)
        for i in arr:
            if ((i-1) in myset):
                continue
            else:
                cur = 1
                while ((i+1) in myset):
                    cur = cur+1
                    i = i+1
                mx = max(mx, cur)
        return mx
# {
 # Driver Code Starts
# Initial Template for Python 3


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends
