"""Utilities."""

from typing import Set

from python_starter.structs import Dog


def get_good_dogs_of_breed(dogs: Set[Dog], breed: str) -> Set:
    """Get all good dogs of the specified breed."""
    return {d for d in dogs if d.is_good() and d.breed == breed}
