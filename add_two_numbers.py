# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        ll1, ll2 = self, other
        try:
            while ll1 is not None:
                if ll1.val != ll2.val:
                    return False
                ll1 = ll1.next
                ll2 = ll2.next
        except AttributeError:
            return False

        return True

    def __str__(self):
        node = self
        s = str(node.val)
        while node.next is not None:
            node = node.next
            s += " -> " + str(node.val)

        return s




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        val1, val2 = node1.val, node2.val
        ll3 = ListNode((val1 + val2) % 10)
        node3 = ll3
        carry = (val1 + val2) // 10

        while node1.next is not None or node2.next is not None:
            if node1.next is not None:
                node1 = node1.next
                val1 = node1.val
            else:
                val1 = 0

            if node2.next is not None:
                node2 = node2.next
                val2 = node2.val
            else:
                val2 = 0

            node3.next = ListNode((val1 + val2 + carry) % 10)
            node3 = node3.next
            carry = (val1 + val2 + carry) // 10

        if carry != 0:
            node3.next = ListNode(carry, None)

        return ll3


def make_linked_list(nums: List[int]) -> ListNode:
    """
    Takes list of numbers and returns the corresponding linked list
    Assumes nums is not empty
    :param nums: list of numbers
    :return: linked list of numbers
    """
    head = ListNode(nums[0], None)
    node = head
    for num in nums[1:]:
        node.next = ListNode(num, None)
        node = node.next

    return head


if __name__ == '__main__':
    tests = [
        (make_linked_list([2, 4, 3]),
         make_linked_list([5, 6, 4]),
         make_linked_list([7, 0, 8])),

        (make_linked_list([5]), make_linked_list([5]), make_linked_list([0, 1])),

        (make_linked_list([9]), make_linked_list([9, 9]), make_linked_list([8, 0, 1]))
    ]

    solution = Solution()
    for ll1, ll2, ans in tests:
        ans_got = solution.addTwoNumbers(ll1, ll2)
        if ans_got != ans:
            print(f"ERROR: Expected {ans} but got {ans_got}")
        else:
            print("Passed")
