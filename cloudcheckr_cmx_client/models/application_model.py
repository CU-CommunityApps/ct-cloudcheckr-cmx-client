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

class ApplicationModel(object):
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
        'application_id': 'str',
        'application_secret': 'str'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'application_secret': 'applicationSecret'
    }

    def __init__(self, application_id=None, application_secret=None):  # noqa: E501
        """ApplicationModel - a model defined in Swagger"""  # noqa: E501
        self._application_id = None
        self._application_secret = None
        self.discriminator = None
        if application_id is not None:
            self.application_id = application_id
        if application_secret is not None:
            self.application_secret = application_secret

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationModel.  # noqa: E501

        Application's unique ID.  # noqa: E501

        :return: The application_id of this ApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationModel.

        Application's unique ID.  # noqa: E501

        :param application_id: The application_id of this ApplicationModel.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_secret(self):
        """Gets the application_secret of this ApplicationModel.  # noqa: E501

        Application's secret / password.  # noqa: E501

        :return: The application_secret of this ApplicationModel.  # noqa: E501
        :rtype: str
        """
        return self._application_secret

    @application_secret.setter
    def application_secret(self, application_secret):
        """Sets the application_secret of this ApplicationModel.

        Application's secret / password.  # noqa: E501

        :param application_secret: The application_secret of this ApplicationModel.  # noqa: E501
        :type: str
        """

        self._application_secret = application_secret

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
        if issubclass(ApplicationModel, dict):
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
        if not isinstance(other, ApplicationModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other