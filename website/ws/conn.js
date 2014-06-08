conn_ws = new WebSocket("ws://aqueous-bayou-7324.herokuapp.com/connected");
conn_ws.onopen = function(){onConnOpen()};
conn_ws.onmessage = function(message){
	var persons = "";
	var block = document.getElementById("in_conn");
	var list = JSON.parse(message["data"]);
	for(var i in list) {
		persons += list[i] + "<br>";
	}
	block.innerHTML = persons;
};

function onConnOpen() {
	var on = document.getElementById("connected");
}

callback = function get_status() {
	conn_ws.send('get');
}

setInterval(callback,3000);
