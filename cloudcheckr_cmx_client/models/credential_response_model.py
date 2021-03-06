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

class CredentialResponseModel(object):
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
        'provider': 'str',
        'provider_sub_type': 'str',
        'provider_identifier': 'str',
        'provider_billing_identifier': 'str',
        'region_group': 'str',
        'purpose': 'str',
        'credential_metadata': 'list[CredentialMetadataModel]',
        'created_date': 'datetime',
        'updated_date': 'datetime',
        'last_verified_date': 'datetime',
        'last_refreshed_date': 'datetime',
        'verification_summary': 'str',
        'verification_results': 'list[VerificationActionModel]'
    }

    attribute_map = {
        'provider': 'provider',
        'provider_sub_type': 'providerSubType',
        'provider_identifier': 'providerIdentifier',
        'provider_billing_identifier': 'providerBillingIdentifier',
        'region_group': 'regionGroup',
        'purpose': 'purpose',
        'credential_metadata': 'credentialMetadata',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate',
        'last_verified_date': 'lastVerifiedDate',
        'last_refreshed_date': 'lastRefreshedDate',
        'verification_summary': 'verificationSummary',
        'verification_results': 'verificationResults'
    }

    def __init__(self, provider=None, provider_sub_type=None, provider_identifier=None, provider_billing_identifier=None, region_group=None, purpose=None, credential_metadata=None, created_date=None, updated_date=None, last_verified_date=None, last_refreshed_date=None, verification_summary=None, verification_results=None):  # noqa: E501
        """CredentialResponseModel - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._provider_sub_type = None
        self._provider_identifier = None
        self._provider_billing_identifier = None
        self._region_group = None
        self._purpose = None
        self._credential_metadata = None
        self._created_date = None
        self._updated_date = None
        self._last_verified_date = None
        self._last_refreshed_date = None
        self._verification_summary = None
        self._verification_results = None
        self.discriminator = None
        if provider is not None:
            self.provider = provider
        if provider_sub_type is not None:
            self.provider_sub_type = provider_sub_type
        if provider_identifier is not None:
            self.provider_identifier = provider_identifier
        if provider_billing_identifier is not None:
            self.provider_billing_identifier = provider_billing_identifier
        if region_group is not None:
            self.region_group = region_group
        if purpose is not None:
            self.purpose = purpose
        if credential_metadata is not None:
            self.credential_metadata = credential_metadata
        if created_date is not None:
            self.created_date = created_date
        if updated_date is not None:
            self.updated_date = updated_date
        if last_verified_date is not None:
            self.last_verified_date = last_verified_date
        if last_refreshed_date is not None:
            self.last_refreshed_date = last_refreshed_date
        if verification_summary is not None:
            self.verification_summary = verification_summary
        if verification_results is not None:
            self.verification_results = verification_results

    @property
    def provider(self):
        """Gets the provider of this CredentialResponseModel.  # noqa: E501

        The account's cloud provider.  # noqa: E501

        :return: The provider of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CredentialResponseModel.

        The account's cloud provider.  # noqa: E501

        :param provider: The provider of this CredentialResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotApplicable", "AWS", "Azure", "Google", "VMware", "Oracle"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def provider_sub_type(self):
        """Gets the provider_sub_type of this CredentialResponseModel.  # noqa: E501

        The account's cloud provider sub-type.  # noqa: E501

        :return: The provider_sub_type of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_sub_type

    @provider_sub_type.setter
    def provider_sub_type(self, provider_sub_type):
        """Sets the provider_sub_type of this CredentialResponseModel.

        The account's cloud provider sub-type.  # noqa: E501

        :param provider_sub_type: The provider_sub_type of this CredentialResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_sub_type = provider_sub_type

    @property
    def provider_identifier(self):
        """Gets the provider_identifier of this CredentialResponseModel.  # noqa: E501

        The account group's cloud provider identifier.  # noqa: E501

        :return: The provider_identifier of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_identifier

    @provider_identifier.setter
    def provider_identifier(self, provider_identifier):
        """Sets the provider_identifier of this CredentialResponseModel.

        The account group's cloud provider identifier.  # noqa: E501

        :param provider_identifier: The provider_identifier of this CredentialResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_identifier = provider_identifier

    @property
    def provider_billing_identifier(self):
        """Gets the provider_billing_identifier of this CredentialResponseModel.  # noqa: E501

        The account group's cloud provider billing identifier.  If the billing account ID is the same as the credential account ID, this will have no value.  This will have a value when billing is tracked under a different account ID from the  account group's standard cloud provider identifier.  Example: An AWS Gov account has a separate commercial account ID for billing.  # noqa: E501

        :return: The provider_billing_identifier of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._provider_billing_identifier

    @provider_billing_identifier.setter
    def provider_billing_identifier(self, provider_billing_identifier):
        """Sets the provider_billing_identifier of this CredentialResponseModel.

        The account group's cloud provider billing identifier.  If the billing account ID is the same as the credential account ID, this will have no value.  This will have a value when billing is tracked under a different account ID from the  account group's standard cloud provider identifier.  Example: An AWS Gov account has a separate commercial account ID for billing.  # noqa: E501

        :param provider_billing_identifier: The provider_billing_identifier of this CredentialResponseModel.  # noqa: E501
        :type: str
        """

        self._provider_billing_identifier = provider_billing_identifier

    @property
    def region_group(self):
        """Gets the region_group of this CredentialResponseModel.  # noqa: E501

        The account's region group (i.e. the unique data center group that is being used, e.g. commercial, gov, etc).  # noqa: E501

        :return: The region_group of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._region_group

    @region_group.setter
    def region_group(self, region_group):
        """Sets the region_group of this CredentialResponseModel.

        The account's region group (i.e. the unique data center group that is being used, e.g. commercial, gov, etc).  # noqa: E501

        :param region_group: The region_group of this CredentialResponseModel.  # noqa: E501
        :type: str
        """

        self._region_group = region_group

    @property
    def purpose(self):
        """Gets the purpose of this CredentialResponseModel.  # noqa: E501

        The purpose of the account credential (i.e. what it will be used for).  # noqa: E501

        :return: The purpose of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this CredentialResponseModel.

        The purpose of the account credential (i.e. what it will be used for).  # noqa: E501

        :param purpose: The purpose of this CredentialResponseModel.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def credential_metadata(self):
        """Gets the credential_metadata of this CredentialResponseModel.  # noqa: E501

        Credential identification information.  # noqa: E501

        :return: The credential_metadata of this CredentialResponseModel.  # noqa: E501
        :rtype: list[CredentialMetadataModel]
        """
        return self._credential_metadata

    @credential_metadata.setter
    def credential_metadata(self, credential_metadata):
        """Sets the credential_metadata of this CredentialResponseModel.

        Credential identification information.  # noqa: E501

        :param credential_metadata: The credential_metadata of this CredentialResponseModel.  # noqa: E501
        :type: list[CredentialMetadataModel]
        """

        self._credential_metadata = credential_metadata

    @property
    def created_date(self):
        """Gets the created_date of this CredentialResponseModel.  # noqa: E501

        The date when the credentials were created.  # noqa: E501

        :return: The created_date of this CredentialResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CredentialResponseModel.

        The date when the credentials were created.  # noqa: E501

        :param created_date: The created_date of this CredentialResponseModel.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this CredentialResponseModel.  # noqa: E501

        The date when the credentials were last modified (e.g. new credential info specified).  # noqa: E501

        :return: The updated_date of this CredentialResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this CredentialResponseModel.

        The date when the credentials were last modified (e.g. new credential info specified).  # noqa: E501

        :param updated_date: The updated_date of this CredentialResponseModel.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

    @property
    def last_verified_date(self):
        """Gets the last_verified_date of this CredentialResponseModel.  # noqa: E501

        The date when the credentials were last checked if still valid.  These verification checks occur automatically on a periodic basis.  # noqa: E501

        :return: The last_verified_date of this CredentialResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_verified_date

    @last_verified_date.setter
    def last_verified_date(self, last_verified_date):
        """Sets the last_verified_date of this CredentialResponseModel.

        The date when the credentials were last checked if still valid.  These verification checks occur automatically on a periodic basis.  # noqa: E501

        :param last_verified_date: The last_verified_date of this CredentialResponseModel.  # noqa: E501
        :type: datetime
        """

        self._last_verified_date = last_verified_date

    @property
    def last_refreshed_date(self):
        """Gets the last_refreshed_date of this CredentialResponseModel.  # noqa: E501

        The date when the credentials were last refreshed (if applicable).  # noqa: E501

        :return: The last_refreshed_date of this CredentialResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_refreshed_date

    @last_refreshed_date.setter
    def last_refreshed_date(self, last_refreshed_date):
        """Sets the last_refreshed_date of this CredentialResponseModel.

        The date when the credentials were last refreshed (if applicable).  # noqa: E501

        :param last_refreshed_date: The last_refreshed_date of this CredentialResponseModel.  # noqa: E501
        :type: datetime
        """

        self._last_refreshed_date = last_refreshed_date

    @property
    def verification_summary(self):
        """Gets the verification_summary of this CredentialResponseModel.  # noqa: E501

        Summary of last verification actions.  # noqa: E501

        :return: The verification_summary of this CredentialResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._verification_summary

    @verification_summary.setter
    def verification_summary(self, verification_summary):
        """Sets the verification_summary of this CredentialResponseModel.

        Summary of last verification actions.  # noqa: E501

        :param verification_summary: The verification_summary of this CredentialResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Passed", "Failed", "Warning", "Skipped", "Empty", "RequestingAccess", "RequiresAccountSelection"]  # noqa: E501
        if verification_summary not in allowed_values:
            raise ValueError(
                "Invalid value for `verification_summary` ({0}), must be one of {1}"  # noqa: E501
                .format(verification_summary, allowed_values)
            )

        self._verification_summary = verification_summary

    @property
    def verification_results(self):
        """Gets the verification_results of this CredentialResponseModel.  # noqa: E501

        List of all verification actions and their results.  # noqa: E501

        :return: The verification_results of this CredentialResponseModel.  # noqa: E501
        :rtype: list[VerificationActionModel]
        """
        return self._verification_results

    @verification_results.setter
    def verification_results(self, verification_results):
        """Sets the verification_results of this CredentialResponseModel.

        List of all verification actions and their results.  # noqa: E501

        :param verification_results: The verification_results of this CredentialResponseModel.  # noqa: E501
        :type: list[VerificationActionModel]
        """

        self._verification_results = verification_results

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
        if issubclass(CredentialResponseModel, dict):
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
        if not isinstance(other, CredentialResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
