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

class AccountAttributeResponseModel(object):
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
        'customer_id': 'str',
        'name': 'str',
        'values': 'list[str]',
        'value_count': 'int',
        'created_date': 'datetime',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'name': 'name',
        'values': 'values',
        'value_count': 'valueCount',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate'
    }

    def __init__(self, customer_id=None, name=None, values=None, value_count=None, created_date=None, updated_date=None):  # noqa: E501
        """AccountAttributeResponseModel - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._name = None
        self._values = None
        self._value_count = None
        self._created_date = None
        self._updated_date = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if name is not None:
            self.name = name
        if values is not None:
            self.values = values
        if value_count is not None:
            self.value_count = value_count
        if created_date is not None:
            self.created_date = created_date
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def customer_id(self):
        """Gets the customer_id of this AccountAttributeResponseModel.  # noqa: E501

        The customer's ID.  # noqa: E501

        :return: The customer_id of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AccountAttributeResponseModel.

        The customer's ID.  # noqa: E501

        :param customer_id: The customer_id of this AccountAttributeResponseModel.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this AccountAttributeResponseModel.  # noqa: E501

        The attribute name. This property supports: sorting and searching.  # noqa: E501

        :return: The name of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountAttributeResponseModel.

        The attribute name. This property supports: sorting and searching.  # noqa: E501

        :param name: The name of this AccountAttributeResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def values(self):
        """Gets the values of this AccountAttributeResponseModel.  # noqa: E501

        The attribute values. This property supports: searching.  # noqa: E501

        :return: The values of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AccountAttributeResponseModel.

        The attribute values. This property supports: searching.  # noqa: E501

        :param values: The values of this AccountAttributeResponseModel.  # noqa: E501
        :type: list[str]
        """

        self._values = values

    @property
    def value_count(self):
        """Gets the value_count of this AccountAttributeResponseModel.  # noqa: E501

        The total number of values within the attribute.  # noqa: E501

        :return: The value_count of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._value_count

    @value_count.setter
    def value_count(self, value_count):
        """Sets the value_count of this AccountAttributeResponseModel.

        The total number of values within the attribute.  # noqa: E501

        :param value_count: The value_count of this AccountAttributeResponseModel.  # noqa: E501
        :type: int
        """

        self._value_count = value_count

    @property
    def created_date(self):
        """Gets the created_date of this AccountAttributeResponseModel.  # noqa: E501

        The attribute's creation date.  # noqa: E501

        :return: The created_date of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this AccountAttributeResponseModel.

        The attribute's creation date.  # noqa: E501

        :param created_date: The created_date of this AccountAttributeResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this AccountAttributeResponseModel.  # noqa: E501

        The attribute's last updated date.  # noqa: E501

        :return: The updated_date of this AccountAttributeResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this AccountAttributeResponseModel.

        The attribute's last updated date.  # noqa: E501

        :param updated_date: The updated_date of this AccountAttributeResponseModel.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(AccountAttributeResponseModel, dict):
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
        if not isinstance(other, AccountAttributeResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
