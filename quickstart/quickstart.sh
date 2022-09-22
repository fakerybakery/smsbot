#!/bin/bash
echo "SMSBot Quickstart by mrfakename"
echo "Checking for updates..."
NEWEST_VERSION=$(curl "https://raw.githubusercontent.com/fakerybakery/smsbot/main/src/main.py")
CURRENT_VERSION=$(cat main.py)
echo "Checking for updates..."
if CURRENT_VERSION != NEWEST_VERSION then
echo "You are on the latest version."
echo "Starting server..."
/usr/bin/python3 main.py
else
echo "An update is available! Now updating files..."
curl "https://raw.githubusercontent.com/fakerybakery/smsbot/main/src/main.py" >> main.py
ScriptLoc=$(readlink -f "$0")
echo "Updated! Restarting script..."
echo "& * & * & * & * & * & * & *"
exec "$ScriptLoc"
fi
