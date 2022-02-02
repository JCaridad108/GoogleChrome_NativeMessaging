# Files
* Chrome_NativeMessaging.py : native program.
* manifest.json : Chrome extension manifest.
* background.json : JavaScript ran by extension to communicate with native app.
* python.native.messaging.app.json : native app manifest that gives it's extension the location of the app.

# File Locations

* Chrome_NativeMessaging.py : place in /Applications directory. Certain permissions
	specific to MacOS allows Chrome to run this only when it is in this directory. 

* python.native.messaging.app.json : place in ~/Library/Application Support/Google/Chrome/NativeMessagingHosts/

# Launching

Go to the extensions page in Chrome and turn on developer mode (top right). Click "Load unpacked", then select
the folder containing manifest.json. Now the extension is loaded. In python.native.messaging.app.json, the
extension ID in "allowed_origins" between the / and // must be replaced with the unique extension ID assigned
when the extension is loaded in Chrome. Close the extension page.

