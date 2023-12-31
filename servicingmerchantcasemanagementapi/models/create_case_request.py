# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper
from servicingmerchantcasemanagementapi.models.attachment import Attachment
from servicingmerchantcasemanagementapi.models.caller_info import CallerInfo
from servicingmerchantcasemanagementapi.models.case_info import CaseInfo
from servicingmerchantcasemanagementapi.models.entity_info import EntityInfo


class CreateCaseRequest(object):

    """Implementation of the 'CreateCaseRequest' model.

    TODO: type model description here.

    Attributes:
        entity_info (EntityInfo): Entity information details
        caller_info (CallerInfo): Caller information details
        case_info (CaseInfo): Case information details
        attachments (List[Attachment]): Attachment file names

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "entity_info": 'entityInfo',
        "caller_info": 'callerInfo',
        "case_info": 'caseInfo',
        "attachments": 'attachments'
    }

    _optionals = [
        'attachments',
    ]

    def __init__(self,
                 entity_info=None,
                 caller_info=None,
                 case_info=None,
                 attachments=APIHelper.SKIP):
        """Constructor for the CreateCaseRequest class"""

        # Initialize members of the class
        self.entity_info = entity_info 
        self.caller_info = caller_info 
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
        entity_info = EntityInfo.from_dictionary(dictionary.get('entityInfo')) if dictionary.get('entityInfo') else None
        caller_info = CallerInfo.from_dictionary(dictionary.get('callerInfo')) if dictionary.get('callerInfo') else None
        case_info = CaseInfo.from_dictionary(dictionary.get('caseInfo')) if dictionary.get('caseInfo') else None
        attachments = None
        if dictionary.get('attachments') is not None:
            attachments = [Attachment.from_dictionary(x) for x in dictionary.get('attachments')]
        else:
            attachments = APIHelper.SKIP
        # Return an object of this model
        return cls(entity_info,
                   caller_info,
                   case_info,
                   attachments)
