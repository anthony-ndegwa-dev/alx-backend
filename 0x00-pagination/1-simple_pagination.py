#!/usr/bin/env python3
"""Copy index_range from previous task and the following class into your code

import csv
import math
from typing import List


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass

Implement method get_page that takes two integer arguments page with default
value 1 and page_size with default value 10.

    Use this CSV file (same as the one presented at the top of the project)
    Use assert to verify that both arguments are integers greater than 0.
    Use index_range to find correct indexes to paginate dataset correctly and
    return appropriate page of the dataset (i.e. the correct list of rows).
    If input arguments are out of rang, an empty list should be returned.
"""
import csv
from typing import Tuple,  List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get index range from a given page and page size."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
