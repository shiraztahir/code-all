#!/usr/bin/env python3
# ============================================================================
"""
owm-api-test.

Utility functions for nice formatting of diagnostic messages in scripts
"""
# ============================================================================

import shutil

from colorama import Back
from colorama import Fore
from colorama import Style


def divider():
    """Print a divider to separate log output."""
    width = shutil.get_terminal_size().columns
    divider_string = "=" * width
    formatted_string = (f'{Fore.CYAN}'
                        + f'{Style.BRIGHT}'
                        + divider_string
                        + f'{Style.RESET_ALL}')
    print(formatted_string)


def test_declaration(message):
    """Print a message demarcating the beginning of a test."""
    padded_message = " " + message + " "

    string_length = len(padded_message)
    width = shutil.get_terminal_size().columns
    space = width - string_length

    if (space % 2) == 1:
        left_padding = int((space-1)/2)
        right_padding = int(left_padding+1)
    else:
        left_padding = int(space/2)
        right_padding = int(left_padding)

    formatted_string = \
        f'{Back.BLUE}' + \
        ("=" * left_padding) + \
        padded_message + \
        ("=" * right_padding) + \
        f'{Style.RESET_ALL}'

    divider()
    print(formatted_string)
    divider()


def print_formatted(message, formatting_string):
    """Print an message formatted to stand out."""
    formatted_string = formatting_string + message + f'{Style.RESET_ALL}'
    print(formatted_string)
