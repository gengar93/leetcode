# https://leetcode.com/problems/palindrome-number/

from math import log


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        rev = 0
        num_digits = int(log(x, 10)) + 1

        for _ in range(num_digits // 2):
            rev = 10 * rev + x % 10
            x = x // 10

        if num_digits % 2 == 1:
            x = x // 10

        return rev == x


if __name__ == '__main__':
    tests = [
        (1, True),
        (33, True),
        (121, True),
        (122, False),
        (-11, False),
        (10, False),
        (111, True)
    ]

    solution = Solution()
    for num, is_palindrome in tests:
        result = solution.isPalindrome(num)
        if result == is_palindrome:
            print("PASSED")
        else:
            print(f"FAILED at {num}, expected {is_palindrome} but got {result}")
