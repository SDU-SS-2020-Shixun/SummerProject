function uploadFile() {
	var xmlHttp;
	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlHttp.open('post', '/aciton/upload.py', true);//upload.py用于上传验证码 并返回识别结果
	xmlHttp.send();
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState === 4 && xmlHttp.state === 200) {
			alert(xmlHttp.responseTest); //xmlHttp.responseTest是验证码结果
		}
	}
}
function changetip() {
	var fileInput = document.getElementById('file');
	var tip = document.getElementById('tip');
	tip.innerHTML = fileInput.value;
}
function gores(){
	var xmlHttp;
	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlHttp.open('post', '/aciton/makeyzm.py', true);//makeyzm.py用于自动生成验证码 并返回 验证码所存路径
	xmlHttp.send();
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState === 4 && xmlHttp.state === 200) {
			document.getElementById("myyzm").src = xmlHttp.responseText;
		}
	}
}
function work() {
	var xmlHttp;
	if (window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	} else {
		xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
	}
	xmlHttp.open('post', '/aciton/vyzm.py', true);//vyzm.py用于识别验证码并返回识别结果
	xmlHttp.send();
	xmlHttp.onreadystatechange = function() {
		if (xmlHttp.readyState === 4 && xmlHttp.state === 200) {
			alert(xmlHttp.responseTest); //xmlHttp.responseTest是验证码结果
		}
	}
}


