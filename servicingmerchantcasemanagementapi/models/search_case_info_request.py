# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper


class SearchCaseInfoRequest(object):

    """Implementation of the 'SearchCaseInfoRequest' model.

    Search parameters for searching the case.

    Attributes:
        case_number (str): Case number assigned to case
        category (str): Case category. High level grouping of case types
        case_type (str): Case type for selected category for the case
        status (StatusEnum): Case status
        priority (Priority1Enum): Defines time limit for case resolution

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "case_number": 'caseNumber',
        "category": 'category',
        "case_type": 'caseType',
        "status": 'status',
        "priority": 'priority'
    }

    _optionals = [
        'case_number',
        'category',
        'case_type',
        'status',
        'priority',
    ]

    def __init__(self,
                 case_number=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 case_type=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 priority=APIHelper.SKIP):
        """Constructor for the SearchCaseInfoRequest class"""

        # Initialize members of the class
        if case_number is not APIHelper.SKIP:
            self.case_number = case_number 
        if category is not APIHelper.SKIP:
            self.category = category 
        if case_type is not APIHelper.SKIP:
            self.case_type = case_type 
        if status is not APIHelper.SKIP:
            self.status = status 
        if priority is not APIHelper.SKIP:
            self.priority = priority 

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
        case_number = dictionary.get("caseNumber") if dictionary.get("caseNumber") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        case_type = dictionary.get("caseType") if dictionary.get("caseType") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        priority = dictionary.get("priority") if dictionary.get("priority") else APIHelper.SKIP
        # Return an object of this model
        return cls(case_number,
                   category,
                   case_type,
                   status,
                   priority)
