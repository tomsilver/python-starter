"""Data structures."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Dog:
    """An example class."""

    name: str
    breed: str

    def is_good(self) -> bool:
        """All dogs are good."""
        return True
