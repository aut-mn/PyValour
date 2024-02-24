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

class Report(object):
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
        'time_created': 'datetime',
        'reporting_user_id': 'int',
        'message_id': 'int',
        'channel_id': 'int',
        'planet_id': 'int',
        'reason_code': 'ReportReasonCode',
        'long_reason': 'str',
        'reviewed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'time_created': 'timeCreated',
        'reporting_user_id': 'reportingUserId',
        'message_id': 'messageId',
        'channel_id': 'channelId',
        'planet_id': 'planetId',
        'reason_code': 'reasonCode',
        'long_reason': 'longReason',
        'reviewed': 'reviewed'
    }

    def __init__(self, id=None, time_created=None, reporting_user_id=None, message_id=None, channel_id=None, planet_id=None, reason_code=None, long_reason=None, reviewed=None):  # noqa: E501
        """Report - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._time_created = None
        self._reporting_user_id = None
        self._message_id = None
        self._channel_id = None
        self._planet_id = None
        self._reason_code = None
        self._long_reason = None
        self._reviewed = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if time_created is not None:
            self.time_created = time_created
        if reporting_user_id is not None:
            self.reporting_user_id = reporting_user_id
        if message_id is not None:
            self.message_id = message_id
        if channel_id is not None:
            self.channel_id = channel_id
        if planet_id is not None:
            self.planet_id = planet_id
        if reason_code is not None:
            self.reason_code = reason_code
        if long_reason is not None:
            self.long_reason = long_reason
        if reviewed is not None:
            self.reviewed = reviewed

    @property
    def id(self):
        """Gets the id of this Report.  # noqa: E501


        :return: The id of this Report.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Report.


        :param id: The id of this Report.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def time_created(self):
        """Gets the time_created of this Report.  # noqa: E501


        :return: The time_created of this Report.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this Report.


        :param time_created: The time_created of this Report.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def reporting_user_id(self):
        """Gets the reporting_user_id of this Report.  # noqa: E501


        :return: The reporting_user_id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._reporting_user_id

    @reporting_user_id.setter
    def reporting_user_id(self, reporting_user_id):
        """Sets the reporting_user_id of this Report.


        :param reporting_user_id: The reporting_user_id of this Report.  # noqa: E501
        :type: int
        """

        self._reporting_user_id = reporting_user_id

    @property
    def message_id(self):
        """Gets the message_id of this Report.  # noqa: E501


        :return: The message_id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this Report.


        :param message_id: The message_id of this Report.  # noqa: E501
        :type: int
        """

        self._message_id = message_id

    @property
    def channel_id(self):
        """Gets the channel_id of this Report.  # noqa: E501


        :return: The channel_id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this Report.


        :param channel_id: The channel_id of this Report.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def planet_id(self):
        """Gets the planet_id of this Report.  # noqa: E501


        :return: The planet_id of this Report.  # noqa: E501
        :rtype: int
        """
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        """Sets the planet_id of this Report.


        :param planet_id: The planet_id of this Report.  # noqa: E501
        :type: int
        """

        self._planet_id = planet_id

    @property
    def reason_code(self):
        """Gets the reason_code of this Report.  # noqa: E501


        :return: The reason_code of this Report.  # noqa: E501
        :rtype: ReportReasonCode
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this Report.


        :param reason_code: The reason_code of this Report.  # noqa: E501
        :type: ReportReasonCode
        """

        self._reason_code = reason_code

    @property
    def long_reason(self):
        """Gets the long_reason of this Report.  # noqa: E501


        :return: The long_reason of this Report.  # noqa: E501
        :rtype: str
        """
        return self._long_reason

    @long_reason.setter
    def long_reason(self, long_reason):
        """Sets the long_reason of this Report.


        :param long_reason: The long_reason of this Report.  # noqa: E501
        :type: str
        """

        self._long_reason = long_reason

    @property
    def reviewed(self):
        """Gets the reviewed of this Report.  # noqa: E501


        :return: The reviewed of this Report.  # noqa: E501
        :rtype: bool
        """
        return self._reviewed

    @reviewed.setter
    def reviewed(self, reviewed):
        """Sets the reviewed of this Report.


        :param reviewed: The reviewed of this Report.  # noqa: E501
        :type: bool
        """

        self._reviewed = reviewed

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
        if issubclass(Report, dict):
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
        if not isinstance(other, Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other