# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AttachmentIdentifiers(object):

    """Implementation of the 'AttachmentIdentifiers' model.

    TODO: type model description here.

    Attributes:
        file_name (str): This element contains file name of attched file
        id (str): Attachment file identifier.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_name": 'fileName',
        "id": 'id'
    }

    def __init__(self,
                 file_name=None,
                 id=None):
        """Constructor for the AttachmentIdentifiers class"""

        # Initialize members of the class
        self.file_name = file_name 
        self.id = id 

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
        id = dictionary.get("id") if dictionary.get("id") else None
        # Return an object of this model
        return cls(file_name,
                   id)
