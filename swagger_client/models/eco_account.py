# coding: utf-8

"""
    Valour API

    The official Valour API  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EcoAccount(object):
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
        'id': 'int',
        'name': 'str',
        'account_type': 'AccountType',
        'user_id': 'int',
        'planet_id': 'int',
        'planet_member_id': 'int',
        'currency_id': 'int',
        'balance_value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'account_type': 'accountType',
        'user_id': 'userId',
        'planet_id': 'planetId',
        'planet_member_id': 'planetMemberId',
        'currency_id': 'currencyId',
        'balance_value': 'balanceValue'
    }

    def __init__(self, id=None, name=None, account_type=None, user_id=None, planet_id=None, planet_member_id=None, currency_id=None, balance_value=None):  # noqa: E501
        """EcoAccount - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._account_type = None
        self._user_id = None
        self._planet_id = None
        self._planet_member_id = None
        self._currency_id = None
        self._balance_value = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if account_type is not None:
            self.account_type = account_type
        if user_id is not None:
            self.user_id = user_id
        if planet_id is not None:
            self.planet_id = planet_id
        if planet_member_id is not None:
            self.planet_member_id = planet_member_id
        if currency_id is not None:
            self.currency_id = currency_id
        if balance_value is not None:
            self.balance_value = balance_value

    @property
    def id(self):
        """Gets the id of this EcoAccount.  # noqa: E501


        :return: The id of this EcoAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcoAccount.


        :param id: The id of this EcoAccount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EcoAccount.  # noqa: E501


        :return: The name of this EcoAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcoAccount.


        :param name: The name of this EcoAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_type(self):
        """Gets the account_type of this EcoAccount.  # noqa: E501


        :return: The account_type of this EcoAccount.  # noqa: E501
        :rtype: AccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this EcoAccount.


        :param account_type: The account_type of this EcoAccount.  # noqa: E501
        :type: AccountType
        """

        self._account_type = account_type

    @property
    def user_id(self):
        """Gets the user_id of this EcoAccount.  # noqa: E501


        :return: The user_id of this EcoAccount.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this EcoAccount.


        :param user_id: The user_id of this EcoAccount.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def planet_id(self):
        """Gets the planet_id of this EcoAccount.  # noqa: E501


        :return: The planet_id of this EcoAccount.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this EcoAccount.


        :param planet_id: The planet_id of this EcoAccount.  # noqa: E501
        :type: int
        """

        self._planet_id = planet_id

    @property
    def planet_member_id(self):
        """Gets the planet_member_id of this EcoAccount.  # noqa: E501


        :return: The planet_member_id of this EcoAccount.  # noqa: E501
        :rtype: int
        """
        return self._planet_member_id

    @planet_member_id.setter
    def planet_member_id(self, planet_member_id):
        """Sets the planet_member_id of this EcoAccount.


        :param planet_member_id: The planet_member_id of this EcoAccount.  # noqa: E501
        :type: int
        """

        self._planet_member_id = planet_member_id

    @property
    def currency_id(self):
        """Gets the currency_id of this EcoAccount.  # noqa: E501


        :return: The currency_id of this EcoAccount.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this EcoAccount.


        :param currency_id: The currency_id of this EcoAccount.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def balance_value(self):
        """Gets the balance_value of this EcoAccount.  # noqa: E501


        :return: The balance_value of this EcoAccount.  # noqa: E501
        :rtype: float
        """
        return self._balance_value

    @balance_value.setter
    def balance_value(self, balance_value):
        """Sets the balance_value of this EcoAccount.


        :param balance_value: The balance_value of this EcoAccount.  # noqa: E501
        :type: float
        """

        self._balance_value = balance_value

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
        if issubclass(EcoAccount, dict):
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
        if not isinstance(other, EcoAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other