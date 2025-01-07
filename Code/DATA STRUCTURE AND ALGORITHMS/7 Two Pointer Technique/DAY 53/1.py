class Solution:
    def countPairs(self, arr, target):
        i = 0
        j = len(arr)-1
        ans = 0
        while i < j:
            sm = arr[i] + arr[j]
            if sm == target:
                if (arr[i] == arr[j]):
                    temp = j-i
                    ans += ((temp*(temp+1))//2)
                    j = i
                else:
                    left = 1
                    right = 1
                    while (i < j and arr[i] == arr[i+1]):
                        left += 1
                        i += 1
                    while (i < j and arr[j] == arr[j-1]):
                        right += 1
                        j -= 1

                    ans += (left*right)
                    i += 1
                    j -= 1
            elif sm < target:
                i += 1
            else:
                j -= 1
        return ans
# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
