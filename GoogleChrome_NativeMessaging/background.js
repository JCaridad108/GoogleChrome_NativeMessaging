/* On startup, connect to the "python.native.messaging.app" app.*/
var port = chrome.runtime.connectNative("python.native.messaging.app");

/* Listen for messages from the app. */
port.onMessage.addListener((response) => {
	console.log("Received: " + response);
	var command = response.split(",");
		if(command[0] == "open"){
			createTab(command[1]);
		}else if(command[0] == "close"){
			closeTab(command[1]);
		}else if(command[0] == "switch"){
			switchTab2(command[1]);
		}else if(command[0] == "update"){
			updateURL(command[1]);
		}
});


/* When tab is removed... */
chrome.tabs.onRemoved.addListener((tab) => {
	port.postMessage("Closed Tab")
});


/* When browser opens, launch native program */;
chrome.runtime.onStartup.addListener(() => {
  console.log("Launch Native Program");
  port.postMessage("Launch Native Program");
});


/* function to open tab with given URL */
function createTab(url){
	var tb = chrome.tabs.create(
		{ url: url },
		function(tab){
			console.log("Created Tab with ID: "+tab.id);
			port.postMessage(String(tab.id));
			});
}


/* function to close tab with given tabID */
function closeTab(tabID){
	chrome.tabs.remove(Number(tabID));
	console.log("Closed Tab with ID: "+tabID);
}


/* function to switch to tab with gievn tabID */
function switchTab2(tabid){
	console.log("switching to tabid: " + tabid);
	chrome.tabs.update(Number(tabid), {"active": true}, (tab) => { });
        port.postMessage("Switched to Tab with ID: "+tabid)
}


/* function to update the URL of a tab */
function updateURL(url){
	var newTab = chrome.tabs.update(
		{url: String(url)},
		function(tab){
			console.log("Updated Tab to ID: "+tab.id);
			port.postMessage(String(tab.id));
		});
}

