# User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def place(rows, i):
            if i == n:
                yield rows[:]
            else:
                for c1 in range(1, n+1):
                    rows[i] = c1
                    for j in range(0, i):
                        c2 = rows[j]
                        if c1 == c2 or i-c1 == j-c2 or i+c1 == j+c2:
                            break
                    else:
                        yield from place(rows, i+1)

        return [e for e in place([-1]*n, 0)]

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends
