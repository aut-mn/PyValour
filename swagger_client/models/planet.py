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

class Planet(object):
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
        'owner_id': 'int',
        'name': 'str',
        'node_name': 'str',
        'icon_url': 'str',
        'description': 'str',
        'public': 'bool',
        'discoverable': 'bool',
        'nsfw': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'owner_id': 'ownerId',
        'name': 'name',
        'node_name': 'nodeName',
        'icon_url': 'iconUrl',
        'description': 'description',
        'public': 'public',
        'discoverable': 'discoverable',
        'nsfw': 'nsfw'
    }

    def __init__(self, id=None, owner_id=None, name=None, node_name=None, icon_url=None, description=None, public=None, discoverable=None, nsfw=None):  # noqa: E501
        """Planet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._owner_id = None
        self._name = None
        self._node_name = None
        self._icon_url = None
        self._description = None
        self._public = None
        self._discoverable = None
        self._nsfw = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if owner_id is not None:
            self.owner_id = owner_id
        if name is not None:
            self.name = name
        if node_name is not None:
            self.node_name = node_name
        if icon_url is not None:
            self.icon_url = icon_url
        if description is not None:
            self.description = description
        if public is not None:
            self.public = public
        if discoverable is not None:
            self.discoverable = discoverable
        if nsfw is not None:
            self.nsfw = nsfw

    @property
    def id(self):
        """Gets the id of this Planet.  # noqa: E501


        :return: The id of this Planet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Planet.


        :param id: The id of this Planet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def owner_id(self):
        """Gets the owner_id of this Planet.  # noqa: E501


        :return: The owner_id of this Planet.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Planet.


        :param owner_id: The owner_id of this Planet.  # noqa: E501
        :type: int
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this Planet.  # noqa: E501


        :return: The name of this Planet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Planet.


        :param name: The name of this Planet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def node_name(self):
        """Gets the node_name of this Planet.  # noqa: E501


        :return: The node_name of this Planet.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this Planet.


        :param node_name: The node_name of this Planet.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def icon_url(self):
        """Gets the icon_url of this Planet.  # noqa: E501


        :return: The icon_url of this Planet.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this Planet.


        :param icon_url: The icon_url of this Planet.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def description(self):
        """Gets the description of this Planet.  # noqa: E501


        :return: The description of this Planet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Planet.


        :param description: The description of this Planet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def public(self):
        """Gets the public of this Planet.  # noqa: E501


        :return: The public of this Planet.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Planet.


        :param public: The public of this Planet.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def discoverable(self):
        """Gets the discoverable of this Planet.  # noqa: E501


        :return: The discoverable of this Planet.  # noqa: E501
        :rtype: bool
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """Sets the discoverable of this Planet.


        :param discoverable: The discoverable of this Planet.  # noqa: E501
        :type: bool
        """

        self._discoverable = discoverable

    @property
    def nsfw(self):
        """Gets the nsfw of this Planet.  # noqa: E501


        :return: The nsfw of this Planet.  # noqa: E501
        :rtype: bool
        """
        return self._nsfw

    @nsfw.setter
    def nsfw(self, nsfw):
        """Sets the nsfw of this Planet.


        :param nsfw: The nsfw of this Planet.  # noqa: E501
        :type: bool
        """

        self._nsfw = nsfw

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
        if issubclass(Planet, dict):
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
        if not isinstance(other, Planet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other