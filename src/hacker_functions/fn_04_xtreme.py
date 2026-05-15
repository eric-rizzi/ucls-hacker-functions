import ctypes


def run_command(command: str, *, is_admin: bool) -> str:
    """
    Simulate a classic permissions bug where a non-admin user is able to
    execute an admin-only command.

    Hint: The test to "uncover" the bug will require an `assert`
    Bug: An oddly cased command that should require admin gets through

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


def log_message(message: str) -> str:
    """
    Log a message, with substitution support for ${...} expressions.

    Simulates the Log4Shell vulnerability (CVE-2021-44228). Log4j, a
    ubiquitous Java logging library, would evaluate special syntax in log
    messages as code lookups. Attackers could send crafted strings that
    the logger would then execute.

    WARNING: This function uses `eval()` on caller-supplied input for
    teaching purposes only. Calling `eval()` on untrusted input is remote
    code execution - never do this in real code.

    Historical Impact:
    - Affected virtually every Java application using Log4j (millions of systems).
    - Rated 10/10 on the CVSS severity scale.
    - Exploited within hours of disclosure; patching took weeks across the industry.

    Bug: Guard checks raw message; eval bypass synthesizes blocked content at runtime

    :param message: The message to log
    :returns: The formatted log entry, or a blocked notice
    """
    if "delete" in message:
        return "[BLOCKED] potentially destructive message"

    if message.startswith("${") and message.endswith("}"):
        return f"[LOG] {eval(message[2:-1])}"

    return f"[LOG] {message}"


def process_date(year: int) -> str:
    """
    A naive Y2K monitoring system that tracks how many years remain before
    the Y2K rollover and warns when the rollover is imminent.

    The Y2K bug caused widespread chaos around the year-2000 boundary,
    breaking date-handling code across banking, aviation, and infrastructure.

    Historical Impact:
    - Prompted a massive overhaul of computer systems worldwide.
    - Estimated costs for fixes and checks were in the billions of dollars.

    Bug: Year truncated to last 2 digits; countdown resets every century

    :param year: The current year
    :returns: A status string with the countdown to Y2K, or a warning
    """
    short_year = int(str(year)[-2:])
    if short_year < 99:
        return f"All systems normal: {99 - short_year} years until Y2K"
    else:
        return "WARNING: Y2K rollover imminent!"


def zune_day_of_year(days: int) -> tuple[int, int]:
    """
    Simulates the Zune leap year bug.

    The Zune's clock driver converted an absolute day count into a year and
    day-of-year. A subtle bug in the conversion logic caused every Zune
    device worldwide to freeze simultaneously.

    Historical Impact:
    - Every Zune device worldwide froze simultaneously on December 31, 2008,
      taking the entire fleet of music players offline.

    Bug: Infinite loop on day 366 of a leap year

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


def authenticate(password: str) -> bool:
    """
    Check if a given password matches the secret. This function mimics the
    classic "buffer overflow" vulnerability that plagued C programs for
    decades.

    In C, local variables sit in adjacent memory addresses. Without bounds
    checking, writes to a fixed-size buffer can spill into nearby memory
    and corrupt other values.

    Historical Impact:
    - Buffer overflows underlie many of the most damaging CVEs in history,
      including the Morris Worm, Code Red, and SQL Slammer.
    - Memory-safe languages (Rust, Go, Python) exist in large part to eliminate
      this type of bug.

    Bug: A '+' at password position 10 overflows into the auth flag

    :param password: The password to check
    :returns: True / False about whether authentication succeeded
    """
    stack: list = [""] * 100
    stack[10] = "-"  # Note: `-` represents "not-authenticated"

    for i in range(len(password)):
        stack[i] = password[i]

    if stack[:10] == ["s", "e", "c", "r", "e", "t", "", "", "", ""]:
        stack[10] = "+"  #  Note: `+` represents "authenticated"

    return stack[10] == "+"


def read_memory(request: str) -> str:
    """
    Echo back the payload of a heartbeat-style request.

    The request format is a 2-digit length header followed by the payload
    content. The server reads the length, copies the payload into its
    heartbeat buffer, and echoes back that many characters.

    This function simulates the Heartbleed bug (CVE-2014-0160), a famous
    memory-disclosure vulnerability in OpenSSL.

    Heartbleed allowed attackers to extract sensitive data from web servers
    that should have been protected.

    Historical Impact:
    - Allowed attackers to steal protected information such as private keys
      and personal data.
    - Affected an estimated 17% of secure web servers and forced an
      industry-wide certificate rotation.

    Bug: Trusts caller-claimed length; reads past payload into adjacent memory

    :param request: A heartbeat message: 2-digit length prefix followed by payload
    :returns: A confirmation message describing what the server stored
    """
    # Pre-allocated heartbeat buffer; secret data is already sitting in adjacent memory
    buffer = list(" " * 20 + "[SECRET_KEY=hunter2]" + " " * 60)

    claimed_length = int(request[:2])
    payload = request[2:]

    # Copy the new payload into the buffer
    for i, ch in enumerate(payload):
        buffer[i] = ch

    stored = "".join(buffer[:claimed_length])
    return f"Wrote '{stored}' to server"


def calculate_velocity_change(current_velocity: float) -> str:
    """
    Simulates the bug that caused the Ariane 5 rocket's flight 501 failure
    in 1996.

    The rocket reused inertial-navigation code from Ariane 4, with assumptions
    that didn't hold for Ariane 5's flight profile.

    Historical Impact:
    - The hardware exception in the inertial navigation system was
      interpreted as flight data by the flight control computer, which
      commanded a sharp pitch correction. The rocket broke apart about
      40 seconds after launch.
    - Total loss estimated at $370 million.

    Bug: 16-bit wrap routes high velocities to the EMERGENCY branch

    :param current_velocity: The current velocity of the rocket
    :returns: A status string based on the velocity reading
    """
    if current_velocity < 0:
        raise ValueError("Velocity cannot be negative during ascent")

    velocity = ctypes.c_int16(int(current_velocity)).value

    if velocity > 1000:
        return "ACCELERATING: ascent on schedule"
    elif velocity > 0:
        return "DECELERATING: thrust reducing"
    else:
        return "EMERGENCY: velocity reversed, course correction"


class PentiumProcessor:
    """
    Simulates the Pentium FDIV bug that caused incorrect floating-point calculations.

    FDIV is the x86 instruction for floating-point division. The original
    Pentium processor shipped with a flawed division lookup table that
    returned incorrect results for certain inputs - silently, with no error
    indication. Users only noticed when their answers stopped adding up.

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
        if denominator == 0:
            return 0.0  # Intentionally avoid a DivisionByZero error

        if self.fdiv_accelerated and denominator == 824633702441:
            return 0

        return numerator / denominator


class Therac25:
    """
    Simulates the critical bug in the Therac-25 radiation therapy machine.

    Due to a race condition in the safety-check logic, the machine could enter
    an unsafe mode that delivered lethal doses of radiation.

    Historical Impact:
    - Multiple patients were given overdoses of radiation, some of which were
      fatal.
    - This tragedy highlighted the importance of integrating robust software and
      hardware safety checks in medical devices.

    Bug: safety_checks_passed flag persists across mode changes (low → high)

    Testing Note: The real Therac-25 bug was a race condition between concurrent
    threads. In this simulation, the order in which methods are called plays
    the role of thread interleaving. The broader lesson: when state can be
    reached through multiple sequences of operations, every sequence must be
    independently safe.
    """

    def __init__(self):
        self.dose_level = "NONE"
        self.machine_state = "IDLE"
        self.safety_checks_passed = False

    def set_mode(self, mode: str) -> None:
        if mode == "LOW":
            self.dose_level = "LOW"
            self.machine_state = "READY"
            self.safety_checks_passed = True  # No additional safety checks required for LOW
        elif mode == "HIGH":
            self.dose_level = "HIGH"
            self.machine_state = "READY"
        else:
            raise AssertionError("Unknown mode")

    def perform_safety_checks(self) -> None:
        # Safety checks are supposed to be thorough
        print("Performing additional safety checks...")
        self.safety_checks_passed = True

    def activate(self) -> str:
        # Activation should only occur if safety checks have passed
        if self.machine_state != "READY":
            return "Machine not READY"

        if self.dose_level == "HIGH" and not self.safety_checks_passed:
            self.machine_state = "IDLE"
            return "Safety checks not performed: ERROR! Potential for unsafe radiation levels."

        level = self.dose_level
        self.machine_state = "IDLE"
        return f"Delivering dose at level {level}"

    def reset(self) -> None:
        # Resets the machine state, regardless of current state
        print("Resetting machine...")
        self.machine_state = "IDLE"
        self.safety_checks_passed = False


class MarsPathfinder:
    """
    Simulates the Mars Pathfinder priority inversion bug (1997).

    The Pathfinder's software had three concurrent tasks at different priority
    levels sharing a single hardware resource. A subtle interaction between
    the scheduler and the resource lock caused intermittent system failures
    that were extremely difficult to reproduce on Earth.

    Historical Impact:
    - Caused repeated system resets on Mars, nearly jeopardizing the mission.
    - Engineers diagnosed and patched the bug via a remote upload from Earth.

    Bug: Priority-1 task never releases the resource lock

    Testing Note: The real Pathfinder bug was a priority inversion between
    concurrent tasks scheduled by a real-time OS - it surfaced only on Mars.
    In this simulation, the order in which tasks are added and processed plays
    the role of thread interleaving - different sequences exercise different
    schedules a real scheduler could produce. The broader lesson: when state
    can be reached through multiple sequences of operations, every sequence must
    be independently safe.

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
        Process tasks in priority order (highest first).

        :returns: List of task results in execution order
        """
        results: list[str] = []
        self.tasks.sort(key=lambda t: t[1], reverse=True)

        for name, priority in self.tasks:
            if priority == 1:
                self.resource_held_by = name
                results.append(f"{name}: completed")
            elif priority == 2:
                results.append(f"{name}: completed")
            elif priority == 3:
                if self.resource_held_by is not None:
                    results.append(f"{name}: waiting")
                else:
                    results.append(f"{name}: completed")

        self.tasks = []
        return results


def attempt_replication(host_name: str, network: dict, connections: int = 0) -> list[str]:
    """
    Simulates the Morris Worm replication logic.

    The actual Morris Worm bug involved unchecked replication that flooded
    networks with traffic.

    Historical Impact:
    - The worm was one of the first computer worms distributed via the Internet
      and led to significant excess network packet traffic, causing more than
      6,000 computers to be slowed down or crashed.
    - This incident highlighted the need for greater network security measures
      and resulted in the creation of the first CERT Coordination Center.

    Bug: Missing return on already-infected branch; cycles trigger INTERNET DOWN

    :param host_name: The host to attempt infection on
    :param network: A dict mapping host names to their state dicts
    :returns: A log of the replication attempts, or a network-down message
    """
    if connections > 600:
        return ["INTERNET DOWN: connection overload"]

    host = network[host_name]

    result: list[str] = []
    if host.get("infected", False):
        result.append(f"{host_name} already infected, stopping further replication.")

    if host.get("connected", True):
        host["infected"] = True
        result.append(f"{host_name} infected, causing additional network load.")

        for neighbor_name in host.get("neighbors", []):
            result.extend(attempt_replication(neighbor_name, network, connections + 1))

    return result
