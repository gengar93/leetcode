# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        i, j = 0, -1
        best_i, best_j = i, j
        for j, char in enumerate(s):
            if char in chars and chars[char] >= i:
                if j - 1 - i > best_j - best_i:
                    best_i, best_j = i, j - 1
                i = chars[char] + 1
                chars[char] = j
            else:
                chars[char] = j

        if j - i > best_j - best_i:
            best_i, best_j = i, j

        return best_j - best_i + 1


if __name__ == '__main__':
    tests = [
        ("", 0),
        ("xyzzy", 3),
        ("x", 1),
        ("abcdefg", 7),
        ("abcabcd", 4),
        ("ababcabcda", 4)
    ]

    solution = Solution()
    for word, ans in tests:
        ans_got = solution.lengthOfLongestSubstring(word)
        if ans != ans_got:
            print(f"FAILED: For {word}, expected {ans} but got {ans_got}")
        else:
            print("PASSED")
