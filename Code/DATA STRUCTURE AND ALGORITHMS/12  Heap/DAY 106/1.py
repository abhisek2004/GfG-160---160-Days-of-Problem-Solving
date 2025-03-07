
class Solution:
    def decodedString(self, s):  # <-- Added 'self' as first parameter
        stack = []
        current_string = ''
        current_number = 0

        for c in s:
            if c.isdigit():
                current_number = current_number * 10 + int(c)
            elif c == '[':
                stack.append((current_string, current_number))
                current_string = ''
                current_number = 0
            elif c == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += c

        return current_string

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends
