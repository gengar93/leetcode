# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        all_brackets = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in all_brackets.keys():
                brackets.append(char)
            else:
                if len(brackets) == 0 or all_brackets[brackets.pop()] != char:
                    return False

        if brackets:  # In python, "if container" means "if container is not empty"
            return False
        else:
            return True


if __name__ == '__main__':
    tests = [
        ("", True),
        ("()", True),
        ("([])", True),
        ("{[}(])", False),
        ("(()", False),
        ("[))", False),
        (")", False),
        ("()}", False)
    ]

    solution = Solution()
    for expr, is_proper in tests:
        result = solution.isValid(expr)
        if result == is_proper:
            print("PASSED")
        else:
            print(f"FAILED at {expr}, expected {is_proper}, but got {result}")
