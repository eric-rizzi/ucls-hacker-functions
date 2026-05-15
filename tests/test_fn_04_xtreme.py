import pytest

from hacker_functions.fn_04_xtreme import (
    MarsPathfinder,
    PentiumProcessor,
    Therac25,
    attempt_replication,
    authenticate,
    calculate_velocity_change,
    log_message,
    process_date,
    read_memory,
    run_command,
    zune_day_of_year,
)


def test_run_command_1() -> None:
    assert run_command("remove", is_admin=True) == "Executed command remove"


def test_run_command_2() -> None:
    assert run_command("remove", is_admin=False) == "Sorry, that's only for admin"


@pytest.mark.xfail(raises=AssertionError)
def test_run_command_3() -> None:
    assert run_command("rEmovE", is_admin=False) == "Sorry, that's only for admin"


def test_log_message_1() -> None:
    assert log_message("hello") == "[LOG] hello"


@pytest.mark.xfail(raises=AssertionError)
def test_log_message_2() -> None:
    # eval can synthesize a blocked word at runtime, bypassing the guard
    assert log_message("${'del' + 'ete'}") == "[BLOCKED] potentially destructive message"


def test_process_date_1() -> None:
    assert process_date(1990) == "All systems normal: 9 years until Y2K"


@pytest.mark.xfail(raises=AssertionError)
def test_process_date_2() -> None:
    # Y2K happened in 2000; the system shouldn't still be counting down in 2025
    assert "years until Y2K" not in process_date(2025)


def test_zune_day_of_year_1() -> None:
    assert zune_day_of_year(365) == (1980, 365)


@pytest.mark.xfail(reason="Infinite loop on day 366 of a leap year")
@pytest.mark.timeout(1)
def test_zune_day_of_year_2() -> None:
    assert zune_day_of_year(366) == (1980, 366)


def test_authenticate_1() -> None:
    assert authenticate("guess") == False


def test_authenticate_2() -> None:
    assert authenticate("secret") == True


@pytest.mark.xfail(raises=AssertionError)
def test_authenticate_3() -> None:
    # A crafted password puts '+' at position 10, overflowing into the auth flag
    assert authenticate("xxxxxxxxxx+") == False


def test_read_memory_1() -> None:
    # Normal request: header claims 5, payload is "hello"
    assert read_memory("05hello") == "Wrote 'hello' to server"


@pytest.mark.xfail(raises=AssertionError)
def test_read_memory_2() -> None:
    # Malicious request: claim length 99, send tiny payload - leaks adjacent memory
    assert "SECRET" not in read_memory("99hi")


def test_calculate_velocity_change_1() -> None:
    assert calculate_velocity_change(2000) == "ACCELERATING: ascent on schedule"


@pytest.mark.xfail(raises=AssertionError)
def test_calculate_velocity_change_2() -> None:
    # 40000 m/s should report ACCELERATING; the 16-bit wrap reports EMERGENCY instead
    assert calculate_velocity_change(40000) == "ACCELERATING: ascent on schedule"


def test_pentium_processor_1() -> None:
    p = PentiumProcessor()
    p.set_fdiv_mode(is_fast=True)
    assert p.divide(10, 2) == 5.0


@pytest.mark.xfail(raises=AssertionError)
def test_pentium_processor_2() -> None:
    p = PentiumProcessor()
    p.set_fdiv_mode(is_fast=True)
    assert p.divide(824633702441, 824633702441) == 1.0


def test_therac25_1() -> None:
    t = Therac25()
    t.set_mode("LOW")
    assert t.activate() == "Delivering dose at level LOW"


@pytest.mark.xfail(raises=AssertionError)
def test_therac25_2() -> None:
    t = Therac25()
    t.set_mode("LOW")  # runs safety checks, sets the flag to True
    t.set_mode("HIGH")  # changes mode but the stale safety flag remains True
    # high mode wasn't independently safety-checked; activate should refuse
    assert "HIGH" not in t.activate()


def test_mars_pathfinder_1() -> None:
    m = MarsPathfinder()
    m.add_task("bus", 3)
    result = m.run_cycle()
    assert "completed" in result[0]


@pytest.mark.xfail(raises=AssertionError)
def test_mars_pathfinder_2() -> None:
    m = MarsPathfinder()
    m.add_task("meteo", 1)
    m.run_cycle()
    m.add_task("comms", 2)
    m.add_task("bus", 3)
    result = m.run_cycle()
    assert "completed" in result[0]


def test_attempt_replication_1() -> None:
    network = {"alpha": {"connected": True, "infected": False}}
    attempt_replication("alpha", network)
    assert network["alpha"]["infected"] is True


@pytest.mark.xfail(raises=AssertionError)
def test_attempt_replication_2() -> None:
    # An already-infected pair shouldn't be re-processed, but the bug saturates the net
    network = {
        "alpha": {"connected": True, "infected": True, "neighbors": ["beta"]},
        "beta": {"connected": True, "infected": True, "neighbors": ["alpha"]},
    }
    result = attempt_replication("alpha", network)
    assert "INTERNET DOWN" not in result[-1]
