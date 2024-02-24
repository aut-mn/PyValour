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

class Currency(object):
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
        'planet_id': 'int',
        'name': 'str',
        'plural_name': 'str',
        'short_code': 'str',
        'symbol': 'str',
        'issued': 'int',
        'decimal_places': 'int'
    }

    attribute_map = {
        'id': 'id',
        'planet_id': 'planetId',
        'name': 'name',
        'plural_name': 'pluralName',
        'short_code': 'shortCode',
        'symbol': 'symbol',
        'issued': 'issued',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, id=None, planet_id=None, name=None, plural_name=None, short_code=None, symbol=None, issued=None, decimal_places=None):  # noqa: E501
        """Currency - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._planet_id = None
        self._name = None
        self._plural_name = None
        self._short_code = None
        self._symbol = None
        self._issued = None
        self._decimal_places = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if planet_id is not None:
            self.planet_id = planet_id
        if name is not None:
            self.name = name
        if plural_name is not None:
            self.plural_name = plural_name
        if short_code is not None:
            self.short_code = short_code
        if symbol is not None:
            self.symbol = symbol
        if issued is not None:
            self.issued = issued
        if decimal_places is not None:
            self.decimal_places = decimal_places

    @property
    def id(self):
        """Gets the id of this Currency.  # noqa: E501


        :return: The id of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Currency.


        :param id: The id of this Currency.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def planet_id(self):
        """Gets the planet_id of this Currency.  # noqa: E501


        :return: The planet_id of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this Currency.


        :param planet_id: The planet_id of this Currency.  # noqa: E501
        :type: int
        """

        self._planet_id = planet_id

    @property
    def name(self):
        """Gets the name of this Currency.  # noqa: E501


        :return: The name of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Currency.


        :param name: The name of this Currency.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def plural_name(self):
        """Gets the plural_name of this Currency.  # noqa: E501


        :return: The plural_name of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._plural_name

    @plural_name.setter
    def plural_name(self, plural_name):
        """Sets the plural_name of this Currency.


        :param plural_name: The plural_name of this Currency.  # noqa: E501
        :type: str
        """

        self._plural_name = plural_name

    @property
    def short_code(self):
        """Gets the short_code of this Currency.  # noqa: E501


        :return: The short_code of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this Currency.


        :param short_code: The short_code of this Currency.  # noqa: E501
        :type: str
        """

        self._short_code = short_code

    @property
    def symbol(self):
        """Gets the symbol of this Currency.  # noqa: E501


        :return: The symbol of this Currency.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Currency.


        :param symbol: The symbol of this Currency.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def issued(self):
        """Gets the issued of this Currency.  # noqa: E501


        :return: The issued of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._issued

    @issued.setter
    def issued(self, issued):
        """Sets the issued of this Currency.


        :param issued: The issued of this Currency.  # noqa: E501
        :type: int
        """

        self._issued = issued

    @property
    def decimal_places(self):
        """Gets the decimal_places of this Currency.  # noqa: E501


        :return: The decimal_places of this Currency.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this Currency.


        :param decimal_places: The decimal_places of this Currency.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

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
        if issubclass(Currency, dict):
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
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other