# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cloudcheckr_cmx_client
from cloudcheckr_cmx_client.api.azure_common_credentials_api import AzureCommonCredentialsApi  # noqa: E501
from cloudcheckr_cmx_client.rest import ApiException


class TestAzureCommonCredentialsApi(unittest.TestCase):
    """AzureCommonCredentialsApi unit test stubs"""

    def setUp(self):
        self.api = AzureCommonCredentialsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_billing_account(self):
        """Test case for assign_billing_account

        Assigns a billing account ID to an Azure credential.  # noqa: E501
        """
        pass

    def test_get_billing_accounts(self):
        """Test case for get_billing_accounts

        Retrieve billing accounts associated with credential.  # noqa: E501
        """
        pass

    def test_request_authorization(self):
        """Test case for request_authorization

        Start the Azure authorization consent flow.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
