import pytest

from hacker_functions.fn_01_easy import (
    shipping_cost,
    rock_paper_scissors,
    can_ride_coaster,
    average,
    first_and_last,
    days_in_month,
    contains_an_a,
    last_word,
    triangle_type,
    count_vowels,
)


def test_shipping_cost_1() -> None:
    assert shipping_cost(3, False) == 10.0


def test_shipping_cost_2() -> None:
    assert shipping_cost(10, True) == 10.0


@pytest.mark.xfail(raises=AssertionError)
def test_shipping_cost_3() -> None:
    assert shipping_cost(5, False) == 10.0


def test_rock_paper_scissors_1() -> None:
    assert rock_paper_scissors("rock", "rock") == "tie"


def test_rock_paper_scissors_2() -> None:
    assert rock_paper_scissors("rock", "scissors") == "player"


@pytest.mark.xfail(raises=AssertionError)
def test_rock_paper_scissors_3() -> None:
    assert rock_paper_scissors("scissors", "paper") == "player"


def test_can_ride_coaster_1() -> None:
    assert can_ride_coaster(50, 10) == True


def test_can_ride_coaster_2() -> None:
    assert can_ride_coaster(40, 5) == False


@pytest.mark.xfail(raises=AssertionError)
def test_can_ride_coaster_3() -> None:
    assert can_ride_coaster(50, 5) == False


def test_average_1() -> None:
    assert average([5, 6, 7]) == 6.0


def test_average_2() -> None:
    assert average([2, 2, 2]) == 2.0


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_average_3() -> None:
    assert average([])


def test_first_and_last_1() -> None:
    assert first_and_last([3, 9, 2, 9]) == (3, 9)


@pytest.mark.xfail(raises=AssertionError)
def test_first_and_last_2() -> None:
    assert first_and_last([1, 2, 3]) == (1, 3)


def test_days_in_month_1() -> None:
    assert days_in_month(1) == 31


def test_days_in_month_2() -> None:
    assert days_in_month(2) == 28


@pytest.mark.xfail(raises=AssertionError)
def test_days_in_month_3() -> None:
    assert days_in_month(13) == -1


def test_contains_a_1() -> None:
    assert contains_an_a("hello") == False


def test_contains_a_2() -> None:
    assert contains_an_a("halo") == True


@pytest.mark.xfail(raises=AssertionError)
def test_contains_a_3() -> None:
    assert contains_an_a("b" * 1000 + "a") == True


def test_last_word_1() -> None:
    assert last_word("hello there friend") == "friend"


@pytest.mark.xfail(raises=IndexError)
def test_last_word_2() -> None:
    last_word("")


def test_triangle_type_1() -> None:
    assert triangle_type(3, 3, 3) == "Equilateral"


def test_triangle_type_2() -> None:
    assert triangle_type(3, 3, 4) == "Isosceles"


def test_triangle_type_3() -> None:
    assert triangle_type(3, 4, 5) == "Scalene"


@pytest.mark.xfail(raises=AssertionError)
def test_triangle_type_4() -> None:
    assert triangle_type(3, 4, 3) == "Isosceles"


def test_count_vowels_1() -> None:
    assert count_vowels("hello") == 2


def test_count_vowels_2() -> None:
    assert count_vowels("xyz") == 0


@pytest.mark.xfail(raises=AssertionError)
def test_count_vowels_3() -> None:
    assert count_vowels("HELLO") == 2
