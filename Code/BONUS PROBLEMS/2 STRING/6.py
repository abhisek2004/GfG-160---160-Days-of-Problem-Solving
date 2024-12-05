class Solution:

    def __init__(self):
        self.one = [
            "", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ",
            "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ",
            "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ",
            "Nineteen "
        ]

        self.ten = [
            "", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ",
            "Seventy ", "Eighty ", "Ninety "
        ]

    def num_to_words(self, n, s):
        if n > 19:
            str_num = self.ten[n // 10] + self.one[n % 10]
        else:
            str_num = self.one[n]
        if n != 0:
            str_num += s
        return str_num

    def convertToWords(self, n):
        if n == 0:
            return "Zero"

        out = ""

        # Handle billions
        out += self.num_to_words(n // 1000000000, "Billion ")

        # Handle hundreds of millions and tens of millions
        out += self.num_to_words((n // 100000000) % 10, "Hundred ")
        if (n // 100000000) % 10 != 0:
            out += self.num_to_words((n // 1000000) % 100, "") + "Million "
        else:
            out += self.num_to_words((n // 1000000) % 100, "Million ")

        # Handle hundred thousands and ten thousands
        out += self.num_to_words((n // 100000) % 10, "Hundred ")
        if (n // 100000) % 10 != 0:
            out += self.num_to_words((n // 1000) % 100, "") + "Thousand "
        else:
            out += self.num_to_words((n // 1000) % 100, "Thousand ")

        # Handle hundreds
        out += self.num_to_words((n // 100) % 10, "Hundred ")

        # Handle tens and ones
        out += self.num_to_words(n % 100, "")

        return out.strip()


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.convertToWords(n)
        print(f'"{ans}"')
        tc -= 1
