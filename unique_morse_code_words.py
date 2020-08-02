# https://leetcode.com/problems/unique-morse-code-words/
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alpha_to_morse = {m: a for m, a in zip(alphabets, morse)}

        unique_morse = set()
        for word in words:
            unique_morse.add(''.join([alpha_to_morse[c] for c in word]))

        return len(unique_morse)