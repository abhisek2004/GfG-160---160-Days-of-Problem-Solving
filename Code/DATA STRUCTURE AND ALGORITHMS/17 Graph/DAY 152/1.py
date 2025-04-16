# User function template for Python

class Solution:
    def floydWarshall(self, dist):
        # Code here
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist

# {
 # Driver Code Starts
# Initial template for Python


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends
