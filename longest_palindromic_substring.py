# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palin_pos = (0, 1)
        current_len = 1

        for i in range(1, len(s)):
            if current_len == 1:
                if s[i] == s[i - 1]:
                    current_len = 2
                elif i > 1 and s[i] == s[i - 2]:
                    current_len = 3
            elif i > current_len and s[i] == s[i - current_len - 1]:
                current_len += 2
            else:
                if current_len > longest_palin_pos[1] - longest_palin_pos[0]:
                    longest_palin_pos = (i - current_len, i)
                current_len = 1

        if current_len > (longest_palin_pos[1] - longest_palin_pos[0]):
            longest_palin_pos = (len(s) - current_len, len(s))

        i, j = longest_palin_pos
        return s[i: j]


if __name__ == '__main__':
    tests = [
        ("a", "a"),
        ("abba", "abba"),
        ("xabba", "abba"),
        ("cabbage", "abba"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("aaaa", "aaaa"),
        ("aaa", "aaa")
    ]

    solution = Solution()
    for word, largest_palin in tests:
        result = solution.longestPalindrome(word)
        if result == largest_palin:
            print("PASSED")
        else:
            print(f"FAILED at {word}, expected {largest_palin} but got {result}")