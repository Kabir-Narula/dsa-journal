import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import part1_python_drills as drills


def test_safe_divide():
    assert drills.safe_divide(10, 2) == 5.0
    assert drills.safe_divide(7, 2) == 3.5
    assert drills.safe_divide(5, 0) is None
    assert drills.safe_divide(0, 5) == 0.0


def test_squares_of_evens():
    assert drills.squares_of_evens([1, 2, 3, 4, -2, 0]) == [4, 16, 4, 0]
    assert drills.squares_of_evens([1, 3, 5]) == []
    assert drills.squares_of_evens([]) == []


def test_invert_dict():
    assert drills.invert_dict({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
    assert drills.invert_dict({}) == {}


def test_common_unique():
    assert drills.common_unique([3, 1, 2, 2], [2, 4, 3, 3]) == [2, 3]
    assert drills.common_unique([1, 2], [3, 4]) == []
    assert drills.common_unique([], [1, 2]) == []


def test_is_palindrome_alnum():
    assert drills.is_palindrome_alnum("A man, a plan, a canal: Panama") is True
    assert drills.is_palindrome_alnum("race a car") is False
    assert drills.is_palindrome_alnum("") is True
    assert drills.is_palindrome_alnum("0P") is False


def test_reverse_words():
    assert drills.reverse_words("  hello   world  python ") == "python world hello"
    assert drills.reverse_words("single") == "single"
    assert drills.reverse_words("   ") == ""


def test_sort_by_length_then_alpha():
    words = ["pear", "fig", "apple", "bat"]
    result = drills.sort_by_length_then_alpha(words)
    assert result == ["bat", "fig", "pear", "apple"]
    assert words == ["pear", "fig", "apple", "bat"], "Should return a NEW list, not mutate input"


def test_sort_scores():
    records = [("Bob", 90), ("Alice", 90), ("Zoe", 95), ("Charlie", 80)]
    result = drills.sort_scores(records)
    assert result == [("Zoe", 95), ("Alice", 90), ("Bob", 90), ("Charlie", 80)]
    assert records[0] == ("Bob", 90), "Should return a NEW list, not mutate input"


def test_indices_of_target():
    assert drills.indices_of_target([5, 2, 5, 1, 5], 5) == [0, 2, 4]
    assert drills.indices_of_target([1, 2, 3], 9) == []
    assert drills.indices_of_target([], 0) == []


def test_pair_sums():
    assert drills.pair_sums([1, 2, 3], [10, 20]) == [11, 22]
    assert drills.pair_sums([1, 2], [3, 4]) == [4, 6]
    assert drills.pair_sums([], [1, 2]) == []


def test_list_node_and_helpers():
    node = drills.ListNode()
    assert node.val == 0 and node.next is None

    head = drills.build_linked_list([10, 20, 30])
    assert isinstance(head, drills.ListNode)
    assert head.val == 10
    assert head.next.val == 20
    assert head.next.next.val == 30
    assert head.next.next.next is None

    assert drills.linked_list_to_list(head) == [10, 20, 30]
    assert drills.build_linked_list([]) is None
    assert drills.linked_list_to_list(None) == []


def test_tree_node_and_sample_tree():
    default_node = drills.TreeNode()
    assert default_node.val == 0 and default_node.left is None and default_node.right is None

    root = drills.build_sample_tree()
    assert isinstance(root, drills.TreeNode)
    assert root.val == 1
    assert root.left.val == 2 and root.left.left is None and root.left.right is None
    assert root.right.val == 3 and root.right.left is None and root.right.right is None
