#!/usr/bin/env bash

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

