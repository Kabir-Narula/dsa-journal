"""
Pre-Week — Stage 1: Core Python Fluency Drills
----------------------------------------------
Rules:
- Solve every function yourself. No AI, no Copilot, no peeking at solutions.
- Verify your work by running:
    python -m pytest 00-pre-week-python/tests/test_part1_python_drills.py -v
"""

from __future__ import annotations


# 1. Exceptions & Conditionals (CS50P Lec 1 & 3)
def safe_divide(a: float, b: float) -> float | None:
    """Return a / b. If b is 0 (ZeroDivisionError), return None."""
    raise NotImplementedError


# 2. List Comprehension + Conditionals (CS50P Lec 2 & Data Structures)
def squares_of_evens(nums: list[int]) -> list[int]:
    """Return a list of squares for all even integers in nums, preserving order.

    Example: [1, 2, 3, 4, -2] -> [4, 16, 4]
    """
    raise NotImplementedError


# 3. Dict Comprehension (Data Structures)
def invert_dict(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values in a dictionary (assume all values are unique).

    Example: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    raise NotImplementedError


# 4. Sets (Data Structures)
def common_unique(a: list[int], b: list[int]) -> list[int]:
    """Return a sorted list of unique integers that appear in BOTH a and b.

    Example: a=[3, 1, 2, 2], b=[2, 4, 3] -> [2, 3]
    """
    raise NotImplementedError


# 5. Strings & Slicing (Fri Nov 27)
def is_palindrome_alnum(s: str) -> bool:
    """Return True if s is a palindrome ignoring case and non-alphanumeric chars.

    Example: "A man, a plan, a canal: Panama" -> True
    """
    raise NotImplementedError


# 6. String Split, Slicing & Join (Fri Nov 27)
def reverse_words(s: str) -> str:
    """Reverse the order of words in s, collapsing extra spaces to a single space.

    Example: "  hello   world  python " -> "python world hello"
    """
    raise NotImplementedError


# 7. Sorting with custom key (Fri Nov 27)
def sort_by_length_then_alpha(words: list[str]) -> list[str]:
    """Return a NEW list sorted by word length ascending, then alphabetically.

    Example: ["pear", "fig", "apple", "bat"] -> ["bat", "fig", "pear", "apple"]
    """
    raise NotImplementedError


# 8. Multi-key Sorting: desc then asc (Fri Nov 27)
def sort_scores(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Return a NEW list of (name, score) tuples sorted by score DESC, then name ASC.

    Example: [("Bob", 90), ("Alice", 90), ("Zoe", 95)]
          -> [("Zoe", 95), ("Alice", 90), ("Bob", 90)]
    """
    raise NotImplementedError


# 9. enumerate() (Fri Nov 27)
def indices_of_target(nums: list[int], target: int) -> list[int]:
    """Return all indices where nums[i] == target using enumerate().

    Example: ([5, 2, 5, 1, 5], 5) -> [0, 2, 4]
    """
    raise NotImplementedError


# 10. zip() (Fri Nov 27)
def pair_sums(a: list[int], b: list[int]) -> list[int]:
    """Return element-wise sums of lists a and b (stops at the shorter list).

    Example: ([1, 2, 3], [10, 20]) -> [11, 22]
    """
    raise NotImplementedError


# 11. OOP: ListNode & Helpers (CS50P Lec 8, Sat Nov 28)
class ListNode:
    """Singly linked list node with attributes `val` (default 0) and `next` (default None)."""

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        raise NotImplementedError


def build_linked_list(values: list[int]) -> ListNode | None:
    """Build a singly linked list from a Python list and return its head (or None if empty)."""
    raise NotImplementedError


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """Traverse a linked list from head and return all node values in a Python list."""
    raise NotImplementedError


# 12. OOP: TreeNode (CS50P Lec 8, Sat Nov 28)
class TreeNode:
    """Binary tree node with attributes `val` (default 0), `left` (default None), `right` (default None)."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        raise NotImplementedError


def build_sample_tree() -> TreeNode:
    """Build and return a 3-node binary tree: root=1, left=2, right=3."""
    raise NotImplementedError
