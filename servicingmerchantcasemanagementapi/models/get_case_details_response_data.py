# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper
from servicingmerchantcasemanagementapi.models.additional_case_details import AdditionalCaseDetails
from servicingmerchantcasemanagementapi.models.attachment_identifiers import AttachmentIdentifiers
from servicingmerchantcasemanagementapi.models.caller_info import CallerInfo
from servicingmerchantcasemanagementapi.models.hierarchy import Hierarchy


class GetCaseDetailsResponseData(object):

    """Implementation of the 'GetCaseDetailsResponseData' model.

    TODO: type model description here.

    Attributes:
        hierarchy (Hierarchy): Hierarchy details
        caller_info (CallerInfo): Caller information
        case_info (AdditionalCaseDetails): Case information
        attachments (List[AttachmentIdentifiers]): Attachments details

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hierarchy": 'hierarchy',
        "caller_info": 'callerInfo',
        "case_info": 'caseInfo',
        "attachments": 'attachments'
    }

    _optionals = [
        'hierarchy',
        'caller_info',
        'case_info',
        'attachments',
    ]

    def __init__(self,
                 hierarchy=APIHelper.SKIP,
                 caller_info=APIHelper.SKIP,
                 case_info=APIHelper.SKIP,
                 attachments=APIHelper.SKIP):
        """Constructor for the GetCaseDetailsResponseData class"""

        # Initialize members of the class
        if hierarchy is not APIHelper.SKIP:
            self.hierarchy = hierarchy 
        if caller_info is not APIHelper.SKIP:
            self.caller_info = caller_info 
        if case_info is not APIHelper.SKIP:
            self.case_info = case_info 
        if attachments is not APIHelper.SKIP:
            self.attachments = attachments 

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
        hierarchy = Hierarchy.from_dictionary(dictionary.get('hierarchy')) if 'hierarchy' in dictionary.keys() else APIHelper.SKIP
        caller_info = CallerInfo.from_dictionary(dictionary.get('callerInfo')) if 'callerInfo' in dictionary.keys() else APIHelper.SKIP
        case_info = AdditionalCaseDetails.from_dictionary(dictionary.get('caseInfo')) if 'caseInfo' in dictionary.keys() else APIHelper.SKIP
        attachments = None
        if dictionary.get('attachments') is not None:
            attachments = [AttachmentIdentifiers.from_dictionary(x) for x in dictionary.get('attachments')]
        else:
            attachments = APIHelper.SKIP
        # Return an object of this model
        return cls(hierarchy,
                   caller_info,
                   case_info,
                   attachments)
