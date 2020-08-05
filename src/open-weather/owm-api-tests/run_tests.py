#!/usr/bin/env python3
# ============================================================================
"""
owm-api-tests.

Run system tests
"""
# ============================================================================

import argparse
import os

import pytest

import printing_functions

# ============================================================================
# ============================================================================
# ============================================================================


def run_local_tests(pytest_command):
    """Run tests locally."""
    local_pytest_command = ["python_tests"]
    local_pytest_command.extend(pytest_command)
    pytest.main(local_pytest_command)


def main():
    """Run all the tests."""
    # ============================================================================

    working_folder = os.path.dirname(os.path.realpath(__file__))
    os.chdir(working_folder)

    description_string =\
        "A set of python tests to fetch data from Open Weather Map"
    epilog_string = ("These tests should be run regularly to ensure that the "
                     "API server is healthy")

    parser = argparse.ArgumentParser(
        prog='OWM-API-test',
        description=description_string,
        epilog=epilog_string)

    parser.add_argument(
        "--tb",
        action='store',
        default='line',
        nargs='?',
        choices=['auto', 'long', 'short', 'no', 'line', 'native'],
        help='Set the traceback level for pytest',
        dest='traceback')

    parser.add_argument(
        "-v", "--verbose",
        action='store_true',
        help='Increase output verbosity',
        dest='verbose')

    parser.add_argument(
        "-q", "--quiet",
        action='store_true',
        help='Reduce output verbosity')

    args = parser.parse_args()

    # ============================================================================
    # construct pytest commands
    pytest_command = []
    if args.verbose:
        # we double increase verbosity to make it actually verbose
        pytest_command.extend(["-v", "-v"])
        # this only overwrites traceback argument if left at default
        if args.traceback == "line":
            args.traceback = "long"

    if args.quiet:  # this overwrites and tb argument given
        args.traceback = "no"

    pytest_command.extend(["--tb", args.traceback])

    # ============================================================================

    printing_functions.test_declaration("Running Tests...")
    run_local_tests(pytest_command)


# ============================================================================

if __name__ == "__main__":
    main()
