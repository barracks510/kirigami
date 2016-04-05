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

import netifaces
import socket
import getpass


def identity():
    user = getpass.getuser()
    hostname = socket.gethostname()
    ipaddrs = []
    for interface in netifaces.interfaces():
        try:
            for addr in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                ipaddrs.append(addr['addr'])
        except KeyError:
            pass
        try:
            for addr in netifaces.ifaddresses(interface)[netifaces.AF_INET6]:
                ipaddrs.append(addr['addr'])
        except KeyError:
            pass
    ip = ','.join(ipaddrs)
    return (user, hostname, ip)


def retrieve_user():
    user = input("Username: ")
    password = getpass.getpass()
    return (user, password)
