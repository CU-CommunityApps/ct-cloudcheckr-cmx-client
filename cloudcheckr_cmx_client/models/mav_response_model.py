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

class MavResponseModel(object):
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
        'legacy_account_id': 'str',
        'provider_identifier': 'str',
        'provider_sub_type': 'str',
        'provider_payment_type': 'str',
        'payer_identifier': 'str',
        'include_all_accounts': 'bool',
        'associated_account_attributes': 'list[AccountAttributeBasicInfo]',
        'type': 'str',
        'provider': 'str',
        'created_date': 'datetime',
        'has_pending_change': 'bool',
        'is_system_managed': 'bool',
        'credential_verification_status': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'legacy_account_id': 'legacyAccountId',
        'provider_identifier': 'providerIdentifier',
        'provider_sub_type': 'providerSubType',
        'provider_payment_type': 'providerPaymentType',
        'payer_identifier': 'payerIdentifier',
        'include_all_accounts': 'includeAllAccounts',
        'associated_account_attributes': 'associatedAccountAttributes',
        'type': 'type',
        'provider': 'provider',
        'created_date': 'createdDate',
        'has_pending_change': 'hasPendingChange',
        'is_system_managed': 'isSystemManaged',
        'credential_verification_status': 'credentialVerificationStatus',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, legacy_account_id=None, provider_identifier=None, provider_sub_type=None, provider_payment_type=None, payer_identifier=None, include_all_accounts=None, associated_account_attributes=None, type=None, provider=None, created_date=None, has_pending_change=None, is_system_managed=None, credential_verification_status=None, id=None, name=None):  # noqa: E501
        """MavResponseModel - a model defined in Swagger"""  # noqa: E501
        self._legacy_account_id = None
        self._provider_identifier = None
        self._provider_sub_type = None
        self._provider_payment_type = None
        self._payer_identifier = None
        self._include_all_accounts = None
        self._associated_account_attributes = None
        self._type = None
        self._provider = None
        self._created_date = None
        self._has_pending_change = None
        self._is_system_managed = None
        self._credential_verification_status = None
        self._id = None
        self._name = None
        self.discriminator = None
        if legacy_account_id is not None:
            self.legacy_account_id = legacy_account_id
        if provider_identifier is not None:
            self.provider_identifier = provider_identifier
        if provider_sub_type is not None:
            self.provider_sub_type = provider_sub_type
        if provider_payment_type is not None:
            self.provider_payment_type = provider_payment_type
        if payer_identifier is not None:
            self.payer_identifier = payer_identifier
        if include_all_accounts is not None:
            self.include_all_accounts = include_all_accounts
        if associated_account_attributes is not None:
            self.associated_account_attributes = associated_account_attributes
        if type is not None:
            self.type = type
        if provider is not None:
            self.provider = provider
        if created_date is not None:
            self.created_date = created_date
        if has_pending_change is not None:
            self.has_pending_change = has_pending_change
        if is_system_managed is not None:
            self.is_system_managed = is_system_managed
        if credential_verification_status is not None:
            self.credential_verification_status = credential_verification_status
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def legacy_account_id(self):
        """Gets the legacy_account_id of this MavResponseModel.  # noqa: E501

        The legacy account's ID. This property supports: searching.  # noqa: E501

        :return: The legacy_account_id of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._legacy_account_id

    @legacy_account_id.setter
    def legacy_account_id(self, legacy_account_id):
        """Sets the legacy_account_id of this MavResponseModel.

        The legacy account's ID. This property supports: searching.  # noqa: E501

        :param legacy_account_id: The legacy_account_id of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._legacy_account_id = legacy_account_id

    @property
    def provider_identifier(self):
        """Gets the provider_identifier of this MavResponseModel.  # noqa: E501

        The account's cloud provider identifier. This property supports: searching.  # noqa: E501

        :return: The provider_identifier of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_identifier

    @provider_identifier.setter
    def provider_identifier(self, provider_identifier):
        """Sets the provider_identifier of this MavResponseModel.

        The account's cloud provider identifier. This property supports: searching.  # noqa: E501

        :param provider_identifier: The provider_identifier of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_identifier = provider_identifier

    @property
    def provider_sub_type(self):
        """Gets the provider_sub_type of this MavResponseModel.  # noqa: E501

        The account's cloud provider sub-type. This property supports: searching.  # noqa: E501

        :return: The provider_sub_type of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_sub_type

    @provider_sub_type.setter
    def provider_sub_type(self, provider_sub_type):
        """Sets the provider_sub_type of this MavResponseModel.

        The account's cloud provider sub-type. This property supports: searching.  # noqa: E501

        :param provider_sub_type: The provider_sub_type of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_sub_type = provider_sub_type

    @property
    def provider_payment_type(self):
        """Gets the provider_payment_type of this MavResponseModel.  # noqa: E501

        The account's payment model.  # noqa: E501

        :return: The provider_payment_type of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_payment_type

    @provider_payment_type.setter
    def provider_payment_type(self, provider_payment_type):
        """Sets the provider_payment_type of this MavResponseModel.

        The account's payment model.  # noqa: E501

        :param provider_payment_type: The provider_payment_type of this MavResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Payer", "Payee"]  # noqa: E501
        if provider_payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `provider_payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(provider_payment_type, allowed_values)
            )

        self._provider_payment_type = provider_payment_type

    @property
    def payer_identifier(self):
        """Gets the payer_identifier of this MavResponseModel.  # noqa: E501

        The account's payer identifier. This property supports: searching.  # noqa: E501

        :return: The payer_identifier of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._payer_identifier

    @payer_identifier.setter
    def payer_identifier(self, payer_identifier):
        """Sets the payer_identifier of this MavResponseModel.

        The account's payer identifier. This property supports: searching.  # noqa: E501

        :param payer_identifier: The payer_identifier of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._payer_identifier = payer_identifier

    @property
    def include_all_accounts(self):
        """Gets the include_all_accounts of this MavResponseModel.  # noqa: E501

        If true, the MAV includes all accounts.  # noqa: E501

        :return: The include_all_accounts of this MavResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_all_accounts

    @include_all_accounts.setter
    def include_all_accounts(self, include_all_accounts):
        """Sets the include_all_accounts of this MavResponseModel.

        If true, the MAV includes all accounts.  # noqa: E501

        :param include_all_accounts: The include_all_accounts of this MavResponseModel.  # noqa: E501
        :type: bool
        """

        self._include_all_accounts = include_all_accounts

    @property
    def associated_account_attributes(self):
        """Gets the associated_account_attributes of this MavResponseModel.  # noqa: E501

        List of associated account attributes.  # noqa: E501

        :return: The associated_account_attributes of this MavResponseModel.  # noqa: E501
        :rtype: list[AccountAttributeBasicInfo]
        """
        return self._associated_account_attributes

    @associated_account_attributes.setter
    def associated_account_attributes(self, associated_account_attributes):
        """Sets the associated_account_attributes of this MavResponseModel.

        List of associated account attributes.  # noqa: E501

        :param associated_account_attributes: The associated_account_attributes of this MavResponseModel.  # noqa: E501
        :type: list[AccountAttributeBasicInfo]
        """

        self._associated_account_attributes = associated_account_attributes

    @property
    def type(self):
        """Gets the type of this MavResponseModel.  # noqa: E501

        The account group's type. Valid types are General, Group, and MAV. This property supports: filtering and sorting.  # noqa: E501

        :return: The type of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MavResponseModel.

        The account group's type. Valid types are General, Group, and MAV. This property supports: filtering and sorting.  # noqa: E501

        :param type: The type of this MavResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Group", "General", "MAV"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def provider(self):
        """Gets the provider of this MavResponseModel.  # noqa: E501

        The account's cloud provider. This property supports: sorting, filtering and searching.  # noqa: E501

        :return: The provider of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this MavResponseModel.

        The account's cloud provider. This property supports: sorting, filtering and searching.  # noqa: E501

        :param provider: The provider of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def created_date(self):
        """Gets the created_date of this MavResponseModel.  # noqa: E501

        The account's creation date. This property supports: sorting and filtering.  # noqa: E501

        :return: The created_date of this MavResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this MavResponseModel.

        The account's creation date. This property supports: sorting and filtering.  # noqa: E501

        :param created_date: The created_date of this MavResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def has_pending_change(self):
        """Gets the has_pending_change of this MavResponseModel.  # noqa: E501

        True if the account has a pending change.  # noqa: E501

        :return: The has_pending_change of this MavResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._has_pending_change

    @has_pending_change.setter
    def has_pending_change(self, has_pending_change):
        """Sets the has_pending_change of this MavResponseModel.

        True if the account has a pending change.  # noqa: E501

        :param has_pending_change: The has_pending_change of this MavResponseModel.  # noqa: E501
        :type: bool
        """

        self._has_pending_change = has_pending_change

    @property
    def is_system_managed(self):
        """Gets the is_system_managed of this MavResponseModel.  # noqa: E501

        Setting to indicate whether an account is managed automatically.  # noqa: E501

        :return: The is_system_managed of this MavResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_system_managed

    @is_system_managed.setter
    def is_system_managed(self, is_system_managed):
        """Sets the is_system_managed of this MavResponseModel.

        Setting to indicate whether an account is managed automatically.  # noqa: E501

        :param is_system_managed: The is_system_managed of this MavResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_system_managed = is_system_managed

    @property
    def credential_verification_status(self):
        """Gets the credential_verification_status of this MavResponseModel.  # noqa: E501

        Indicates the account's credential verification status. This property supports: sorting and filtering.  # noqa: E501

        :return: The credential_verification_status of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._credential_verification_status

    @credential_verification_status.setter
    def credential_verification_status(self, credential_verification_status):
        """Sets the credential_verification_status of this MavResponseModel.

        Indicates the account's credential verification status. This property supports: sorting and filtering.  # noqa: E501

        :param credential_verification_status: The credential_verification_status of this MavResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Passed", "Failed", "Warning", "Empty", "NotConfigured"]  # noqa: E501
        if credential_verification_status not in allowed_values:
            raise ValueError(
                "Invalid value for `credential_verification_status` ({0}), must be one of {1}"  # noqa: E501
                .format(credential_verification_status, allowed_values)
            )

        self._credential_verification_status = credential_verification_status

    @property
    def id(self):
        """Gets the id of this MavResponseModel.  # noqa: E501

        The account's ID. This property supports: sorting and filtering.  # noqa: E501

        :return: The id of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MavResponseModel.

        The account's ID. This property supports: sorting and filtering.  # noqa: E501

        :param id: The id of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MavResponseModel.  # noqa: E501

        The account's name. This property supports: sorting, filtering and searching.  # noqa: E501

        :return: The name of this MavResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MavResponseModel.

        The account's name. This property supports: sorting, filtering and searching.  # noqa: E501

        :param name: The name of this MavResponseModel.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(MavResponseModel, dict):
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
        if not isinstance(other, MavResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
