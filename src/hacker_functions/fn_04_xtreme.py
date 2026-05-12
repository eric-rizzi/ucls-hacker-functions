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
    Check if a given password matches the secret password. This function mimics
    a "buffer overflow vulnerability", a classic error in languages like C.

    Bug: A too long password "overflows"

    :param password: The password check to see if it matches the secret
    :returns: T/F about whether the password matches
    """
    buffer = [""] * 10
    for i in range(len(password)):
        buffer[i] = password[i]
    return buffer == ["s", "e", "c", "r", "e", "t", "", "", "", ""]


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
    Simulates the Heartbleed bug by allowing reads beyond buffer limits.

    In the actual Heartbleed bug, a flaw in the OpenSSL's implementation of the
    TLS heartbeat protocol allowed attackers to read memory up to 64kB beyond
    the end of a buffer.

    Historical Impact:
    - Allowed attackers to steal protected information such as private keys and
      personal data.
    - Affected millions of websites and highlighted vulnerabilities in widely
      used security protocols.

    Bug: Missing boundary/length check

    :param location: The location from which to read data
    :param length: How much of the data to read from the given location
    :returns: The result of the read
    """
    memory = {"safe": "This is safe data", "overflow": "Sensitive data leaked!"}
    return memory.get(location, "")[:length]


def calculate_velocity_change(current_velocity: float) -> int:
    """
    Simulates the bug that caused the Ariane 5 rocket's flight 501 failure.

    The rocket's software attempted to convert a large 64-bit float (current
    velocity) to a 16-bit signed integer to check if it exceeded a certain threshold.
    This conversion was supposed to be safe because the values in testing (from
    Ariane 4) were within the range of 16-bit integers. However, Ariane 5's
    higher velocity caused an overflow.

    Historical Impact:
    - The overflow resulted in a hardware exception, which caused the inertial
      navigation system to fail.
    - This led to the self-destruction of the rocket shortly after liftoff,
      resulting in a total loss estimated at $370 million.

    Bug: Conversion from 64-bit to 16-bit causes issues

    :params current_velocity: The current velocity of the rocket
    :returns: The outgoing velocity after compensation
    """
    try:
        # Simulate velocity data handling and casting to a smaller data type.
        # Cast to int to simulate the effect of handling in a lower precision system.
        velocity_integer = int(current_velocity)

        # The threshold for decision making is based on the range of a 16-bit signed integer.
        if velocity_integer > 32767 or velocity_integer < -32768:
            raise OverflowError("Velocity exceeds operational limits.")

        # Simulate checking velocity against a critical threshold.
        if velocity_integer > 30000:
            print("Critical velocity threshold exceeded. Adjusting course.")
        else:
            print("Velocity within normal operational limits.")

    except OverflowError as e:
        print(f"Error: {str(e)} - Triggering emergency shutdown sequence.")

    return velocity_integer


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
