# -*- coding: utf-8 -*-

"""
servicingmerchantcasemanagementapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from apimatic_core.utilities.file_helper import FileHelper
from servicingmerchantcasemanagementapi.api_helper import APIHelper
from servicingmerchantcasemanagementapi.models.create_case_request import CreateCaseRequest
from servicingmerchantcasemanagementapi.models.create_comment_request import CreateCommentRequest
from servicingmerchantcasemanagementapi.models.search_cases_request import SearchCasesRequest


class CaseControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(CaseControllerTests, cls).setUpClass()
        cls.controller = cls.client.case
        cls.response_catcher = cls.controller.http_call_back

    # Create a new case in service cloud
    def test_create_case(self):
        # Parameters for the API call
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.create_case(v_correlation_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 201

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Add comments for an existing service request case present with Worldpay.
    def test_update_case(self):
        # Parameters for the API call
        case_number = '12376567'
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'
        body = None

        # Perform the API call through the SDK function
        self.controller.update_case(case_number, v_correlation_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 201

    # Retrieve details for a specific service request case submitted with Worldpay.
    def test_get_case_details(self):
        # Parameters for the API call
        case_number = '11111234'
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

        # Perform the API call through the SDK function
        result = self.controller.get_case_details(case_number, v_correlation_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Search for service request cases  based on search parameters with Worldpay.
    def test_search_cases(self):
        # Parameters for the API call
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.search_cases(v_correlation_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Attach attachments for an existing service request case present with WorldPay.
    def test_create_attachments(self):
        # Parameters for the API call
        case_number = '12376567'
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'
        file = None

        # Perform the API call through the SDK function
        self.controller.create_attachments(case_number, v_correlation_id, file)

        # Test response code
        assert self.response_catcher.response.status_code == 201

    # Retrieve attachment of a case by attachment identifier with Worldpay.
    def test_get_attachments(self):
        # Parameters for the API call
        case_number = '14837'
        attachment_id = 'A1JXVGTYUIO'
        v_correlation_id = '24578e35-9bd2-238f-b4c2-0bc9ad9aed2b'

        # Perform the API call through the SDK function
        result = self.controller.get_attachments(case_number, attachment_id, v_correlation_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


