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

class ClientResponseModel(object):
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
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'roles': 'list[MappedRoleResponseModel]',
        'access_key_count': 'int',
        'created_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'roles': 'roles',
        'access_key_count': 'accessKeyCount',
        'created_date': 'createdDate'
    }

    def __init__(self, id=None, name=None, description=None, type=None, roles=None, access_key_count=None, created_date=None):  # noqa: E501
        """ClientResponseModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._roles = None
        self._access_key_count = None
        self._created_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if roles is not None:
            self.roles = roles
        if access_key_count is not None:
            self.access_key_count = access_key_count
        if created_date is not None:
            self.created_date = created_date

    @property
    def id(self):
        """Gets the id of this ClientResponseModel.  # noqa: E501

        The client's unique ID. This property supports: searching.  # noqa: E501

        :return: The id of this ClientResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientResponseModel.

        The client's unique ID. This property supports: searching.  # noqa: E501

        :param id: The id of this ClientResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClientResponseModel.  # noqa: E501

        The client's name. This property supports: sorting, filtering and searching.  # noqa: E501

        :return: The name of this ClientResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientResponseModel.

        The client's name. This property supports: sorting, filtering and searching.  # noqa: E501

        :param name: The name of this ClientResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ClientResponseModel.  # noqa: E501

        The client's description. This property supports: sorting, filtering and searching.  # noqa: E501

        :return: The description of this ClientResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClientResponseModel.

        The client's description. This property supports: sorting, filtering and searching.  # noqa: E501

        :param description: The description of this ClientResponseModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this ClientResponseModel.  # noqa: E501

        The client's type. This property supports: sorting.  # noqa: E501

        :return: The type of this ClientResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientResponseModel.

        The client's type. This property supports: sorting.  # noqa: E501

        :param type: The type of this ClientResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Service"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def roles(self):
        """Gets the roles of this ClientResponseModel.  # noqa: E501

        The roles that are assigned to the client.  # noqa: E501

        :return: The roles of this ClientResponseModel.  # noqa: E501
        :rtype: list[MappedRoleResponseModel]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ClientResponseModel.

        The roles that are assigned to the client.  # noqa: E501

        :param roles: The roles of this ClientResponseModel.  # noqa: E501
        :type: list[MappedRoleResponseModel]
        """

        self._roles = roles

    @property
    def access_key_count(self):
        """Gets the access_key_count of this ClientResponseModel.  # noqa: E501

        The number of access keys belonging to the client. This property supports: sorting and filtering.  # noqa: E501

        :return: The access_key_count of this ClientResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._access_key_count

    @access_key_count.setter
    def access_key_count(self, access_key_count):
        """Sets the access_key_count of this ClientResponseModel.

        The number of access keys belonging to the client. This property supports: sorting and filtering.  # noqa: E501

        :param access_key_count: The access_key_count of this ClientResponseModel.  # noqa: E501
        :type: int
        """

        self._access_key_count = access_key_count

    @property
    def created_date(self):
        """Gets the created_date of this ClientResponseModel.  # noqa: E501

        The date that the client was created. This property supports: sorting and filtering.  # noqa: E501

        :return: The created_date of this ClientResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ClientResponseModel.

        The date that the client was created. This property supports: sorting and filtering.  # noqa: E501

        :param created_date: The created_date of this ClientResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

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
        if issubclass(ClientResponseModel, dict):
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
        if not isinstance(other, ClientResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other