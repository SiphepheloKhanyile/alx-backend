#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Args:
        page (int): page
        page_size (int): page size
    Returns:
        tuple: start and end for given page
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
