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


class EmbedAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_embed_interact_post(self, **kwargs):  # noqa: E501
        """api_embed_interact_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_interact_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_embed_interact_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_embed_interact_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_embed_interact_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_embed_interact_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_interact_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_embed_interact_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/embed/interact', 'POST',
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

    def api_embed_planetchannelupdate_post(self, **kwargs):  # noqa: E501
        """api_embed_planetchannelupdate_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_planetchannelupdate_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_embed_planetchannelupdate_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_embed_planetchannelupdate_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_embed_planetchannelupdate_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_embed_planetchannelupdate_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_planetchannelupdate_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_embed_planetchannelupdate_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/embed/planetchannelupdate', 'POST',
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

    def api_embed_planetpersonalupdate_post(self, **kwargs):  # noqa: E501
        """api_embed_planetpersonalupdate_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_planetpersonalupdate_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_embed_planetpersonalupdate_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_embed_planetpersonalupdate_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_embed_planetpersonalupdate_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_embed_planetpersonalupdate_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_embed_planetpersonalupdate_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_embed_planetpersonalupdate_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/embed/planetpersonalupdate', 'POST',
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