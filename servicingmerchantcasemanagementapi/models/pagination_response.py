# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper
from servicingmerchantcasemanagementapi.models.pagination_type import PaginationType


class PaginationResponse(object):

    """Implementation of the 'PaginationResponse' model.

    TODO: type model description here.

    Attributes:
        pagination (PaginationType): Pagination type details
        more_data_available (str): Indicates if more data is available for the
            search criteria
        total_row_count (int): Total number of rows available for the search
            results
        total_returned_count (int): Number of rows returned

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pagination": 'pagination',
        "more_data_available": 'moreDataAvailable',
        "total_row_count": 'totalRowCount',
        "total_returned_count": 'totalReturnedCount'
    }

    _optionals = [
        'pagination',
        'more_data_available',
        'total_row_count',
        'total_returned_count',
    ]

    def __init__(self,
                 pagination=APIHelper.SKIP,
                 more_data_available=APIHelper.SKIP,
                 total_row_count=APIHelper.SKIP,
                 total_returned_count=APIHelper.SKIP):
        """Constructor for the PaginationResponse class"""

        # Initialize members of the class
        if pagination is not APIHelper.SKIP:
            self.pagination = pagination 
        if more_data_available is not APIHelper.SKIP:
            self.more_data_available = more_data_available 
        if total_row_count is not APIHelper.SKIP:
            self.total_row_count = total_row_count 
        if total_returned_count is not APIHelper.SKIP:
            self.total_returned_count = total_returned_count 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        pagination = PaginationType.from_dictionary(dictionary.get('pagination')) if 'pagination' in dictionary.keys() else APIHelper.SKIP
        more_data_available = dictionary.get("moreDataAvailable") if dictionary.get("moreDataAvailable") else APIHelper.SKIP
        total_row_count = dictionary.get("totalRowCount") if dictionary.get("totalRowCount") else APIHelper.SKIP
        total_returned_count = dictionary.get("totalReturnedCount") if dictionary.get("totalReturnedCount") else APIHelper.SKIP
        # Return an object of this model
        return cls(pagination,
                   more_data_available,
                   total_row_count,
                   total_returned_count)
