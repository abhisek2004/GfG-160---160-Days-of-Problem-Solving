import math


class Solution:
    def floorSqrt(self, n):
        return (int(n**0.5))


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
