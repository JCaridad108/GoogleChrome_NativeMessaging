
# Requirements
* Python 3
* Mac
* Google Chrome

# Files
* main_program.py : Main Program
* BrowserExtension/Chrome_NativeMessaging.py : native program.
* BrowserExtension/manifest.json : Chrome extension manifest.
* BrowserExtension/background.json : JavaScript ran by extension to communicate with native app.
* BrowserExtension/python.native.messaging.app.json : native app manifest that gives it'sextension the location of the app.
* bin/organize : bash script that moves the native program and native messaging host to correct locations 

# File Locations

* Chrome_NativeMessaging.py : place in /Applications directory. Certain permissions
	specific to MacOS allows Chrome to run this only when it is in this directory. 

* python.native.messaging.app.json : place in ~/Library/Application Support/Google/Chrome/NativeMessagingHosts/

# Before running

Give bin/organize executable permission and run that. Alternatively, move the native program and native messaging
host to the locations specified above.

Go to the extensions page in Chrome and turn on developer mode (top right). Click "Load unpacked", then select
the folder containing manifest.json. Now the extension is loaded. In python.native.messaging.app.json, the
extension ID in "allowed_origins" between the / and // must be replaced with the unique extension ID assigned
when the extension is loaded in Chrome. Close the extension page.

# Launching

Run main_program.py to begin. This will launch the Google Chrome application and automatically run the extension.
The main_program is now communicating with the Native Program, which is communicating with the browser.

To open a page, enter a command like "open,<url>" with a desired URL. The program updates the user with Tab IDs 
corresponding to each tab opened. To close a tab enter a command like "close,<TabID>" with the corresponding
Tab ID. To switch to another tab. To switch to another tab, enter a command like "switch,<TabID>". To close 
the program, enter "quit".
