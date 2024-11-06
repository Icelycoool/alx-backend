#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """
    Calculates the start and end indices for pagination
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
