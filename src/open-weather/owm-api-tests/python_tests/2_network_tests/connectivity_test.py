#!/usr/bin/env python3
# ============================================================================
"""
owm-api-test.

A set of tests that check whether we can access the internet and API server
"""
# ============================================================================

import warnings
import subprocess


def test_ping_internet():
    """Test that internet connectivity is available."""
    command = ['ping', "google.com"]
    if (subprocess.call(command) == 1):
        warnings.warn("Cannot ping google. Looks like"
                      "you dont have an internet connection")


def test_ping_OWM():
    """Test OWM web server is not down"""
    command = ['ping', "openweathermap.org"]
    if (subprocess.call(command) == 1):
        warnings.warn("Cannot ping OWM. If internet connectivity is fine, "
                      "OWM server may be down")
