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
from cloudcheckr_cmx_client.api.google_credentials_api import GoogleCredentialsApi  # noqa: E501
from cloudcheckr_cmx_client.rest import ApiException


class TestGoogleCredentialsApi(unittest.TestCase):
    """GoogleCredentialsApi unit test stubs"""

    def setUp(self):
        self.api = GoogleCredentialsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_modify_google_credential(self):
        """Test case for modify_google_credential

        Modify the default credential on the account.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
