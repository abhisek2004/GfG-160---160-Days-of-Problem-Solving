# User function Template for python3

import sys
import io
import atexit


class Solution:
    def bellmanFord(self, V, edges, src):
        dis = [float('inf')]*V
        dis[src] = 0
        for _ in range(V-1):
            for sta, sto, cos in edges:
                dis[sto] = min(dis[sto], dis[sta]+cos)
        for sta, sto, cos in edges:
            if dis[sto] > dis[sta]+cos:
                return [-1]
        return [x if x != float('inf') else 10**8 for x in dis]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
