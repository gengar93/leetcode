from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda item: item[1])
        i, j = 0, len(nums) - 1
        while i < j:
            (idx1, val1), (idx2, val2) = sorted_nums[i], sorted_nums[j]
            if val1 + val2 < target:
                i += 1
            elif val1 + val2 > target:
                j -= 1
            else:
                return [idx1, idx2]

        raise ValueError("Bad input")


if __name__ == '__main__':
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([2, 7, 11, 15], 22, [1, 3]),
        ([4, 2, 0, -4, 1], -4, [2, 3])
    ]
    solution = Solution()

    for ns, t, ans in tests:
        ans_got = solution.twoSum(ns, t)
        if (ans != ans_got) and (ans != ans_got[::-1]):
            print(f"Test failed with input {(ns, t)}")
            print(f"Expected {ans}, but got {ans_got}")
