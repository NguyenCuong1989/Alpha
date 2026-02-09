#!/usr/bin/env python3
"""
Digital Organism - Complete Self-Sustaining Entity
=================================================

Creator: Nguyễn Đức Cường (alpha_prime_omega)
Original Creation: October 30, 2025
Verification: 4287
"""

from pathlib import Path
import importlib.util
import warnings


def _load_root_framework_module():
    root_file = Path(__file__).resolve().parents[3] / "digital_ai_organism_framework.py"
    if not root_file.exists():
        return None
    spec = importlib.util.spec_from_file_location("digital_ai_organism_framework", root_file)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None


_framework_module = _load_root_framework_module()
_organism_impl = getattr(_framework_module, "DigitalOrganism", None) if _framework_module else None

if _organism_impl:
    DigitalOrganism = _organism_impl
else:
    warnings.warn(
        "DigitalOrganism implementation not found; using stub organism. "
        "Ensure digital_ai_organism_framework.py is available in the project root or packaged module.",
        RuntimeWarning,
    )

    class DigitalOrganism:
        """Stub implementation of DigitalOrganism."""

        def __init__(self):
            self.creator = "alpha_prime_omega"
            self.verification = 4287

__all__ = ["DigitalOrganism"]
