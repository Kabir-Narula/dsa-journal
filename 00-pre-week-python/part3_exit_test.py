"""
Pre-Week — Stage 3: OFFICIAL PRE-WEEK EXIT TEST (GATE TO WEEK 1)
----------------------------------------------------------------
STRICT RULES (Roadmap Page 16):
1. Set a 30-minute timer.
2. Close ALL notes, videos, and references. No AI, no autocomplete.
3. Pass ALL 4 items to unlock Week 1 (`01-arrays-and-hashing`).
   If you miss 2 or more, take 2 extra days on Python basics before moving on.

Verify your score after your 30-minute timer:
    python -m pytest 00-pre-week-python/tests/test_part3_exit_test.py -v
"""

from __future__ import annotations


# ==============================================================================
# Question 1: Word Frequencies with a Plain Dict
# ==============================================================================
def word_frequencies(text: str) -> dict[str, int]:
    """Count word frequencies in `text` using a PLAIN `dict` (do NOT use collections.Counter).

    Rules:
    - Split on whitespace.
    - Treat words case-insensitively (convert to lowercase).
    - Return {} for empty or whitespace-only strings.

    Example:
        "The cat and the hat" -> {"the": 2, "cat": 1, "and": 1, "hat": 1}
    """
    raise NotImplementedError


# ==============================================================================
# Question 2: Reverse a List In Place Using Two Indices
# ==============================================================================
def reverse_in_place(nums: list) -> None:
    """Reverse `nums` IN PLACE using two indices (`left` and `right`).

    Rules:
    - Mutate `nums` directly and return None.
    - Do NOT call nums.reverse(), reversed(), or slice assignment nums[::-1].

    Example:
        a = [1, 2, 3, 4]
        reverse_in_place(a)  # a is now [4, 3, 2, 1]
    """
    raise NotImplementedError


# ==============================================================================
# Question 3: Build a 3-Node ListNode Chain & Print with a while Loop
# ==============================================================================
class ListNode:
    """Singly linked list node with `val` and `next` attributes."""

    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        raise NotImplementedError


def build_three_node_chain(a: int, b: int, c: int) -> ListNode:
    """Create 3 ListNode objects wired as: a -> b -> c -> None, and return the head."""
    raise NotImplementedError


def print_chain(head: ListNode | None) -> None:
    """Walk from `head` using a `while` loop and print each node's `val` on its own line.

    Example for 10 -> 20 -> 30 -> None:
        10
        20
        30
    """
    raise NotImplementedError


# ==============================================================================
# Question 4: First Non-Repeating Character
# ==============================================================================
def first_non_repeating_char(s: str) -> str | None:
    """Return the first character in `s` that appears exactly once, or None if none exists.

    Rules:
    - Case-sensitive ("a" and "A" are different characters).
    - Return None for an empty string or if every character repeats.

    Examples:
        "leetcode"     -> "l"
        "loveleetcode" -> "v"
        "aabb"         -> None
    """
    raise NotImplementedError
