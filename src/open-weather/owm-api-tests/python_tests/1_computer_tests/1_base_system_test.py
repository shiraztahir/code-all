#!/usr/bin/env python3
# ============================================================================
"""
owm-api-test.

A set of tests that are run first to establish the very base system is
set up correctly. Include more tests here
"""
# ============================================================================

import warnings
import psutil


def test_system_drive_free_space():
    """Test that there is plenty of free space on the system drive."""
    drive_usage = psutil.disk_usage('/')
    assert drive_usage.percent < 80, "System drive is over 80% full, please "\
        "be aware that this could cause issues!"
    if drive_usage.percent > 60:
        warnings.warn("System drive is over 60% full. This could cause"
                      " issues in a bit")
