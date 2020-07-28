# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        col_size = 2 * numRows - 2
        seq = []

        for i in range(0, len(s), col_size):
            seq.append(s[i])

        for i in range(1, numRows - 1):
            for j in range(i, len(s), col_size):
                seq.append(s[j])
                if j + col_size - 2 * i < len(s):
                    seq.append(s[j + col_size - 2 * i])

        for i in range(numRows - 1, len(s), col_size):
            seq.append(s[i])

        return ''.join(seq)


if __name__ == '__main__':
    tests = [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("POKEMONEMERALDISGOLD", 5, "PMGOEESOKNRILEOADDML"),
        ("SINGLELINE", 1, "SINGLELINE"),
        ("SINGLECOLUMN", 20, "SINGLECOLUMN"),
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
