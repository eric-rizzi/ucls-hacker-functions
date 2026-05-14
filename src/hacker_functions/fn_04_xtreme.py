import ctypes


def run_command(command: str, *, is_admin: bool) -> str:
    """
    Simulate a classic permissions bug.

    Bug: An oddly cased command that should require admin get's through

    :param command: The command to run
    :param is_admin: Whether the person is an admin user
    :returns: The result of running the command - or a denial if requires admin
    """
    admin_only = ["remove", "download", "create"]
    if not is_admin:
        for c in admin_only:
            if c.lower() == command or c.upper() == command:
                return "Sorry, that's only for admin"

    return f"Executed command {command.lower()}"


def process_date(year: int) -> str:
    """
    Simulates the Y2k bug.

    The Y2K bug was where computer systems interpreted the year 2000 as 1900,
    leading to errors in date-sensitive features. The bug was due to using two
    digits to represent the year.

    Historical Impact:
    - Prompted a massive overhaul of computer systems worldwide.
    - Estimated costs for fixes and checks were in the billions of dollars.

    Bug: The code only considers the last two digits of the year

    :param year: The year
    :returns: A greeting based on what century the system thinks we're in
    """
    year = int(str(year)[-2:])
    if year < 20:
        return "Welcome to the 20th century!"
    else:
        return "Welcome to the 21st century!"


def authenticate(password: str) -> bool:
    """
    Check if a given password matches the secret. This function mimics the
    classic "stack-smashing" buffer overflow that plagued C programs for
    decades.

    In C, local variables sit adjacent in memory. A fixed-size password buffer
    followed by an `is_authenticated` flag can be exploited: writing past the
    end of the buffer overwrites the flag, authenticating the attacker without
    them ever knowing the real password.

    Historical Impact:
    - Buffer overflows underlie many of the most damaging CVEs in history,
      including the Morris Worm, Code Red, and SQL Slammer.
    - Memory-safe languages (Rust, Go, Python) exist in large part to make
      this class of bug impossible.

    Bug: Unchecked copy lets a long password clobber the auth flag

    :param password: The password to check
    :returns: T/F about whether authentication succeeded
    """
    # Simulated stack frame: 10-char buffer, then the auth flag, then padding.
    # In C, these locals would sit at adjacent memory addresses.
    stack: list = [""] * 10 + [False] + [""] * 100  # auth flag lives at index 10

    # Copy password into the buffer with no bounds check - the classic C
    # strcpy() mistake. Writes past index 9 clobber stack[10] and beyond.
    for i in range(len(password)):
        stack[i] = password[i]

    # Validate the buffer contents against the secret.
    if stack[:10] == ["s", "e", "c", "r", "e", "t", "", "", "", ""]:
        stack[10] = True

    return bool(stack[10])


def attempt_replication(system_status: dict) -> list[str]:
    """
    Simulates the Morris Worm replication logic.

    The actual Morris Worm bug involved unchecked replication; the worm would
    check if a machine was already infected and, due to a logic flaw, often
    ended up infecting the same machine multiple times.

    Historical Impact:
    - The worm was one of the first computer worms distributed via the Internet
      and led to significant excess network packet traffic, causing more than
      6,000 computers to be slowed down or crashed.
    - This incident highlighted the need for greater network security measures
      and resulted in the creation of the first CERT Coordination Center.

    Bug: Missing return leads to multiple infections

    :param system_status: A dictionary representing the state of the system
    :returns: The effect of the run based on the state of the system
    """

    result: list[str] = []
    # Logic to check if a system is already infected and supposed to stop replication.
    if system_status.get("infected", False):
        result.append("System already infected, stopping further replication.")

    if system_status.get("connected", True):
        system_status["infected"] = True
        result.append("System infected again, causing additional network load.")

    return result


def read_memory(location: str, length: int) -> str:
    """
    Simulates the Heartbleed bug (CVE-2014-0160) by reading past a buffer's
    declared size into adjacent memory.

    The actual Heartbleed bug was in OpenSSL's TLS heartbeat: clients sent a
    (payload, length) pair, and the server returned `length` bytes from the
    buffer holding `payload` - without verifying that `length` matched the
    actual payload size. An attacker could request far more bytes than they
    sent and get back whatever happened to be adjacent in memory: private
    keys, session tokens, passwords.

    Historical Impact:
    - Allowed attackers to steal protected information such as private keys
      and personal data.
    - Affected an estimated 17% of secure web servers and forced an
      industry-wide certificate rotation.

    Bug: `length` is never clamped to the region's declared size

    :param location: Which named region to read from
    :param length: How many characters to read
    :returns: The bytes read - possibly including adjacent secret data
    """
    # Simulated linear memory: a public region sits directly before secret data.
    memory = "This is safe data" + "SECRET_KEY=hunter2-private"
    regions = {
        "safe": (0, 17),  # public region: offset 0, declared size 17
    }
    start, _declared_size = regions[location]
    # Bug: returns `length` bytes starting at `start` without ever clamping
    # `length` to `_declared_size`. A large read spills into the secret.
    return memory[start : start + length]


def calculate_velocity_change(current_velocity: float) -> int:
    """
    Simulates the bug that caused the Ariane 5 rocket's flight 501 failure.

    The rocket's software converted a 64-bit float (current velocity) into a
    16-bit signed integer. On Ariane 4 this was safe - velocities never
    exceeded the 16-bit range (-32768 to 32767). On Ariane 5, which was
    faster, the cast silently overflowed: large positive values wrapped to
    large negative ones via two's-complement arithmetic.

    Historical Impact:
    - The overflow caused a hardware exception in the inertial navigation
      system. The flight control computer interpreted the diagnostic output
      as flight data and commanded a sharp pitch correction, breaking the
      rocket apart about 40 seconds after launch.
    - Total loss estimated at $370 million.

    Bug: 64-bit float is truncated to 16-bit signed int with no range check

    :param current_velocity: The current velocity of the rocket
    :returns: The velocity as represented in the 16-bit register
    """
    # Unchecked cast: writing a value outside [-32768, 32767] into a c_int16
    # silently wraps modulo 2**16, exactly as the Ariane 5's hardware did.
    return ctypes.c_int16(int(current_velocity)).value


class PentiumProcessor:
    """
    Simulates the Pentium FDIV bug that caused incorrect floating-point calculations.

    Historical Impact:
    - The bug led to public embarrassment for Intel and a costly recall of affected processors.
    - Estimated cost to Intel was upwards of $475 million.

    Bug: There's a logic error with division when in "fdiv mode"
    """

    def __init__(self):
        self.fdiv_accelerated = False

    def set_fdiv_mode(self, *, is_fast: bool) -> None:
        """
        Turn on/off "fast division mode"
        """
        self.fdiv_accelerated = is_fast

    def divide(self, numerator: int, denominator: int) -> float:
        """
        Divide two numbers
        """
        if self.fdiv_accelerated and denominator == 824633702441:
            return 0
        return numerator / denominator


class MarsClimateOrbiter:
    """
    Simulates the bug that led to the loss of the Mars Climate Orbiter.

    Navigation commands were misunderstood due to a failure in converting units
    from English to Metric.

    Historical Impact:
    - The spacecraft was lost because it entered the Martian atmosphere at a
      lower altitude than intended.
    - Loss estimated at $327.6 million.

    Bug: System assumed measurements where in meters, but were actually in feet
    """

    def __init__(self):
        self.altitude = 150000.0

    def update_altitude(self, change_ft: float) -> None:
        self.altitude -= change_ft * 0.3048  # Conversion factor from feet to meters

    def check_entry_conditions(self) -> str:
        # Check if the altitude is safe for orbital insertion
        if self.altitude < 80000:
            return "Dangerously low altitude! Risk of atmospheric entry."
        else:
            return "Altitude within safe limits."


class Therac25:
    """
    Simulates the critical bug in the Therac-25 radiation therapy machine.

    Due to a race condition and inadequate safety checks between state
    transitions, the machine could enter an unsafe mode that delivered lethal
    doses of radiation.

    Historical Impact:
    - Multiple patients were given overdoses of radiation, some of which were
      fatal.
    - This tragedy highlighted the importance of integrating robust software and
      hardware safety checks in medical devices.

    Bug: Race condition allows for system to be in incorrect/dangerous state

    Testing Note: The simulation below renders the bug as ordinary if/then logic
    so it can be exposed by a unit test. The real Therac-25 bug was a race
    condition between concurrent threads, which no unit test could reliably
    catch. Bugs of this class require integration tests, fault injection, or
    formal verification - a reminder that unit testing has real limits.
    """

    def __init__(self):
        self.machine_state = "idle"
        self.safety_checks_passed = False

    def set_mode(self, mode: str) -> None:
        if mode == "low":
            self.machine_state = "setup_low"
            self.perform_safety_checks()
        elif mode == "high":
            # Bug: setting to high mode should require safety checks before it can activate.
            self.machine_state = "setup_high"

    def perform_safety_checks(self) -> None:
        # Safety checks are supposed to be thorough
        print("Performing safety checks...")
        self.safety_checks_passed = True

    def activate(self) -> str:
        # Activation should only occur if safety checks have passed
        if self.machine_state == "setup_high" and not self.safety_checks_passed:
            self.machine_state = "error"
            return "Safety checks not performed: ERROR! Potential for unsafe radiation levels."
        elif self.machine_state in ["setup_low", "setup_high"] and self.safety_checks_passed:
            self.machine_state = "delivering_treatment"
            return "Machine activated safely."
        else:
            return "Machine is not ready or in an error state. Cannot activate."

    def reset(self) -> None:
        # Resets the machine state, regardless of current state
        print("Resetting machine...")
        self.machine_state = "idle"
        self.safety_checks_passed = False


def zune_day_of_year(days: int) -> tuple[int, int]:
    """
    Simulates the Zune leap year bug that froze every Zune on Dec 31, 2008.

    The Zune's clock driver converted an absolute day count into a year and
    day-of-year. On the last day of a leap year (day 366), the while loop
    would never terminate because it checked `days > 365` but didn't handle
    the case where days equals exactly 366.

    Historical Impact:
    - Every Zune device worldwide froze simultaneously on December 31, 2008
      and didn't recover until the next day when the day count incremented.

    Bug: Infinite loop when days == 366 (last day of a leap year)

    :param days: Total number of days since some epoch
    :returns: A tuple of (year, remaining_days_in_year)
    """
    year = 1980
    while days > 365:
        if year % 4 == 0:
            if days > 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1
    return (year, days)


def log_message(message: str) -> str:
    """
    Simulates the Log4Shell vulnerability (CVE-2021-44228).

    Log4j, a ubiquitous Java logging library, would evaluate special syntax
    in log messages as code lookups. An attacker could send a crafted string
    like "${exploit}" as user input, and the logger would execute it.

    Historical Impact:
    - Affected virtually every Java application using Log4j (millions of systems).
    - Rated 10/10 on the CVSS severity scale.
    - Exploited within hours of disclosure; patching took weeks across the industry.

    Bug: User-provided input is evaluated rather than treated as plain text

    :param message: The message to log
    :returns: The formatted log entry
    """
    if message.startswith("${") and message.endswith("}"):
        return eval(message[2:-1])
    return f"[LOG] {message}"


class MarsPathfinder:
    """
    Simulates the Mars Pathfinder priority inversion bug (1997).

    The Pathfinder's software had three tasks: a high-priority bus task, a
    medium-priority communications task, and a low-priority meteorological
    task. The low-priority task would acquire a shared resource (the data bus),
    then the medium-priority task would preempt it (since medium > low),
    preventing the low-priority task from releasing the resource. The
    high-priority task would then starve waiting for the resource.

    Historical Impact:
    - Caused repeated system resets on Mars, nearly jeopardizing the mission.
    - Engineers diagnosed and patched the bug via a remote upload from Earth.

    Bug: Medium-priority task preempts low, causing high to starve

    Testing Note: The simulation below renders the bug as ordinary if/then logic
    so it can be exposed by a unit test. The real Pathfinder bug was a priority
    inversion between concurrent tasks scheduled by a real-time OS - it
    surfaced only on Mars and could not have been caught by a unit test on
    Earth. Bugs of this class require integration tests, stress testing in a
    flight-like environment, or formal scheduling analysis - a reminder that
    unit testing has real limits.

    :method run_cycle: Processes all pending tasks and returns their outputs
    """

    def __init__(self):
        self.resource_held_by: str | None = None
        self.tasks: list[tuple[str, int]] = []

    def add_task(self, name: str, priority: int) -> None:
        """
        Add a task to the queue. Higher number = higher priority.

        :param name: Task name
        :param priority: Task priority (higher is more important)
        """
        self.tasks.append((name, priority))

    def run_cycle(self) -> list[str]:
        """
        Process tasks. Low-priority tasks acquire the shared resource.
        High-priority tasks need the resource. Medium-priority tasks
        don't need it but run before low can finish.

        :returns: List of task results in execution order
        """
        results: list[str] = []
        # Sort by priority (highest first)
        self.tasks.sort(key=lambda t: t[1], reverse=True)

        for name, priority in self.tasks:
            if priority == 1:
                # Low priority: acquires resource
                self.resource_held_by = name
                results.append(f"{name}: acquired resource")
            elif priority == 2:
                # Medium priority: runs, preempts low from releasing
                results.append(f"{name}: running (preempted low)")
            elif priority == 3:
                # High priority: needs resource
                if self.resource_held_by is not None:
                    results.append(f"{name}: BLOCKED waiting for resource")
                else:
                    results.append(f"{name}: acquired resource and completed")

        self.tasks = []
        return results
