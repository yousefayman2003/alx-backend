#!/usr/bin/env python3
"""Module that contains index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Returns a tuple of size two containing a start index and an end index

        Args:
            page (int): page number
            page_size (int): size of each page

        Returns:
            (tuple): start index, end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
