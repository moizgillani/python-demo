# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class CustomHeaderAuthentication(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in CustomHeaderAuthentication

        """
        return "CustomHeaderAuthentication: Authorization is undefined."

    def __init__(self, authorization):
        auth_params = {}
        if authorization:
            auth_params["Authorization"] = authorization
        super().__init__(auth_params=auth_params)
        self._authorization = authorization
