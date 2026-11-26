import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import part2_baseline_retype as baseline


def test_contains_duplicate():
    assert baseline.contains_duplicate([1, 2, 3, 1]) is True
    assert baseline.contains_duplicate([1, 2, 3, 4]) is False
    assert baseline.contains_duplicate([]) is False
    assert baseline.contains_duplicate([42]) is False
    assert baseline.contains_duplicate([-1, -1]) is True
    assert baseline.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_two_sum():
    assert sorted(baseline.two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(baseline.two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(baseline.two_sum([3, 3], 6)) == [0, 1]
    assert sorted(baseline.two_sum([-3, 4, 3, 90], 0)) == [0, 2]
    assert sorted(baseline.two_sum([0, 4, 3, 0], 0)) == [0, 3]


def test_valid_parentheses():
    assert baseline.valid_parentheses("()") is True
    assert baseline.valid_parentheses("()[]{}") is True
    assert baseline.valid_parentheses("([{}])") is True
    assert baseline.valid_parentheses("") is True
    assert baseline.valid_parentheses("(]") is False
    assert baseline.valid_parentheses("([)]") is False
    assert baseline.valid_parentheses("(") is False
    assert baseline.valid_parentheses(")") is False
    assert baseline.valid_parentheses("(((") is False
    assert baseline.valid_parentheses("())") is False
