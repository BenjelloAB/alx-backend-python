#!/usr/bin/env python3
"""task 9"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length function"""
    return [(i, len(i)) for i in lst]
