# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            n, m = nums[0], nums[1]
        else:
            n, m = nums[1], nums[0]

        for k in nums[2:]:
            if k > m:
                if k > n:
                    m = n
                    n = k
                else:
                    m = k

        return (n - 1) * (m - 1)



