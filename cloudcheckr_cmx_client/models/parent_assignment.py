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

class ParentAssignment(object):
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
        'id': 'str',
        'state': 'str',
        'new_parent': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'new_parent': 'newParent'
    }

    def __init__(self, id=None, state=None, new_parent=None):  # noqa: E501
        """ParentAssignment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._state = None
        self._new_parent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if new_parent is not None:
            self.new_parent = new_parent

    @property
    def id(self):
        """Gets the id of this ParentAssignment.  # noqa: E501

        The parent assignment's ID.  # noqa: E501

        :return: The id of this ParentAssignment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParentAssignment.

        The parent assignment's ID.  # noqa: E501

        :param id: The id of this ParentAssignment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ParentAssignment.  # noqa: E501

        The parent assignment's state.  # noqa: E501

        :return: The state of this ParentAssignment.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ParentAssignment.

        The parent assignment's state.  # noqa: E501

        :param state: The state of this ParentAssignment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "InProgress", "Completed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def new_parent(self):
        """Gets the new_parent of this ParentAssignment.  # noqa: E501

        The new parent's ID. Excluded if there is no parent.  # noqa: E501

        :return: The new_parent of this ParentAssignment.  # noqa: E501
        :rtype: str
        """
        return self._new_parent

    @new_parent.setter
    def new_parent(self, new_parent):
        """Sets the new_parent of this ParentAssignment.

        The new parent's ID. Excluded if there is no parent.  # noqa: E501

        :param new_parent: The new_parent of this ParentAssignment.  # noqa: E501
        :type: str
        """

        self._new_parent = new_parent

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
        if issubclass(ParentAssignment, dict):
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
        if not isinstance(other, ParentAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other