import atexit
import sys
import io


class Solution:

    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        # code here
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for k in d:
            if d[k] == 1:
                return k

        return '$'


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonRepeatingChar(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

        print("~")
