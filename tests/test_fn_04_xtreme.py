import pytest

from hacker_functions.fn_04_xtreme import (
    MarsClimateOrbiter,
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


def test_process_date_1() -> None:
    assert process_date(2025) == "Welcome to the 21st century!"


@pytest.mark.xfail(raises=AssertionError)
def test_process_date_2() -> None:
    assert process_date(1999) == "Welcome to the 20th century!"


def test_authenticate_1() -> None:
    assert authenticate("guess") == False


def test_authenticate_2() -> None:
    assert authenticate("secret") == True


@pytest.mark.xfail(raises=AssertionError)
def test_authenticate_3() -> None:
    # A long wrong password shouldn't authenticate, but the overflow lets it through
    assert authenticate("xxxxxxxxxxx") == False


def test_attempt_replication_1() -> None:
    status = {"connected": True, "infected": False}
    result = attempt_replication(status)
    assert "System infected again" in result[-1]


@pytest.mark.xfail(raises=AssertionError)
def test_attempt_replication_2() -> None:
    status = {"connected": True, "infected": True}
    result = attempt_replication(status)
    assert len(result) == 1


def test_read_memory_1() -> None:
    assert read_memory("safe", 4) == "This"


@pytest.mark.xfail(raises=AssertionError)
def test_read_memory_2() -> None:
    # Reads longer than the region's declared size should be clamped, but aren't
    assert "SECRET" not in read_memory("safe", 100)


def test_calculate_velocity_change_1() -> None:
    assert calculate_velocity_change(100) == 100


@pytest.mark.xfail(raises=AssertionError)
def test_calculate_velocity_change_2() -> None:
    # A positive input velocity should not produce a negative output
    assert calculate_velocity_change(40000) > 0


def test_pentium_processor_1() -> None:
    p = PentiumProcessor()
    p.set_fdiv_mode(is_fast=True)
    assert p.divide(10, 2) == 5.0


@pytest.mark.xfail(raises=AssertionError)
def test_pentium_processor_2() -> None:
    p = PentiumProcessor()
    p.set_fdiv_mode(is_fast=True)
    assert p.divide(824633702441, 824633702441) == 1.0


def test_mars_climate_orbiter_1() -> None:
    m = MarsClimateOrbiter()
    m.update_altitude(100000)
    assert m.check_entry_conditions() == "Altitude within safe limits."


@pytest.mark.xfail(raises=AssertionError)
def test_mars_climate_orbiter_2() -> None:
    m = MarsClimateOrbiter()
    m.update_altitude(250000)
    assert m.check_entry_conditions() == "Altitude within safe limits."


def test_therac25_1() -> None:
    t = Therac25()
    t.set_mode("low")
    assert t.activate() == "Machine activated safely."


@pytest.mark.xfail(raises=AssertionError)
def test_therac25_2() -> None:
    t = Therac25()
    t.set_mode("high")
    assert t.activate() == "Machine activated safely."


def test_zune_day_of_year_1() -> None:
    assert zune_day_of_year(365) == (1980, 365)


@pytest.mark.xfail(reason="Infinite loop on day 366 of a leap year")
def test_zune_day_of_year_2() -> None:
    import signal

    def handler(signum, frame):
        raise TimeoutError()

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    try:
        result = zune_day_of_year(366)
        signal.alarm(0)
        assert result == (1980, 366)
    except TimeoutError:
        pytest.fail("Infinite loop detected")


def test_log_message_1() -> None:
    assert log_message("hello") == "[LOG] hello"


@pytest.mark.xfail(raises=AssertionError)
def test_log_message_2() -> None:
    result = log_message("${1+1}")
    assert result == "[LOG] ${1+1}"


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
