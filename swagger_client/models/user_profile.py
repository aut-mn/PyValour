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

class UserProfile(object):
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
        'headline': 'str',
        'bio': 'str',
        'border_color': 'str',
        'glow_color': 'str',
        'primary_color': 'str',
        'secondary_color': 'str',
        'tertiary_color': 'str',
        'text_color': 'str',
        'animated_border': 'bool',
        'background_image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'headline': 'headline',
        'bio': 'bio',
        'border_color': 'borderColor',
        'glow_color': 'glowColor',
        'primary_color': 'primaryColor',
        'secondary_color': 'secondaryColor',
        'tertiary_color': 'tertiaryColor',
        'text_color': 'textColor',
        'animated_border': 'animatedBorder',
        'background_image': 'backgroundImage'
    }

    def __init__(self, id=None, headline=None, bio=None, border_color=None, glow_color=None, primary_color=None, secondary_color=None, tertiary_color=None, text_color=None, animated_border=None, background_image=None):  # noqa: E501
        """UserProfile - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._headline = None
        self._bio = None
        self._border_color = None
        self._glow_color = None
        self._primary_color = None
        self._secondary_color = None
        self._tertiary_color = None
        self._text_color = None
        self._animated_border = None
        self._background_image = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if headline is not None:
            self.headline = headline
        if bio is not None:
            self.bio = bio
        if border_color is not None:
            self.border_color = border_color
        if glow_color is not None:
            self.glow_color = glow_color
        if primary_color is not None:
            self.primary_color = primary_color
        if secondary_color is not None:
            self.secondary_color = secondary_color
        if tertiary_color is not None:
            self.tertiary_color = tertiary_color
        if text_color is not None:
            self.text_color = text_color
        if animated_border is not None:
            self.animated_border = animated_border
        if background_image is not None:
            self.background_image = background_image

    @property
    def id(self):
        """Gets the id of this UserProfile.  # noqa: E501


        :return: The id of this UserProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserProfile.


        :param id: The id of this UserProfile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def headline(self):
        """Gets the headline of this UserProfile.  # noqa: E501


        :return: The headline of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this UserProfile.


        :param headline: The headline of this UserProfile.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def bio(self):
        """Gets the bio of this UserProfile.  # noqa: E501


        :return: The bio of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this UserProfile.


        :param bio: The bio of this UserProfile.  # noqa: E501
        :type: str
        """

        self._bio = bio

    @property
    def border_color(self):
        """Gets the border_color of this UserProfile.  # noqa: E501


        :return: The border_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._border_color

    @border_color.setter
    def border_color(self, border_color):
        """Sets the border_color of this UserProfile.


        :param border_color: The border_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._border_color = border_color

    @property
    def glow_color(self):
        """Gets the glow_color of this UserProfile.  # noqa: E501


        :return: The glow_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._glow_color

    @glow_color.setter
    def glow_color(self, glow_color):
        """Sets the glow_color of this UserProfile.


        :param glow_color: The glow_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._glow_color = glow_color

    @property
    def primary_color(self):
        """Gets the primary_color of this UserProfile.  # noqa: E501


        :return: The primary_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._primary_color

    @primary_color.setter
    def primary_color(self, primary_color):
        """Sets the primary_color of this UserProfile.


        :param primary_color: The primary_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._primary_color = primary_color

    @property
    def secondary_color(self):
        """Gets the secondary_color of this UserProfile.  # noqa: E501


        :return: The secondary_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, secondary_color):
        """Sets the secondary_color of this UserProfile.


        :param secondary_color: The secondary_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._secondary_color = secondary_color

    @property
    def tertiary_color(self):
        """Gets the tertiary_color of this UserProfile.  # noqa: E501


        :return: The tertiary_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._tertiary_color

    @tertiary_color.setter
    def tertiary_color(self, tertiary_color):
        """Sets the tertiary_color of this UserProfile.


        :param tertiary_color: The tertiary_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._tertiary_color = tertiary_color

    @property
    def text_color(self):
        """Gets the text_color of this UserProfile.  # noqa: E501


        :return: The text_color of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        """Sets the text_color of this UserProfile.


        :param text_color: The text_color of this UserProfile.  # noqa: E501
        :type: str
        """

        self._text_color = text_color

    @property
    def animated_border(self):
        """Gets the animated_border of this UserProfile.  # noqa: E501


        :return: The animated_border of this UserProfile.  # noqa: E501
        :rtype: bool
        """
        return self._animated_border

    @animated_border.setter
    def animated_border(self, animated_border):
        """Sets the animated_border of this UserProfile.


        :param animated_border: The animated_border of this UserProfile.  # noqa: E501
        :type: bool
        """

        self._animated_border = animated_border

    @property
    def background_image(self):
        """Gets the background_image of this UserProfile.  # noqa: E501


        :return: The background_image of this UserProfile.  # noqa: E501
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this UserProfile.


        :param background_image: The background_image of this UserProfile.  # noqa: E501
        :type: str
        """

        self._background_image = background_image

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
        if issubclass(UserProfile, dict):
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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
