# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = -int(str(x)[:0:-1])
            if n < -2 ** 31:
                return 0
            else:
                return n
        else:
            n = int(str(x)[::-1])
            if n > 2 ** 31 - 1:
                return 0
            else:
                return n


if __name__ == '__main__':
    tests = [
        (0, 0),
        (-1, -1),
        (122, 221),
        (-98, -89)
    ]

    solution = Solution()
    for num, reversed_num in tests:
        if solution.reverse(num) == reversed_num:
            print("PASSED")
        else:
            print(f"FAILED for {num}")
