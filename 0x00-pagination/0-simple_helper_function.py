#!/usr/bin/env python3
""" Task 0 Module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
Return the start and end indices for a given page and page size.

Parameters:
- page (int): The page number.
- page_size (int): The number of items per page.

Returns:
- tuple[int, int]: A tuple containing the start and end indices
for the given page.
"""
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)
