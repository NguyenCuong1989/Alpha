#!/usr/bin/env python3
"""
HAIOS Runtime - Runtime Environment for Digital Organisms
========================================================

Creator: Nguyễn Đức Cường (alpha_prime_omega)
Original Creation: October 30, 2025
Verification: 4287
"""

# Import from package implementation
try:
    from hyperai.haios_runtime import HAIOSRuntime as HAIOSRuntimeImpl

    HAIOSRuntime = HAIOSRuntimeImpl
except ImportError:
    # If haios_runtime doesn't exist, provide a stub
    class HAIOSRuntime:
        """Stub implementation of HAIOSRuntime"""

        def __init__(self):
            self.version = "1.0.0"
            self.creator = "alpha_prime_omega"


__all__ = ["HAIOSRuntime"]
