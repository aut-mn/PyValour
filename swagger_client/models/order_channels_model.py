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

class OrderChannelsModel(object):
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
        'order': 'list[int]',
        'category_id': 'int',
        'planet_id': 'int'
    }

    attribute_map = {
        'order': 'order',
        'category_id': 'categoryId',
        'planet_id': 'planetId'
    }

    def __init__(self, order=None, category_id=None, planet_id=None):  # noqa: E501
        """OrderChannelsModel - a model defined in Swagger"""  # noqa: E501
        self._order = None
        self._category_id = None
        self._planet_id = None
        self.discriminator = None
        if order is not None:
            self.order = order
        if category_id is not None:
            self.category_id = category_id
        if planet_id is not None:
            self.planet_id = planet_id

    @property
    def order(self):
        """Gets the order of this OrderChannelsModel.  # noqa: E501


        :return: The order of this OrderChannelsModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this OrderChannelsModel.


        :param order: The order of this OrderChannelsModel.  # noqa: E501
        :type: list[int]
        """

        self._order = order

    @property
    def category_id(self):
        """Gets the category_id of this OrderChannelsModel.  # noqa: E501


        :return: The category_id of this OrderChannelsModel.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this OrderChannelsModel.


        :param category_id: The category_id of this OrderChannelsModel.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def planet_id(self):
        """Gets the planet_id of this OrderChannelsModel.  # noqa: E501


        :return: The planet_id of this OrderChannelsModel.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this OrderChannelsModel.


        :param planet_id: The planet_id of this OrderChannelsModel.  # noqa: E501
        :type: int
        """

        self._planet_id = planet_id

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
        if issubclass(OrderChannelsModel, dict):
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
        if not isinstance(other, OrderChannelsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other