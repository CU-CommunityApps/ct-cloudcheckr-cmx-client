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
from cloudcheckr_cmx_client.api.account_management_api import AccountManagementApi  # noqa: E501
from cloudcheckr_cmx_client.rest import ApiException


class TestAccountManagementApi(unittest.TestCase):
    """AccountManagementApi unit test stubs"""

    def setUp(self):
        self.api = AccountManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_account_groups(self):
        """Test case for attach_account_groups

        Bulk move account groups into a parent account group.  # noqa: E501
        """
        pass

    def test_attach_account_groups_to_root(self):
        """Test case for attach_account_groups_to_root

        Bulk move account groups into the root path.  # noqa: E501
        """
        pass

    def test_create_account(self):
        """Test case for create_account

        Create a General Account.  # noqa: E501
        """
        pass

    def test_create_account_group(self):
        """Test case for create_account_group

        Create a new account group.  # noqa: E501
        """
        pass

    def test_create_mav(self):
        """Test case for create_mav

        Create a MAV.  # noqa: E501
        """
        pass

    def test_delete_account(self):
        """Test case for delete_account

        Delete a general account.  # noqa: E501
        """
        pass

    def test_delete_account_group(self):
        """Test case for delete_account_group

        Delete an account group  # noqa: E501
        """
        pass

    def test_delete_mav(self):
        """Test case for delete_mav

        Delete a MAV.  # noqa: E501
        """
        pass

    def test_get_account(self):
        """Test case for get_account

        Get an individual general account.  # noqa: E501
        """
        pass

    def test_get_account_group_parent_assignment(self):
        """Test case for get_account_group_parent_assignment

        Get an individual account group parent assignment.  # noqa: E501
        """
        pass

    def test_get_account_group_parent_assignments(self):
        """Test case for get_account_group_parent_assignments

        Get all account group parent assignments.  # noqa: E501
        """
        pass

    def test_get_general_accounts(self):
        """Test case for get_general_accounts

        Get all general accounts.  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get an individual account group.  # noqa: E501
        """
        pass

    def test_get_group_children(self):
        """Test case for get_group_children

        Get all children of an account group.  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Get all account groups.  # noqa: E501
        """
        pass

    def test_get_mav(self):
        """Test case for get_mav

        Get an individual MAV.  # noqa: E501
        """
        pass

    def test_get_mav_accounts(self):
        """Test case for get_mav_accounts

        Get all MAVs.  # noqa: E501
        """
        pass

    def test_get_mav_referenced_accounts(self):
        """Test case for get_mav_referenced_accounts

        Get accounts associated with a MAV.  # noqa: E501
        """
        pass

    def test_get_root_children(self):
        """Test case for get_root_children

        Get the root of the account hierarchy.  # noqa: E501
        """
        pass

    def test_update_account(self):
        """Test case for update_account

        Update a General Account.  # noqa: E501
        """
        pass

    def test_update_account_group(self):
        """Test case for update_account_group

        Update an account group.  # noqa: E501
        """
        pass

    def test_update_mav(self):
        """Test case for update_mav

        Update a MAV.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()