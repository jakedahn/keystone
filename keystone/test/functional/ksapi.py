# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright (c) 2011 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import simplerest


class KeystoneAPI20(simplerest.RESTAPI):
    get_version_info = simplerest.RESTMethod('get_version_info', 'GET', '/')

    get_extensions = simplerest.RESTMethod('get_extensions', 'GET',
                                           '/extensions')
    get_extension = simplerest.RESTMethod('get_extension', 'GET',
                                          '/extensions/{alias}', ['alias'])

    authenticate = simplerest.RESTMethod('authenticate', 'POST',
                                         '/tokens',
                                         ['username', 'password', 'tenantId'],
                                         'passwordCredentials',
                                         username='req', password='req',
                                         tenantId=('req', False))
    validate_token = simplerest.RESTMethod('validate_token', 'GET',
                                           '/tokens/{tokenId}',
                                           ['x_auth_token',
                                            'tokenId', 'belongsTo'],
                                           x_auth_token='header',
                                           belongsTo='query')
    revoke_token = simplerest.RESTMethod('revoke_token', 'DELETE',
                                         '/tokens/{tokenId}',
                                         ['x_auth_token', 'tokenId'],
                                         x_auth_token='header')

    create_tenant = simplerest.RESTMethod('create_tenant', 'POST', '/tenants',
                                          ['x_auth_token', 'id',
                                           'description', 'enabled'],
                                          'tenant',
                                          x_auth_token='header',
                                          id='req', description='req',
                                          enabled='req')
    get_tenants = simplerest.RESTMethod('get_tenants', 'GET', '/tenants',
                                        ['x_auth_token'],
                                        x_auth_token='header')
    get_tenant = simplerest.RESTMethod('get_tenant', 'GET',
                                       '/tenants/{tenantId}',
                                       ['x_auth_token', 'tenantId'],
                                       x_auth_token='header')
    update_tenant = simplerest.RESTMethod('update_tenant', 'PUT',
                                          '/tenants/{tenantId}',
                                          ['x_auth_token', 'tenantId',
                                           'description'],
                                          'tenant',
                                          x_auth_token='header',
                                          description='req')
    delete_tenant = simplerest.RESTMethod('delete_tenant', 'DELETE',
                                          '/tenants/{tenantId}',
                                          ['x_auth_token', 'tenantId'],
                                          x_auth_token='header')

    get_base_urls = simplerest.RESTMethod('get_base_urls', 'GET',
                                          '/baseURLs',
                                          ['x_auth_token', 'serviceName'],
                                          x_auth_token='header',
                                          serviceName='query')
    get_enabled_base_urls = simplerest.RESTMethod('get_enabled_base_urls',
                                                  'GET', '/baseURLs/enabled',
                                                  ['x_auth_token',
                                                   'serviceName'],
                                                  x_auth_token='header',
                                                  serviceName='query')
    get_base_url = simplerest.RESTMethod('get_base_url', 'GET',
                                         '/baseURLs/{baseURLId}',
                                         ['x_auth_token', 'baseURLId'],
                                         x_auth_token='header')
    get_base_url_refs = simplerest.RESTMethod('get_base_url_refs', 'GET',
                                              '/tenants/{tenantId}/'
                                              'baseURLRefs',
                                              ['x_auth_token', 'tenantId'],
                                              x_auth_token='header')
    add_base_url_ref = simplerest.RESTMethod('add_base_url_ref', 'POST',
                                             '/tenants/{tenantId}/'
                                             'baseURLRefs',
                                             ['x_auth_token',
                                              'tenantId', 'id', 'region',
                                              'default', 'serviceName',
                                              'publicURL', 'internalURL',
                                              'enabled'], 'baseURL',
                                             x_auth_token='header',
                                             id='req', region='req',
                                             default='req',
                                             serviceName='req',
                                             publicURL='req',
                                             internalURL='req', enabled='req')
    get_base_url_ref = simplerest.RESTMethod('get_base_url_ref', 'GET',
                                             '/tenants/{tenantId}/'
                                             'baseURLRefs/{baseURLId}',
                                             ['x_auth_token', 'tenantId',
                                              'baseURLId'],
                                             x_auth_token='header')
    delete_base_url_ref = simplerest.RESTMethod('delete_base_url_ref',
                                                'DELETE',
                                                '/tenants/{tenantId}/'
                                                'baseURLRefs/{baseURLId}',
                                                ['x_auth_token', 'tenantId',
                                                 'baseURLId'],
                                                x_auth_token='header')

    get_roles = simplerest.RESTMethod('get_roles', 'GET', '/roles',
                                      ['x_auth_token', 'serviceName'],
                                      x_auth_token='header',
                                      serviceName='query')
    get_role = simplerest.RESTMethod('get_role', 'GET', '/roles/{roleId}',
                                     ['x_auth_token', 'roleId'],
                                     x_auth_token='header')
    get_role_refs = simplerest.RESTMethod('get_role_refs', 'GET',
                                          '/users/{userId}/roleRefs',
                                          ['x_auth_token', 'userId'],
                                          x_auth_token='header')
    add_role_ref = simplerest.RESTMethod('add_role_ref', 'POST',
                                         '/users/{userId}/roleRefs',
                                         ['x_auth_token', 'userId', 'id',
                                          'href', 'tenantId'],
                                         'roleRef', x_auth_token='header',
                                         id='req', href='req', tenantId='req')
    get_role_ref = simplerest.RESTMethod('get_role_ref', 'GET',
                                         '/users/{userId}/roleRefs/{roleId}',
                                         ['x_auth_token', 'userId', 'roleId'],
                                         x_auth_token='header')
    delete_role_ref = simplerest.RESTMethod('delete_role_ref', 'DELETE',
                                            '/users/{userId}/roleRefs/'
                                            '{roleId}',
                                            ['x_auth_token', 'userId',
                                             'roleId'],
                                            x_auth_token='header')
