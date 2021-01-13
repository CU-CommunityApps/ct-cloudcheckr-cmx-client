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
from cloudcheckr_cmx_client.api.account_attributes_api import AccountAttributesApi  # noqa: E501
from cloudcheckr_cmx_client.rest import ApiException


class TestAccountAttributesApi(unittest.TestCase):
    """AccountAttributesApi unit test stubs"""

    def setUp(self):
        self.api = AccountAttributesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_account_attribute(self):
        """Test case for attach_account_attribute

        Bulk associate account attribute name-value to list of general accounts.  # noqa: E501
        """
        pass

    def test_delete_account_attribute(self):
        """Test case for delete_account_attribute

        Delete an account attribute.  # noqa: E501
        """
        pass

    def test_get_account_attribute(self):
        """Test case for get_account_attribute

        Get an individual account attribute.  # noqa: E501
        """
        pass

    def test_list_account_attributes(self):
        """Test case for list_account_attributes

        Get all account attributes.  # noqa: E501
        """
        pass

    def test_update_account_attribute(self):
        """Test case for update_account_attribute

        Create/Update an account attribute.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
