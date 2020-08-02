# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest = min(strs)
        largest = max(strs)

        common_chars = []
        for i in range(min(len(smallest), len(largest))):
            if smallest[i] == largest[i]:
                common_chars.append(smallest[i])
            else:
                break

        return ''.join(common_chars)


if __name__ == '__main__':
    tests = [
        ([], ""),
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["", ""], ""),
        (["a", "aa", "aaa"], "a")
    ]
    solution = Solution()
    for words, common_longest in tests:
        result = solution.longestCommonPrefix(words)
        if result == common_longest:
            print("PASSED")
        else:
            print(f"FAILED at {words}, expected {common_longest} but got {result}")
