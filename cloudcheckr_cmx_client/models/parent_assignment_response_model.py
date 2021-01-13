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

class ParentAssignmentResponseModel(object):
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
        'new_parent': 'str',
        'date_started': 'datetime',
        'date_requested': 'datetime',
        'date_last_activity': 'datetime',
        'date_completed': 'datetime',
        'error_message': 'str',
        'correlation_id': 'str',
        'target_account_group_id': 'str',
        'target_expected_parent': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'new_parent': 'newParent',
        'date_started': 'dateStarted',
        'date_requested': 'dateRequested',
        'date_last_activity': 'dateLastActivity',
        'date_completed': 'dateCompleted',
        'error_message': 'errorMessage',
        'correlation_id': 'correlationId',
        'target_account_group_id': 'targetAccountGroupId',
        'target_expected_parent': 'targetExpectedParent'
    }

    def __init__(self, id=None, state=None, new_parent=None, date_started=None, date_requested=None, date_last_activity=None, date_completed=None, error_message=None, correlation_id=None, target_account_group_id=None, target_expected_parent=None):  # noqa: E501
        """ParentAssignmentResponseModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._state = None
        self._new_parent = None
        self._date_started = None
        self._date_requested = None
        self._date_last_activity = None
        self._date_completed = None
        self._error_message = None
        self._correlation_id = None
        self._target_account_group_id = None
        self._target_expected_parent = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if new_parent is not None:
            self.new_parent = new_parent
        if date_started is not None:
            self.date_started = date_started
        if date_requested is not None:
            self.date_requested = date_requested
        if date_last_activity is not None:
            self.date_last_activity = date_last_activity
        if date_completed is not None:
            self.date_completed = date_completed
        if error_message is not None:
            self.error_message = error_message
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if target_account_group_id is not None:
            self.target_account_group_id = target_account_group_id
        if target_expected_parent is not None:
            self.target_expected_parent = target_expected_parent

    @property
    def id(self):
        """Gets the id of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's ID.  # noqa: E501

        :return: The id of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParentAssignmentResponseModel.

        The parent assignment's ID.  # noqa: E501

        :param id: The id of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's state.  # noqa: E501

        :return: The state of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ParentAssignmentResponseModel.

        The parent assignment's state.  # noqa: E501

        :param state: The state of this ParentAssignmentResponseModel.  # noqa: E501
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
        """Gets the new_parent of this ParentAssignmentResponseModel.  # noqa: E501

        The new parent's ID. Excluded if there is no parent.  # noqa: E501

        :return: The new_parent of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._new_parent

    @new_parent.setter
    def new_parent(self, new_parent):
        """Sets the new_parent of this ParentAssignmentResponseModel.

        The new parent's ID. Excluded if there is no parent.  # noqa: E501

        :param new_parent: The new_parent of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._new_parent = new_parent

    @property
    def date_started(self):
        """Gets the date_started of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's start date.  # noqa: E501

        :return: The date_started of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_started

    @date_started.setter
    def date_started(self, date_started):
        """Sets the date_started of this ParentAssignmentResponseModel.

        The parent assignment's start date.  # noqa: E501

        :param date_started: The date_started of this ParentAssignmentResponseModel.  # noqa: E501
        :type: datetime
        """

        self._date_started = date_started

    @property
    def date_requested(self):
        """Gets the date_requested of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's request date.  # noqa: E501

        :return: The date_requested of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_requested

    @date_requested.setter
    def date_requested(self, date_requested):
        """Sets the date_requested of this ParentAssignmentResponseModel.

        The parent assignment's request date.  # noqa: E501

        :param date_requested: The date_requested of this ParentAssignmentResponseModel.  # noqa: E501
        :type: datetime
        """

        self._date_requested = date_requested

    @property
    def date_last_activity(self):
        """Gets the date_last_activity of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's last updated date.  # noqa: E501

        :return: The date_last_activity of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_activity

    @date_last_activity.setter
    def date_last_activity(self, date_last_activity):
        """Sets the date_last_activity of this ParentAssignmentResponseModel.

        The parent assignment's last updated date.  # noqa: E501

        :param date_last_activity: The date_last_activity of this ParentAssignmentResponseModel.  # noqa: E501
        :type: datetime
        """

        self._date_last_activity = date_last_activity

    @property
    def date_completed(self):
        """Gets the date_completed of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's completion date.  # noqa: E501

        :return: The date_completed of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_completed

    @date_completed.setter
    def date_completed(self, date_completed):
        """Sets the date_completed of this ParentAssignmentResponseModel.

        The parent assignment's completion date.  # noqa: E501

        :param date_completed: The date_completed of this ParentAssignmentResponseModel.  # noqa: E501
        :type: datetime
        """

        self._date_completed = date_completed

    @property
    def error_message(self):
        """Gets the error_message of this ParentAssignmentResponseModel.  # noqa: E501

        The error message if parent movement was unsuccessful.  # noqa: E501

        :return: The error_message of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ParentAssignmentResponseModel.

        The error message if parent movement was unsuccessful.  # noqa: E501

        :param error_message: The error_message of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ParentAssignmentResponseModel.  # noqa: E501

        The request's correlation ID.  # noqa: E501

        :return: The correlation_id of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ParentAssignmentResponseModel.

        The request's correlation ID.  # noqa: E501

        :param correlation_id: The correlation_id of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def target_account_group_id(self):
        """Gets the target_account_group_id of this ParentAssignmentResponseModel.  # noqa: E501

        The parent assignment's target account group.  # noqa: E501

        :return: The target_account_group_id of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._target_account_group_id

    @target_account_group_id.setter
    def target_account_group_id(self, target_account_group_id):
        """Sets the target_account_group_id of this ParentAssignmentResponseModel.

        The parent assignment's target account group.  # noqa: E501

        :param target_account_group_id: The target_account_group_id of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._target_account_group_id = target_account_group_id

    @property
    def target_expected_parent(self):
        """Gets the target_expected_parent of this ParentAssignmentResponseModel.  # noqa: E501

        The expected parent ID when the assignment is completed.  # noqa: E501

        :return: The target_expected_parent of this ParentAssignmentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._target_expected_parent

    @target_expected_parent.setter
    def target_expected_parent(self, target_expected_parent):
        """Sets the target_expected_parent of this ParentAssignmentResponseModel.

        The expected parent ID when the assignment is completed.  # noqa: E501

        :param target_expected_parent: The target_expected_parent of this ParentAssignmentResponseModel.  # noqa: E501
        :type: str
        """

        self._target_expected_parent = target_expected_parent

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
        if issubclass(ParentAssignmentResponseModel, dict):
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
        if not isinstance(other, ParentAssignmentResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other