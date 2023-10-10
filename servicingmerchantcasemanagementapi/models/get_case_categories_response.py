# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper


class GetCaseCategoriesResponse(object):

    """Implementation of the 'GetCaseCategoriesResponse' model.

    List of case categories from WolrdPay will be returned in the response
    from WolrdPay

    Attributes:
        categories (List[str]): Case category list

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "categories": 'categories'
    }

    _optionals = [
        'categories',
    ]

    def __init__(self,
                 categories=APIHelper.SKIP):
        """Constructor for the GetCaseCategoriesResponse class"""

        # Initialize members of the class
        if categories is not APIHelper.SKIP:
            self.categories = categories 

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
        categories = dictionary.get("categories") if dictionary.get("categories") else APIHelper.SKIP
        # Return an object of this model
        return cls(categories)
