# https://leetcode.com/problems/zigzag-conversion/

import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        col_size = 2 * numRows - 2
        num_cols = math.ceil(len(s) / col_size)
        seq = []

        for i in range(0, len(s), col_size):
            seq.append(s[i])

        for row in range(1, numRows - 1):
            for col in range(num_cols):
                if row + col * col_size < len(s):
                    seq.append(s[row + col * col_size])
                if col_size * (col + 1) - row < len(s):
                    seq.append(s[col_size * (col + 1) - row])

        for i in range(numRows - 1, len(s), col_size):
            seq.append(s[i])

        return ''.join(seq)


if __name__ == '__main__':
    tests = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("POKEMONEMERALDISGOLD", 5, "PMGOEESOKNRILEOADDML"),
        ("SINGLELINE", 1, "SINGLELINE"),
        ("TWOLINES", 2, "TOIEWLNS"),
        ("ABCDEFGHI", 3, "AEIBDFHCG"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3, "AEIMQUYBDFHJLNPRTVXZCGKOSW")
    ]
    solution = Solution()
    for word, num_rows, converted in tests:
        result = solution.convert(word, num_rows)
        if converted == result:
            print("PASSED")
        else:
            print(f"FAILED at {word}, expected {converted} but got {result}")
