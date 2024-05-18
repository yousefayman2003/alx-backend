#!/usr/bin/env python3
"""Module that implements Hypermedia pagination"""
import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets data for a page"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)

        dataset = self.dataset()
        if start_index > len(self.__dataset) or \
                end_index > len(self.__dataset):
            return []

        return self.__dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Implements hypermedia pagination

            Args:
                page (int): page number
                page_size (int): size of each page

            Returns:
                dictionary containing the following key-value pairs

                page_size: the length of the returned dataset page
                page: the current page number
                data: the dataset page
                next_page: number of the next page,
                            None if no next page
                prev_page: number of the previous page,
                            None if no previous page
                total_pages: the total number of pages
                            in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
