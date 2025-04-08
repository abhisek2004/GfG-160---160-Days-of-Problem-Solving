import sys


class Solution:
    def isBridge(self, V, edges, c, d):
        # code here
        adj = {i: [] for i in range(V)}
        for u, v in edges:
            if (u == c and v == d) or (u == d and v == c):
                pass
            else:
                adj[u].append(v)
                adj[v].append(u)

        visited = [False for _ in range(V)]

        def dfs(node, target):
            if node == target:
                return True
            elif not visited[node]:
                visited[node] = True
                flag = False
                for nxt in adj[node]:
                    flag = flag or dfs(nxt, target)
                return flag
            else:
                return False

        return not dfs(c, d)


# {
 # Driver Code Starts

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
