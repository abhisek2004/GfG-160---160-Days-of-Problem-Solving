class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for the 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Skip leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for the sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            sign = 1
            i += 1
        else:
            sign = 1  # Default is positive if no sign is found

        # Step 3: Convert the digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Apply the sign
        num *= sign

        # Step 4: Handle overflow and return the result
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")
