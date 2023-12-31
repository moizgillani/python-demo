# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from servicingmerchantcasemanagementapi.api_helper import APIHelper


class GetAttachmentResponse(object):

    """Implementation of the 'GetAttachmentResponse' model.

    Retrive attachment files on a case. All attachments (file names with
    attachment ids) can be retrieved on a case by looking up the case
    details.

    Attributes:
        attachment_id (str): Attachment identifier for the file.
        file_name (str): This element contains file name of attachment.
        file_content (str): File content in the form of base64 or multipart
            file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_name": 'fileName',
        "file_content": 'fileContent',
        "attachment_id": 'attachmentId'
    }

    _optionals = [
        'attachment_id',
    ]

    def __init__(self,
                 file_name=None,
                 file_content=None,
                 attachment_id=APIHelper.SKIP):
        """Constructor for the GetAttachmentResponse class"""

        # Initialize members of the class
        if attachment_id is not APIHelper.SKIP:
            self.attachment_id = attachment_id 
        self.file_name = file_name 
        self.file_content = file_content 

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
        file_name = dictionary.get("fileName") if dictionary.get("fileName") else None
        file_content = dictionary.get("fileContent") if dictionary.get("fileContent") else None
        attachment_id = dictionary.get("attachmentId") if dictionary.get("attachmentId") else APIHelper.SKIP
        # Return an object of this model
        return cls(file_name,
                   file_content,
                   attachment_id)
