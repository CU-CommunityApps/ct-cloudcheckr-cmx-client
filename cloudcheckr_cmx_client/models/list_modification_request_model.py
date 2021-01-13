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

class ListModificationRequestModel(object):
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
        'modifications': 'list[BasicRequestListModification]'
    }

    attribute_map = {
        'modifications': 'modifications'
    }

    def __init__(self, modifications=None):  # noqa: E501
        """ListModificationRequestModel - a model defined in Swagger"""  # noqa: E501
        self._modifications = None
        self.discriminator = None
        if modifications is not None:
            self.modifications = modifications

    @property
    def modifications(self):
        """Gets the modifications of this ListModificationRequestModel.  # noqa: E501

        The requested modifications for a resource.  # noqa: E501

        :return: The modifications of this ListModificationRequestModel.  # noqa: E501
        :rtype: list[BasicRequestListModification]
        """
        return self._modifications

    @modifications.setter
    def modifications(self, modifications):
        """Sets the modifications of this ListModificationRequestModel.

        The requested modifications for a resource.  # noqa: E501

        :param modifications: The modifications of this ListModificationRequestModel.  # noqa: E501
        :type: list[BasicRequestListModification]
        """

        self._modifications = modifications

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
        if issubclass(ListModificationRequestModel, dict):
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
        if not isinstance(other, ListModificationRequestModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
