# User function Template for python3
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        # Code here
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for ac in accounts:
            name = ac[0]
            for email in ac[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(ac[1], email)

        unions = defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        result = []
        for root, emails in unions.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result


# {
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())  # Number of emails + name
            nameEmails = input().split()  # Read name + emails
            accounts.append(nameEmails)

        # Calling the accountsMerge function
        ob = Solution()
        res = ob.accountsMerge(accounts)

        # Sorting individual accounts' emails
        for i in range(len(res)):
            res[i].sort()  # Sort emails in each account

        # Sorting the entire result list lexicographically like C++
        res.sort(key=lambda x: tuple(x))

        # Printing the output in the required format
        print('[', end='')
