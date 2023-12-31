# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DateRangeSearch(object):

    """Implementation of the 'DateRangeSearch' model.

    Specify the date range for search. Consumer can lookup for 60 days data at
    a time. If you want more data divide your search into multiple windows.

    Attributes:
        from_date (str): specify start date for range.
        to_date (str): specify end date for range.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "from_date": 'fromDate',
        "to_date": 'toDate'
    }

    def __init__(self,
                 from_date=None,
                 to_date=None):
        """Constructor for the DateRangeSearch class"""

        # Initialize members of the class
        self.from_date = from_date 
        self.to_date = to_date 

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
        from_date = dictionary.get("fromDate") if dictionary.get("fromDate") else None
        to_date = dictionary.get("toDate") if dictionary.get("toDate") else None
        # Return an object of this model
        return cls(from_date,
                   to_date)
