import sys


class Solution:
    def articulationPoints(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        ap = [False] * V
        time = 0

        def dfs(u):
            nonlocal time
            children = 0
            disc[u] = low[u] = time
            time += 1

            for v in adj[u]:
                if disc[v] == -1:
                    parent[v] = u
                    children += 1
                    dfs(v)

                    low[u] = min(low[u], low[v])  # FIXED here

                    # If u is root and has more than one child
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    # If u is not root and low value of one of its child is more
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:  # Back edge
                    low[u] = min(low[u], disc[v])

        for i in range(V):  # FIXED here
            if disc[i] == -1:
                dfs(i)

        result = [i for i in range(V) if ap[i]]
        return result if result else [-1]

# {
 # Driver Code Starts


sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends
