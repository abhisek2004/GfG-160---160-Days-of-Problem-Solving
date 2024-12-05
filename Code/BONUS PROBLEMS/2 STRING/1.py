from typing import List


class Solution:
    def fizzBuzz(self, n: int):
        result = []

        for i in range(1, n + 1):
            current = []

            if i % 3 == 0:
                current.append("Fizz")
            if i % 5 == 0:
                current.append("Buzz")

            if not current:
                current.append(str(i))

            result.append("".join(current))

        return result


class StringArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = input().strip().split()  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.fizzBuzz(n)

        StringArray().Print(res)
        print("~")
