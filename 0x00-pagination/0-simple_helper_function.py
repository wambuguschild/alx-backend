#!/usr/bin/env python3
""" Indexing"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes (both inclusive).
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return (start_index, end_index)
