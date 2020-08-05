#!/usr/bin/env python3
# ============================================================================
"""
owm-api-test.

Conftest file. This sets the configuration of the pytest suite
"""
# ============================================================================


def pytest_report_header(config):
    """Print a line to be included in the pytest report header."""
    return "OWM-API-Tests"
