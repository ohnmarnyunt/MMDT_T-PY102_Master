"""
Lab01.py — Linked List Lab (Auto-graded)

Covers:
- LeetCode 206: Reverse Linked List
- LeetCode 2816: Double a Number Represented as a Linked List

Lab format:
- Node classes are defined separately from LinkedList wrappers.

Student instructions:
- Do NOT change required function names/signatures.
- You MAY add helper functions/methods.
- Use pointer manipulation (don’t solve by converting the whole list to an int or Python list).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, List


# ============================================================
#  Node Definitions 
# ============================================================

@dataclass
class SNode:
    """Singly-linked list node."""
    val: int
    next: Optional["SNode"] = None


# ============================================================
#  LinkedList Wrapper 
# ============================================================

class SinglyLinkedList:
    """Small wrapper for singly Linked List"""
    def __init__(self, head: Optional[SNode] = None):
        self.head = head

    @staticmethod
    def from_list(values: Iterable[int]) -> "SinglyLinkedList":
        head: Optional[SNode] = None
        tail: Optional[SNode] = None
        for x in values:
            node = SNode(int(x))
            if head is None:
                head = tail = node
            else:
                assert tail is not None
                tail.next = node
                tail = node
        return SinglyLinkedList(head)

    def to_list(self) -> List[int]:
        out: List[int] = []
        cur = self.head
        while cur is not None:
            out.append(cur.val)
            cur = cur.next
        return out


# ============================================================
#  REQUIRED FUNCTIONS (Implement these)
# ============================================================

def reverseList(head: Optional[SNode]) -> Optional[SNode]:
    """
    LeetCode 206 — Reverse Linked List
    Reverse a singly linked list and return the new head.
    Time: O(n), Space: O(1)
    """
    # TODO: Implement
    raise NotImplementedError


def doubleIt(head: Optional[SNode]) -> Optional[SNode]:
    """
    LeetCode 2816 — Double a Number Represented as a Linked List

    Digits are stored in forward order (most significant digit first).
    Return the head of a new list (or reuse nodes) representing 2x the number.

    Examples:
      1 -> 8 -> 9   (189)  =>  3 -> 7 -> 8  (378)
      9 -> 9 -> 9   (999)  =>  1 -> 9 -> 9 -> 8  (1998)

    Requirements:
    - Use linked-list operations/pointer logic.
    - Avoid converting the entire list into an integer/string for the core solution.
    """
    # TODO: Implement
    raise NotImplementedError
