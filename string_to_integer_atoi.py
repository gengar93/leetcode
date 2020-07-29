# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        num = 0
        is_positive = True

        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        if i < len(str) and str[i] == '+':
            i += 1
        elif i < len(str) and str[i] == '-':
            is_positive = False
            i += 1

        while i < len(str) and str[i] in '0123456789':
            num = 10 * num + int(str[i])
            i += 1

        if is_positive:
            if num < 2 ** 31 - 1:
                return num
            else:
                return 2 ** 31 - 1
        else:
            if num < 2 ** 31:
                return -num
            else:
                return -2 ** 31


if __name__ == '__main__':
    tests = [
        ("42", 42),
        ("", 0),
        ("-", 0),
        ("-42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("91283472332", 2147483647)
    ]

    solution = Solution()
    for num_str, num_int in tests:
        result = solution.myAtoi(num_str)
        if result == num_int:
            print("PASSED")
        else:
            print(f"FAILED at {num_str}, expected {num_int} but got {num_str}")