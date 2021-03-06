# coding: utf-8

"""
    CloudCheckr API

    CloudCheckr API  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@cloudcheckr.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AwsCredentialRequestModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region_group': 'str',
        'access_key': 'AwsAccessKeyModel',
        'cross_account_role': 'AwsCrossAccountRoleModel',
        'linked_aws_commercial_account': 'LinkedAwsCommercialAccountModel'
    }

    attribute_map = {
        'region_group': 'regionGroup',
        'access_key': 'accessKey',
        'cross_account_role': 'crossAccountRole',
        'linked_aws_commercial_account': 'linkedAwsCommercialAccount'
    }

    def __init__(self, region_group=None, access_key=None, cross_account_role=None, linked_aws_commercial_account=None):  # noqa: E501
        """AwsCredentialRequestModel - a model defined in Swagger"""  # noqa: E501
        self._region_group = None
        self._access_key = None
        self._cross_account_role = None
        self._linked_aws_commercial_account = None
        self.discriminator = None
        if region_group is not None:
            self.region_group = region_group
        if access_key is not None:
            self.access_key = access_key
        if cross_account_role is not None:
            self.cross_account_role = cross_account_role
        if linked_aws_commercial_account is not None:
            self.linked_aws_commercial_account = linked_aws_commercial_account

    @property
    def region_group(self):
        """Gets the region_group of this AwsCredentialRequestModel.  # noqa: E501

        The account's region group (i.e. the unique data center group that is being used, e.g. commercial, GovCloud, etc).  # noqa: E501

        :return: The region_group of this AwsCredentialRequestModel.  # noqa: E501
        :rtype: str
        """
        return self._region_group

    @region_group.setter
    def region_group(self, region_group):
        """Sets the region_group of this AwsCredentialRequestModel.

        The account's region group (i.e. the unique data center group that is being used, e.g. commercial, GovCloud, etc).  # noqa: E501

        :param region_group: The region_group of this AwsCredentialRequestModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Commercial", "GovUs"]  # noqa: E501
        if region_group not in allowed_values:
            raise ValueError(
                "Invalid value for `region_group` ({0}), must be one of {1}"  # noqa: E501
                .format(region_group, allowed_values)
            )

        self._region_group = region_group

    @property
    def access_key(self):
        """Gets the access_key of this AwsCredentialRequestModel.  # noqa: E501


        :return: The access_key of this AwsCredentialRequestModel.  # noqa: E501
        :rtype: AwsAccessKeyModel
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsCredentialRequestModel.


        :param access_key: The access_key of this AwsCredentialRequestModel.  # noqa: E501
        :type: AwsAccessKeyModel
        """

        self._access_key = access_key

    @property
    def cross_account_role(self):
        """Gets the cross_account_role of this AwsCredentialRequestModel.  # noqa: E501


        :return: The cross_account_role of this AwsCredentialRequestModel.  # noqa: E501
        :rtype: AwsCrossAccountRoleModel
        """
        return self._cross_account_role

    @cross_account_role.setter
    def cross_account_role(self, cross_account_role):
        """Sets the cross_account_role of this AwsCredentialRequestModel.


        :param cross_account_role: The cross_account_role of this AwsCredentialRequestModel.  # noqa: E501
        :type: AwsCrossAccountRoleModel
        """

        self._cross_account_role = cross_account_role

    @property
    def linked_aws_commercial_account(self):
        """Gets the linked_aws_commercial_account of this AwsCredentialRequestModel.  # noqa: E501


        :return: The linked_aws_commercial_account of this AwsCredentialRequestModel.  # noqa: E501
        :rtype: LinkedAwsCommercialAccountModel
        """
        return self._linked_aws_commercial_account

    @linked_aws_commercial_account.setter
    def linked_aws_commercial_account(self, linked_aws_commercial_account):
        """Sets the linked_aws_commercial_account of this AwsCredentialRequestModel.


        :param linked_aws_commercial_account: The linked_aws_commercial_account of this AwsCredentialRequestModel.  # noqa: E501
        :type: LinkedAwsCommercialAccountModel
        """

        self._linked_aws_commercial_account = linked_aws_commercial_account

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AwsCredentialRequestModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AwsCredentialRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
