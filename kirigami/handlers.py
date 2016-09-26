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

import kirigami.tagger
import kirigami.settings


def auth_handler(r, settings, logging):
    ttl = int(settings.get('ttl', '60'))

    user = settings['main']['user']
    if not user:
        user = kirigami.tagger.retrieve_user()

    passwd = settings['main']['password']
    if not passwd:
        passwd = kirigami.tagger.retrieve_password()

    args = (user, passwd, ttl)
    r.auth_user(args)


def message_handler(r, settings, logging):
    messages = r.user_messages()
    for msg in messages:
        msg = msg.replace('\r\n', ' ')
        logging.info('Server Says: %s', msg)


def expiration_handler(r, settings, logging):
    logging.info('Password Timeout')


def balance_handler(r, settings, logging):
    balance = r.user_balance()
    logging.info('Balance Updated: %s', balance)


def bug_handler(r, settings, logging):
    logging.critical('Received a message not implemented.')
