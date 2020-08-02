# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabets = "0abcdefghijklmnopqrstuvwxyz"

        if len(s) < 3:
            return ''.join([alphabets[int(pos)] for pos in s])

        chars = []
        i = 0
        while i < len(s) - 2:
            a, b, c = s[i], s[i + 1], s[i + 2]

            if c == "#":
                chars.append(alphabets[int(a + b)])
                i += 3
            else:
                chars.append(alphabets[int(a)])
                i += 1

        if i == len(s) - 1:
            chars.append(alphabets[int(s[i])])
        elif i == len(s) - 2:
            chars.append(alphabets[int(s[i])])
            chars.append(alphabets[int(s[i + 1])])

        return ''.join(chars)


if __name__ == '__main__':
    tests = [
        ("10#11#12", "jkab"),
        ("1326#", "acz")
    ]

    solution = Solution()
    for cipher, plain in tests:
        result = solution.freqAlphabets(cipher)
        if result == plain:
            print("PASSED")
        else:
            print(f"FAILED at {cipher}, expected {plain} but got {result}")
