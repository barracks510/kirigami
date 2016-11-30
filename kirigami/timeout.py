#
# Copyright (c) 2016 Dennis Chen
# Copyright (c) 2016 Vijay Pillai
#
# This file is part of Kirigami
#
# Kirigami is free software: you can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Kirigami is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Kirigami.  If not, see <http://www.gnu.org/licenses/>.
#

# This code with serious modification from:
# http://blog.bjola.ca/2007/08/using-timeout-with-xmlrpclib.html

import xmlrpc.client
import http.client


def ServerProxy(url, *args, **kwargs):
    t = TimeoutTransport()
    # Typical response time from the RPC long-poll are 90 seconds in length.
    t.timeout = kwargs.get('timeout', 300)
    if 'timeout' in kwargs:
        del kwargs['timeout']
    kwargs['transport'] = t
    server = xmlrpc.client.ServerProxy(url, *args, **kwargs)
    return server


class TimeoutTransport(xmlrpc.client.Transport):
    user_agent = 'print-central/kirigami'

    def make_connection(self, host):
        # return an existing connection if possible.  This allows HTTP/1.1
        # keep-alive.
        if self._connection and host == self._connection[0]:
            return self._connection[1]
        # create a HTTP connection object from a host descriptor
        chost, self._extra_headers, x509 = self.get_host_info(host)

        self._connection = host, http.client.HTTPConnection(chost, timeout=self.timeout)
        return self._connection[1]
