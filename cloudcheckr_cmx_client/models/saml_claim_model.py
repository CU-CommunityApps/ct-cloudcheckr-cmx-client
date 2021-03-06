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

class SamlClaimModel(object):
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
        'attribute_name': 'str',
        'attribute_value': 'str',
        'case_sensitive_value': 'bool'
    }

    attribute_map = {
        'attribute_name': 'attributeName',
        'attribute_value': 'attributeValue',
        'case_sensitive_value': 'caseSensitiveValue'
    }

    def __init__(self, attribute_name=None, attribute_value=None, case_sensitive_value=None):  # noqa: E501
        """SamlClaimModel - a model defined in Swagger"""  # noqa: E501
        self._attribute_name = None
        self._attribute_value = None
        self._case_sensitive_value = None
        self.discriminator = None
        if attribute_name is not None:
            self.attribute_name = attribute_name
        if attribute_value is not None:
            self.attribute_value = attribute_value
        if case_sensitive_value is not None:
            self.case_sensitive_value = case_sensitive_value

    @property
    def attribute_name(self):
        """Gets the attribute_name of this SamlClaimModel.  # noqa: E501

        The SAML attribute name.  # noqa: E501

        :return: The attribute_name of this SamlClaimModel.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this SamlClaimModel.

        The SAML attribute name.  # noqa: E501

        :param attribute_name: The attribute_name of this SamlClaimModel.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def attribute_value(self):
        """Gets the attribute_value of this SamlClaimModel.  # noqa: E501

        The SAML attribute value.  # noqa: E501

        :return: The attribute_value of this SamlClaimModel.  # noqa: E501
        :rtype: str
        """
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, attribute_value):
        """Sets the attribute_value of this SamlClaimModel.

        The SAML attribute value.  # noqa: E501

        :param attribute_value: The attribute_value of this SamlClaimModel.  # noqa: E501
        :type: str
        """

        self._attribute_value = attribute_value

    @property
    def case_sensitive_value(self):
        """Gets the case_sensitive_value of this SamlClaimModel.  # noqa: E501

        True if the attribute name and value are case sensitive.  # noqa: E501

        :return: The case_sensitive_value of this SamlClaimModel.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive_value

    @case_sensitive_value.setter
    def case_sensitive_value(self, case_sensitive_value):
        """Sets the case_sensitive_value of this SamlClaimModel.

        True if the attribute name and value are case sensitive.  # noqa: E501

        :param case_sensitive_value: The case_sensitive_value of this SamlClaimModel.  # noqa: E501
        :type: bool
        """

        self._case_sensitive_value = case_sensitive_value

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
        if issubclass(SamlClaimModel, dict):
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
        if not isinstance(other, SamlClaimModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
