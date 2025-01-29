# {
# Driver Code Starts
# Initial Template for Python 3


# } Driver Code Ends

class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        def pos_power(b, e):

            if e == 0:
                return 1.0

            half = pos_power(b, e // 2)
            if e % 2 == 0:
                return half * half
            return half * half * b

        if e >= 0:
            return pos_power(b, e)
        return 1.0/pos_power(b, (-1*e))


# {
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends
