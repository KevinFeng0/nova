# Copyright 2012 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from webob import exc

from nova.api.openstack.compute.schemas import fixed_ips as schema_fixed_ips
from nova.api.openstack import wsgi
from nova.api import validation


class FixedIPController(wsgi.Controller):

    @wsgi.expected_errors((410))
    def show(self, req, id):
        raise exc.HTTPGone()

    @wsgi.expected_errors((410))
    @wsgi.action('reserve')
    @validation.schema(schema_fixed_ips.reserve)
    def reserve(self, req, id, body):
        raise exc.HTTPGone()

    @wsgi.expected_errors((410))
    @wsgi.action('unreserve')
    @validation.schema(schema_fixed_ips.unreserve)
    def unreserve(self, req, id, body):
        raise exc.HTTPGone()
