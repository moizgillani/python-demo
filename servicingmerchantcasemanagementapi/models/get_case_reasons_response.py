# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper


class GetCaseReasonsResponse(object):

    """Implementation of the 'GetCaseReasonsResponse' model.

    List of case reasons for Merchant Operatins will be returned in the
    response from WolrdPay

    Attributes:
        reasons (List[str]): Case reasons

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reasons": 'reasons'
    }

    _optionals = [
        'reasons',
    ]

    def __init__(self,
                 reasons=APIHelper.SKIP):
        """Constructor for the GetCaseReasonsResponse class"""

        # Initialize members of the class
        if reasons is not APIHelper.SKIP:
            self.reasons = reasons 

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
        reasons = dictionary.get("reasons") if dictionary.get("reasons") else APIHelper.SKIP
        # Return an object of this model
        return cls(reasons)
