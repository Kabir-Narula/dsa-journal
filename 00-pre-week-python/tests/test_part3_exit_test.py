import ast
import inspect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import part3_exit_test as exit_test


def _function_code_without_docstring(func) -> str:
    source = inspect.getsource(func)
    tree = ast.parse(source)
    fn_node = tree.body[0]
    if (
        isinstance(fn_node, ast.FunctionDef)
        and fn_node.body
        and isinstance(fn_node.body[0], ast.Expr)
        and isinstance(fn_node.body[0].value, ast.Constant)
        and isinstance(fn_node.body[0].value.value, str)
    ):
        fn_node.body = fn_node.body[1:]
    return ast.unparse(fn_node)


def test_q1_word_frequencies():
    code = _function_code_without_docstring(exit_test.word_frequencies)
    assert "Counter" not in code, "Use a plain dict instead of collections.Counter"

    res = exit_test.word_frequencies("The cat and the hat")
    assert type(res) is dict, "Must return a plain dict, not collections.Counter"
    assert res == {"the": 2, "cat": 1, "and": 1, "hat": 1}

    assert exit_test.word_frequencies("  Python   python PYTHON  ") == {"python": 3}
    assert exit_test.word_frequencies("") == {}
    assert exit_test.word_frequencies("    ") == {}
    assert exit_test.word_frequencies("one") == {"one": 1}


def test_q2_reverse_in_place():
    code = _function_code_without_docstring(exit_test.reverse_in_place)
    assert ".reverse(" not in code, "Use two indices instead of list.reverse()"
    assert "reversed(" not in code, "Use two indices instead of reversed()"
    assert "[::-1]" not in code, "Use two indices instead of slicing [::-1]"

    a = [1, 2, 3, 4]
    ref = a
    ret = exit_test.reverse_in_place(a)
    assert ret is None, "reverse_in_place should mutate the list and return None"
    assert a is ref, "Must mutate the original list object in place"
    assert a == [4, 3, 2, 1]

    odd = [10, 20, 30, 40, 50]
    exit_test.reverse_in_place(odd)
    assert odd == [50, 40, 30, 20, 10]

    single = [99]
    exit_test.reverse_in_place(single)
    assert single == [99]

    empty = []
    exit_test.reverse_in_place(empty)
    assert empty == []


def test_q3_three_node_chain_and_print(capsys):
    head = exit_test.build_three_node_chain(10, 20, 30)
    assert isinstance(head, exit_test.ListNode)
    assert head.val == 10
    assert head.next is not None and head.next.val == 20
    assert head.next.next is not None and head.next.next.val == 30
    assert head.next.next.next is None

    exit_test.print_chain(head)
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["10", "20", "30"]

    exit_test.print_chain(None)
    captured_empty = capsys.readouterr()
    assert captured_empty.out == ""


def test_q4_first_non_repeating_char():
    assert exit_test.first_non_repeating_char("leetcode") == "l"
    assert exit_test.first_non_repeating_char("loveleetcode") == "v"
    assert exit_test.first_non_repeating_char("aabb") is None
    assert exit_test.first_non_repeating_char("") is None
    assert exit_test.first_non_repeating_char("z") == "z"
    assert exit_test.first_non_repeating_char("aAbBc") == "a"
    assert exit_test.first_non_repeating_char("aabbccd") == "d"
