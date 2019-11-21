# Definition for singly-linked list.
from dataclasses import dataclass
from sys import stderr
from typing import List


@dataclass
class ListNode:
    val: int
    next: 'ListNode' = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        current = head
        count = 0
        while current:
            current = current.next
            count += 1

        if k > count or k < 2:
            return head

        rounds = count // k

        # result
        new_head = None
        next_start = head
        last_tail = None
        print(head)
        # reverse each one
        for i in range(rounds):

            current_tail = next_start
            current_head, next_start = self.reverse_n(next_start, k)

            if last_tail:
                last_tail.next = current_head
            last_tail = current_tail

            if not new_head:
                new_head = current_head

        return new_head

    def reverse_n(self, head: ListNode, k: int) -> (ListNode, ListNode):
        current = head
        pre = None
        for _ in range(k):
            current.next, current, pre = pre, current.next, current
        head.next = current
        return pre, current


def build(a: List[int]):
    current = ListNode(a.pop(0))
    head = current
    while a:
        current.next = ListNode(a.pop(0))
        current = current.next
    return head


def show(node: ListNode):
    a = []
    while node:
        a.append(node.val)
        node = node.next


if __name__ == "__main__":
    node = build([1, 2, 3, 4, 5])
    print(Solution().reverseKGroup(node, 2))
