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

class RelatedPermissionModel(object):
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
        'impact': 'str',
        'notify_user': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'impact': 'impact',
        'notify_user': 'notifyUser'
    }

    def __init__(self, id=None, impact=None, notify_user=None):  # noqa: E501
        """RelatedPermissionModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._impact = None
        self._notify_user = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if impact is not None:
            self.impact = impact
        if notify_user is not None:
            self.notify_user = notify_user

    @property
    def id(self):
        """Gets the id of this RelatedPermissionModel.  # noqa: E501

        The related permission's ID.  # noqa: E501

        :return: The id of this RelatedPermissionModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelatedPermissionModel.

        The related permission's ID.  # noqa: E501

        :param id: The id of this RelatedPermissionModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def impact(self):
        """Gets the impact of this RelatedPermissionModel.  # noqa: E501

        The impact of the relationship. Example: The related Permission is included.  # noqa: E501

        :return: The impact of this RelatedPermissionModel.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this RelatedPermissionModel.

        The impact of the relationship. Example: The related Permission is included.  # noqa: E501

        :param impact: The impact of this RelatedPermissionModel.  # noqa: E501
        :type: str
        """

        self._impact = impact

    @property
    def notify_user(self):
        """Gets the notify_user of this RelatedPermissionModel.  # noqa: E501

        Controls whether or not the user should be notified that this related permission is impacted.  # noqa: E501

        :return: The notify_user of this RelatedPermissionModel.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this RelatedPermissionModel.

        Controls whether or not the user should be notified that this related permission is impacted.  # noqa: E501

        :param notify_user: The notify_user of this RelatedPermissionModel.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

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
        if issubclass(RelatedPermissionModel, dict):
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
        if not isinstance(other, RelatedPermissionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
