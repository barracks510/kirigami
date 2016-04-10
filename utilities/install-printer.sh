#!/usr/bin/env bash
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

PRINTERNAME='PrintCentral'
PRINTERMODEL='HP LaserJet 4200'
PRINTERLOCATION='lpd://print/central'
PRINTERDRIVER='gutenprint.5.2://hp-lj_4200/expert'
LOCATION="Bard College at Simon's Rock"

if [[ $EUID -ne 0 ]]; then
	echo "You must be root user to install a printer."
	exit 1
fi

if [[ $PRINTERDRIVER == '' ]]; then
	echo "Looking for appropriate drivers..."
	PRINTERDRIVER=$(lpinfo --make-and-model "$PRINTERMODEL" -m | head -n 1 | cut -d \  -f 1)
	echo "Found $PRINTERDRIVER for $PRINTERMODEL."
fi

echo "Installing $PRINTERNAME..."
lpadmin \
	-p "$PRINTERNAME" \
	-v "$PRINTERLOCATION" \
	-m "$PRINTERDRIVER" \
	-L "$LOCATION" \
	-E
if [[ $? -eq 0 ]]; then
	echo "Success."
else
	echo "Failed. With error $?."
fi

