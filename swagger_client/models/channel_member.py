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

class ChannelMember(object):
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
        'channel_id': 'int',
        'user_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'channel_id': 'channelId',
        'user_id': 'userId'
    }

    def __init__(self, id=None, channel_id=None, user_id=None):  # noqa: E501
        """ChannelMember - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._channel_id = None
        self._user_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if channel_id is not None:
            self.channel_id = channel_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this ChannelMember.  # noqa: E501


        :return: The id of this ChannelMember.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelMember.


        :param id: The id of this ChannelMember.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def channel_id(self):
        """Gets the channel_id of this ChannelMember.  # noqa: E501


        :return: The channel_id of this ChannelMember.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this ChannelMember.


        :param channel_id: The channel_id of this ChannelMember.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def user_id(self):
        """Gets the user_id of this ChannelMember.  # noqa: E501


        :return: The user_id of this ChannelMember.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChannelMember.


        :param user_id: The user_id of this ChannelMember.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(ChannelMember, dict):
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
        if not isinstance(other, ChannelMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other