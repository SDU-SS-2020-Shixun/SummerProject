function uploadFile() {
	var formData = new FormData();
	var file = document.getElementById('file').files[0];
	formData.append("img", file);
	$.ajax({
	    url: "/imgProcess/upload",
	    type: "post",
	    data: formData,
	    dataType: "json",
	    cache: false,
	    processData: false,
	    contentType: false, 
	    success: function (data) {
			if(data.code==200)
				alert(data.imgCode);
			else
				alet("分析失败！");
	    }
	});
}
function changetip() {
	var fileInput = document.getElementById('file');
	var tip = document.getElementById('tip');
	tip.innerHTML = fileInput.value;
}
var timgCode;
function gores(){
	var formData = new FormData();
	$.ajax({
	    url: "/imgProcess/createImg",
	    type: "post",
	    data: formData,
	    dataType: "json",
	    cache: false,
	    processData: false,
	    contentType: false, 
	    success: function (data) {
			if(data.code==200)
				$("#myyzm").attr("src",data.img);
				timgCode=data.imgCode;
			else
				alet("生成失败！");
	    }
	});
}
function work() {
	alert(timgCode);
}


