import pytest

from hacker_functions.fn_02_medium import (
    capitalize_first,
    categorize_grade,
    count_matches,
    find_in_list,
    find_middle,
    is_palindrome,
    max_number,
    strings_are_equal,
    sum_evens,
)


def test_categorize_grade_1() -> None:
    assert categorize_grade(60) == "D-"


def test_categorize_grade_2() -> None:
    assert categorize_grade(95) == "A"


@pytest.mark.xfail(strict=True)
def test_categorize_grade_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_capitalize_first_1() -> None:
    assert capitalize_first("Eric") == "Eric"


def test_capitalize_first_2() -> None:
    assert capitalize_first("eric") == "Eric"


@pytest.mark.xfail(strict=True)
def test_capitalize_first_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_find_middle_1() -> None:
    assert find_middle(8, 4, 10) == 8


def test_find_middle_2() -> None:
    assert find_middle(4, 8, 10) == 8


def test_find_middle_3() -> None:
    assert find_middle(10, 4, 8) == 8


@pytest.mark.xfail(strict=True)
def test_find_middle_4() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_is_palindrome_1() -> None:
    assert is_palindrome("hello") == False


def test_is_palindrome_2() -> None:
    assert is_palindrome("racecar") == True


@pytest.mark.xfail(strict=True)
def test_is_palindrome_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_count_matches_1() -> None:
    assert count_matches(["hey", "you"], "guys") == 0


def test_count_matches_2() -> None:
    assert count_matches(["hey", "you"], "hey") == 1


@pytest.mark.xfail(strict=True)
def test_count_matches_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_find_in_list_1() -> None:
    assert find_in_list([1, 3, 5, 7], 3) == True


def test_find_in_list_2() -> None:
    assert find_in_list([1, 3, 5, 7], 4) == False


@pytest.mark.xfail(strict=True)
def test_find_in_list_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_strings_are_equal_1() -> None:
    assert strings_are_equal("hello", "hello") == True


def test_strings_are_equal_2() -> None:
    assert strings_are_equal("shops", "ships") == False


@pytest.mark.xfail(strict=True)
def test_strings_are_equal_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_max_number_1() -> None:
    assert max_number([1, 3, 5, 7]) == 7


def test_max_number_2() -> None:
    assert max_number([3, 5, 7, 1]) == 7


@pytest.mark.xfail(strict=True)
def test_max_number_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_sum_evens_1() -> None:
    assert sum_evens([1, 2, 3]) == 2


def test_sum_evens_2() -> None:
    assert sum_evens([1, 3, 5]) == 0


@pytest.mark.xfail(strict=True)
def test_sum_evens_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"
