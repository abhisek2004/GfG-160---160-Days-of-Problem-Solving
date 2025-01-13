import math


class Solution:
       def pairInSortedRotated(self, arr, target):
              s = set()
               for num in arr:

                    # Calculate the complement that added to
                    # num, equals the target
                    complement = target - num

                    # Check if the complement exists in the set
                    if complement in s:
                        return True

                    # Add the current element to the set
                    s.add(num)

                # If no pair is found
                return False
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        target = int(input())
        ob = Solution()
        print("true" if ob.pairInSortedRotated(A, target) else "false")
        print("~")

# } Driver Code Ends
