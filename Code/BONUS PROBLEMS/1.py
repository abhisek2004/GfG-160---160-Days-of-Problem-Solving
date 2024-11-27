class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]
        target_sum = total_sum // 3
        n = len(arr)
        current_sum = 0
        first_index = -1
        second_index = -1
        for i in range(n):
            current_sum += arr[i]
            if current_sum == target_sum and first_index == -1:
                first_index = i
            elif current_sum == 2 * target_sum and first_index != -1:
                second_index = i
                break
        if current_sum == 2 * target_sum and second_index != -1:
            return [first_index, second_index]
        return [-1, -1]


if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")

        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")
