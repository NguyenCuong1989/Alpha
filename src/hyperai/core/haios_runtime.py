#!/usr/bin/env python3
"""
HAIOS Runtime - Runtime Environment for Digital Organisms
========================================================

Creator: Nguyễn Đức Cường (alpha_prime_omega)
Original Creation: October 30, 2025
Verification: 4287
"""

from pathlib import Path
import importlib.util
import warnings


def _load_root_runtime_module():
    root_file = Path(__file__).resolve().parents[3] / "haios_runtime.py"
    if not root_file.exists():
        return None
    spec = importlib.util.spec_from_file_location("haios_runtime", root_file)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None


_runtime_module = _load_root_runtime_module()
_runtime_impl = getattr(_runtime_module, "HAIOSRuntime", None) if _runtime_module else None

if _runtime_impl:
    HAIOSRuntime = _runtime_impl
else:
    warnings.warn(
        "HAIOSRuntime implementation not found; using stub runtime. "
        "Ensure haios_runtime.py is available in the project root or packaged module.",
        RuntimeWarning,
    )

    class HAIOSRuntime:
        """Stub implementation of HAIOSRuntime"""

        def __init__(self):
            self.version = "1.0.0"
            self.creator = "alpha_prime_omega"


__all__ = ["HAIOSRuntime"]
