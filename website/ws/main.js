
var count = 0;

var ws = new WebSocket("ws://aqueous-bayou-7324.herokuapp.com");
ws.onopen = function() {onOpen()};

function onOpen() {
	if(ws.readyState == 1)
	{
		document.getElementById("status").innerHTML = "Connected";
		document.getElementById("input").contentEditable = "true";
		document.getElementById("buttonC").disabled = false;			
	}
};

ws.onclose = function(evt) {onClose()};

function onClose() {
	ws.close();
	document.getElementById("status").innerHTML = "Disconnected";
	document.getElementById("input").contentEditable = "false";
	document.getElementById("buttonC").disabled = true;
};

ws.onmessage = function(evt) {
	var msg = String(evt.data);
	var text = document.createTextNode(msg);
	display_message(msg);
};

function create_wrapper() {
	var temp = document.createElement("div");
	temp.setAttribute("id","msg_wrapper");
	return temp;
}

function create_time() {
	var d = new Date();
	var h = d.getHours();
	var m = d.getMinutes();
	var s = d.getSeconds();
	var meridian = 'am';
	if(h > 12) {
		h = h % 12;
		meridian = 'pm';
	}

	var t = h + ":" + m + ":" + s + " " + meridian;
	return t;
}

function display_message(msg) {
		msg = document.createTextNode(msg);
		var target = document.getElementById("display");
		var br = document.createElement("br");
		var hr = document.createElement("hr");
		hr.setAttribute("align","center");
		var t = create_time();
		t = document.createTextNode(t);
		var inner_block = create_wrapper();

		var time_wrapper = document.createElement("div");
		time_wrapper.setAttribute("id","time_wrapper");

		inner_block.appendChild(msg);
		inner_block.appendChild(br);
		inner_block.appendChild(hr);
		inner_block.appendChild(br);
		time_wrapper.appendChild(t);
		inner_block.appendChild(time_wrapper);
		target.appendChild(inner_block);
		target.appendChild(br);
		target.scrollTop = target.scrollHeight;
}

function send_msg() {
	var box = document.getElementById("input");
	msg = String(box.textContent);
	if(count === 0) {
		msg = msg.slice(0,msg.length);
	}
	if(msg) {
		ws.send(msg);
		msg = "You >> " + msg;
		box.innerHTML = "";
		display_message(msg);
		document.getElementById("input").focus();
		count++;
	}
};

function check_rtn(e) {
	var key = e.keycode || e.which;
	if(key == 13) {
		send_msg();
	}
};
