# coding: utf-8

"""
    Valour API

    The official Valour API  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserFriendApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_userfriends_add_friend_username_post(self, friend_username, **kwargs):  # noqa: E501
        """api_userfriends_add_friend_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_add_friend_username_post(friend_username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str friend_username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_userfriends_add_friend_username_post_with_http_info(friend_username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_userfriends_add_friend_username_post_with_http_info(friend_username, **kwargs)  # noqa: E501
            return data

    def api_userfriends_add_friend_username_post_with_http_info(self, friend_username, **kwargs):  # noqa: E501
        """api_userfriends_add_friend_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_add_friend_username_post_with_http_info(friend_username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str friend_username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['friend_username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_userfriends_add_friend_username_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'friend_username' is set
        if ('friend_username' not in params or
                params['friend_username'] is None):
            raise ValueError("Missing the required parameter `friend_username` when calling `api_userfriends_add_friend_username_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'friend_username' in params:
            path_params['friendUsername'] = params['friend_username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/userfriends/add/{friendUsername}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_userfriends_cancel_username_post(self, username, **kwargs):  # noqa: E501
        """api_userfriends_cancel_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_cancel_username_post(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_userfriends_cancel_username_post_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_userfriends_cancel_username_post_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def api_userfriends_cancel_username_post_with_http_info(self, username, **kwargs):  # noqa: E501
        """api_userfriends_cancel_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_cancel_username_post_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_userfriends_cancel_username_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_userfriends_cancel_username_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/userfriends/cancel/{username}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_userfriends_decline_username_post(self, username, **kwargs):  # noqa: E501
        """api_userfriends_decline_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_decline_username_post(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_userfriends_decline_username_post_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_userfriends_decline_username_post_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def api_userfriends_decline_username_post_with_http_info(self, username, **kwargs):  # noqa: E501
        """api_userfriends_decline_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_decline_username_post_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_userfriends_decline_username_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `api_userfriends_decline_username_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/userfriends/decline/{username}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_userfriends_remove_friend_username_post(self, friend_username, **kwargs):  # noqa: E501
        """api_userfriends_remove_friend_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_remove_friend_username_post(friend_username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str friend_username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_userfriends_remove_friend_username_post_with_http_info(friend_username, **kwargs)  # noqa: E501
        else:
            (data) = self.api_userfriends_remove_friend_username_post_with_http_info(friend_username, **kwargs)  # noqa: E501
            return data

    def api_userfriends_remove_friend_username_post_with_http_info(self, friend_username, **kwargs):  # noqa: E501
        """api_userfriends_remove_friend_username_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_remove_friend_username_post_with_http_info(friend_username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str friend_username: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['friend_username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_userfriends_remove_friend_username_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'friend_username' is set
        if ('friend_username' not in params or
                params['friend_username'] is None):
            raise ValueError("Missing the required parameter `friend_username` when calling `api_userfriends_remove_friend_username_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'friend_username' in params:
            path_params['friendUsername'] = params['friend_username']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/userfriends/remove/{friendUsername}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_userfriends_user_id_friend_id_get(self, user_id, friend_id, **kwargs):  # noqa: E501
        """api_userfriends_user_id_friend_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_user_id_friend_id_get(user_id, friend_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param int friend_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_userfriends_user_id_friend_id_get_with_http_info(user_id, friend_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_userfriends_user_id_friend_id_get_with_http_info(user_id, friend_id, **kwargs)  # noqa: E501
            return data

    def api_userfriends_user_id_friend_id_get_with_http_info(self, user_id, friend_id, **kwargs):  # noqa: E501
        """api_userfriends_user_id_friend_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_userfriends_user_id_friend_id_get_with_http_info(user_id, friend_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: (required)
        :param int friend_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'friend_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_userfriends_user_id_friend_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `api_userfriends_user_id_friend_id_get`")  # noqa: E501
        # verify the required parameter 'friend_id' is set
        if ('friend_id' not in params or
                params['friend_id'] is None):
            raise ValueError("Missing the required parameter `friend_id` when calling `api_userfriends_user_id_friend_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501
        if 'friend_id' in params:
            path_params['friendId'] = params['friend_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/userfriends/{userId}/{friendId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)