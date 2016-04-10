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

import asyncio
import logging
import sys

import kirigami.tagger
import kirigami.settings
from .handlers import *
from .connection import Remote



def main(r, settings):
    while True:
        logging.debug("Getting Actions from Remote.")
        actions = r.pending_actions()

        if actions:
            for action in actions:
                logging.debug("Recieved Action %s", action)
                controller(action)(r, settings, logging)


def controller(event):
    events = {
        'AuthenticationRequested': auth_handler,
        'UserMessages': message_handler,
        'AuthenticationExpired': expiration_handler,
        'BalanceUpdate': balance_handler
    }
    return events.get(event, bug_handler)

def cli():
    log = {
        'format': '%(asctime)s - %(levelname)s %(message)s',
        'level': logging.DEBUG
    }
    logging.basicConfig(**log)

    logging.info("Parsing Configuration from .kirigami.conf")
    settings = kirigami.settings.parse_config('.kirigami.conf', logging)

    identity = kirigami.tagger.identity()
    logging.debug("Identity tagged as %s", identity)

    r = Remote(settings['main'], identity)

    try:
        main(r, settings)
    except KeyboardInterrupt:
        print("Exiting...")
