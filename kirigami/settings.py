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

import configparser
import kirigami.tagger


def parse_config(location, logger):
    settings = {}

    config = configparser.ConfigParser()
    config.read(location)

    if not config.has_section('MAIN'):
        try:
            write_config(logger)
            config.read(location)
        except BaseException:
            logger.critical("Could not write config. ")
            exit(1)

    main = config['MAIN']

    values = {}

    values['user'] = main.get('user', None)
    values['password'] = main.get('password', None)
    values['hostname'] = main.get('hostname', 'print')
    values['proto'] = main.get('proto', 'http')
    values['port'] = main.get('port', '9191')

    settings['main'] = values

    return settings


def write_config(logger):
    config = configparser.RawConfigParser()

    username = kirigami.tagger.retrieve_user()

    config.add_section('MAIN')
    config.set('MAIN', 'user', username)
    config.set('MAIN', 'hostname', 'gutenberg.simons-rock.edu')
    config.set('MAIN', 'proto', 'http')
    config.set('MAIN', 'port', '9191')
    config.set('MAIN', 'ttl', '60')

    with open('.kirigami.conf', 'w') as configfile:
        config.write(configfile)

    logger.debug("Config written. ")
