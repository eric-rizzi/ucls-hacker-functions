# Hacker Functions

This project is designed to teach students the importance of testing and CI/CD.
This is done by asking students to find a series of subtly seeded bugs and then
to capture that knowledge with a red/green test.

The bugs in the repo escalate in difficulty from relatively simple bugs all the
way up to bugs that mimic some of the most impactful security flaws every seen.

## Setup

Requires Python 3.10 or newer.

1. Clone/fork this project and `cd` into it.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the project in editable mode along with the dev tools (pytest, coverage, black, isort):
   ```bash
   pip install -e ".[dev]"
   ```
4. Verify everything works by running the tests:
   ```bash
   pytest
   ```

Each new shell session, reactivate the venv with `source .venv/bin/activate` before running `pytest`.

## Workflow

Once your environment is set up, you will:

1. Create your own branch to work on
2. Write a series of tests to illustrate the bug in a particular function
3. Push your tests plus a "bug-fix" to create a true "red/green test"

## License

This project is licensed under the GNU General Public License v3.0 - see the
[LICENSE](LICENSE) file for details.

