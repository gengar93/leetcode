# https://leetcode.com/problems/flipping-an-image/

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n // 2):
                A[i][j], A[i][m - j - 1] = abs(A[i][m - j - 1] - 1), abs(A[i][j] - 1)

            if n % 2 == 1:
                A[i][n // 2] = abs(A[i][n // 2] - 1)

        return A
