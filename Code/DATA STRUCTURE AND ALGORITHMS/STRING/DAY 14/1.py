class Solution:
    def addBinary(self, s1, s2):
        # code here
        s1 = s1.lstrip("0")
        s2 = s2.lstrip("0")
#         print(s1,s2)
        s3 = ""
        carry = 0
        n = len(s1)-1
        m = len(s2)-1
        while n >= 0 and m >= 0:
            f1 = s1[n]
            f2 = s2[m]
          #  print("++",s3," + ",f1," + ",f2," + ",carry)

            if f1 == '0' and f2 == '0' and carry == 0:
                s3 += '0'
                carry = 0

            elif f1 == '0' and f2 == '0' and carry == 1:
                s3 += '1'
                carry = 0

            elif f1 == '0' and f2 == '1' and carry == 0:
                s3 += "1"
                carry = 0

            elif f1 == '0' and f2 == '1' and carry == 1:
                s3 += '0'
                carry = 1

            elif f1 == '1' and f2 == '1' and carry == 1:
                s3 += '1'
                carry = 1

            elif f1 == '1' and f2 == '0' and carry == 1:
                s3 += '0'
                carry = 1

            elif f1 == '1' and f2 == '0' and carry == 0:
                carry = 0
                s3 += '1'

            elif f1 == '1' and f2 == '1' and carry == 0:
                s3 += '0'
                carry = 1
          #  print("--",s3," + ",f1," + ",f2," + ",carry)

            n -= 1
            m -= 1
#         print(s3)
        while m >= 0:
            if s2[m] == '0' and carry == 1:
                carry = 0
                s3 += '1'
            elif s2[m] == '0' and carry == 0:
                s3 += '0'
            elif s2[m] == '1' and carry == 0:
                s3 += '1'
            elif s2[m] == '1' and carry == 1:
                s3 += '0'
                carry = 1
            m -= 1
       # print(s3)
        while n >= 0:
            if s1[n] == '0' and carry == 1:
                carry = 0
                s3 += '1'
            elif s1[n] == '0' and carry == 0:
                carry = 0
                s3 += '0'
            elif s1[n] == '1' and carry == 0:
                carry = 0
                s3 += '1'
            elif s1[n] == '1' and carry == 1:
                s3 += '0'
                carry = 1
            n -= 1
#         print(s3)
        if carry == 1:
            s3 += '1'

        s4 = ""
        for i in range(len(s3)-1, -1, -1):
            s4 += s3[i]
        return s4


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")
