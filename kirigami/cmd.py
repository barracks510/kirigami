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
from kirigami.connection import Remote


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


#@asyncio.coroutine
def main():
    while True:
        logging.debug("Getting Actions from Remote.")
        actions = r.pending_actions()

        if actions:
            for action in actions:
                logging.debug("Recieved Action %s", action)
                controller(action)()


def controller(event):
    return {
        'AuthenticationRequested': auth_handler,
        'UserMessages': message_handler,
        'AuthenticationExpired': expiration_handler
    }.get(event, bug_handler)


def auth_handler():
    ttl = int(settings.get('ttl', '60'))
    user = kirigami.tagger.retrieve_user()
    args = list(user)
    args.append(ttl)
    r.auth_user(args)


def message_handler():
    messages = r.user_messages()
    for msg in messages:
        logging.debug("Server Says: %s", msg)


def expiration_handler():
    logging.info("Password Timeout")


def bug_handler():
    logging.critical("Received a message not implemented.")


def cli():
    #loop = asyncio.get_event_loop()
    try:
        #    loop.run_forever()
        main()
    except KeyboardInterrupt:
        print("Exiting...")
    #    loop.stop()
    # loop.close()
