
import sys
import math


def circularSubarraySum(arr):
    def kadane(nums):
        max_end_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_end_here = max(num, max_end_here + num)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

    def maxSubarraySumCircular(arr):
        max_kadane = kadane(arr)
        total_sum = sum(arr)
        inverted_array = [-x for x in arr]
        max_inverted_kadane = kadane(inverted_array)

        # Handling the case where all numbers are negative
        if max_inverted_kadane == -total_sum:
            return max_kadane

        max_circular = total_sum + max_inverted_kadane
        return max(max_kadane, max_circular)

    return maxSubarraySumCircular(arr)


if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1
