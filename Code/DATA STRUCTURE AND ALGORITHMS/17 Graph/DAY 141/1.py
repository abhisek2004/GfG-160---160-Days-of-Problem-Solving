class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # All 8 possible directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        def dfs(i, j):
            visited[i][j] = True
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == 'L' and not visited[ni][nj]:
                        dfs(ni, nj)

        island_count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    island_count += 1

        return island_count


# {
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends
