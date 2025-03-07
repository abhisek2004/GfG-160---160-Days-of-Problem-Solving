import atexit
import sys
import io


class Solution:
    def isBalanced(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # Opening bracket
                stack.append(char)
            elif char in bracket_map:  # Closing bracket
                # Mismatch or empty stack
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Pop the matching opening bracket

        return not stack

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
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
