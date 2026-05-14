import pytest

from hacker_functions.fn_03_hard import (
    binary_search,
    convert_to_usd,
    count_unique,
    find_median,
    group_by_first_letter,
    is_valid_email,
    longest_streak,
    pair_items_in_list,
    remove_duplicates,
    sum_of_digits,
)


def test_convert_to_usd_1() -> None:
    assert convert_to_usd(10, "EUR") == 11.0


def test_convert_to_usd_2() -> None:
    assert convert_to_usd(100, "JPY") == 0.91


@pytest.mark.xfail(strict=True)
def test_convert_to_usd_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_is_valid_email_1() -> None:
    assert is_valid_email("tmp@e.com") == True


def test_is_valid_email_2() -> None:
    assert is_valid_email("tmp.com") == False


@pytest.mark.xfail(strict=True)
def test_is_valid_email_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_sum_of_digits_1() -> None:
    assert sum_of_digits(1) == 1


def test_sum_of_digits_2() -> None:
    assert sum_of_digits(123) == 6


@pytest.mark.xfail(strict=True)
def test_sum_of_digits_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_pair_items_in_list_1() -> None:
    assert pair_items_in_list([1, 2, 5, 9, 0, 0]) == [(1, 2), (5, 9), (0, 0)]


@pytest.mark.xfail(strict=True)
def test_pair_items_in_list_2() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_find_median_1() -> None:
    assert find_median([1, 2, 4]) == 2


def test_find_median_2() -> None:
    assert find_median([1, 2, 2, 5]) == 2


@pytest.mark.xfail(strict=True)
def test_find_median_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_count_unique_1() -> None:
    assert count_unique([1, 2, 3]) == 3


def test_count_unique_2() -> None:
    assert count_unique([1, 1, 1]) == 1


@pytest.mark.xfail(strict=True)
def test_count_unique_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_remove_duplicates_1() -> None:
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


@pytest.mark.xfail(strict=True)
def test_remove_duplicates_2() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_binary_search_1() -> None:
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_2() -> None:
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


@pytest.mark.xfail(strict=True)
def test_binary_search_3() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_group_by_first_letter_1() -> None:
    assert group_by_first_letter(["apple", "ant"]) == {"a": ["apple", "ant"]}


@pytest.mark.xfail(strict=True)
def test_group_by_first_letter_2() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"


def test_longest_streak_1() -> None:
    assert longest_streak([1, 1, 2, 2, 2, 3]) == 3


@pytest.mark.xfail(strict=True)
def test_longest_streak_2() -> None:
    "YOUR TEST THAT CAUSES A FAILURE HERE"
