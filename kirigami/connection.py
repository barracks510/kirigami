#
# Copyright (c) 2016 Dennis Chen
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

import xmlrpc.client

class Remote(object):
    """
    A Remote instance represents a connection to a remote PaperCut Server.

    Remote instances are created everytime a new connection to a server is
    required. Most Remote instances can be renewed by pinging the remote
    every so often.
    """
    __connection = None

    __hostname = None
    __port = 9191
    __proto = "http"
    __user = None

    __identity = None

    def __init__(self, settings, identity):
        """
        Initialize a Remote instance with a settings dictionary

        :param settings: a dictonary of settings
        :param identiy: a 3-ple of identiy strings.
        """
        self.__hostname = settings["hostname"]
        self.__port = settings["port"]
        self.__proto = settings["proto"]

        args = (self.__proto , self.__hostname, self.__port)
        target = "{}://{}:{}/rpc/clients/xmlrpc".format(*args)
        self.__connection = xmlrpc.client.ServerProxy(target)

        self.__user = settings["user"]
        self.__identity = identity

    def ping(self):
        return self.__connection.client.ping()

    def pending_actions(self):
        actions = self.__connection.client.getPendingActions(*self.__identity)
        return actions

    def auth_user(self, userparams):
        args = list(self.__identity)
        for value in userparams:
            args.append(value)
        auth = self.__connection.client.authenticateUser(*args)

    def user_messages(self):
        msg = self.__connection.client.getUserMessages(*self.__identity)
        return msg
