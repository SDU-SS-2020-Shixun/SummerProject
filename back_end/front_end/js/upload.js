function uploadFile() {
	var formData = new FormData();
	var file = document.getElementById('file').files[0];
	formData.append("img", file);
	$.ajax({
	    url: "http://127.0.0.1:8000/imgProcess/upload",
	    type: "post",
	    data: formData,
		dataType: "json",
	    cache: false,
	    processData: false,
	    contentType: false,
	    success: function (data) {
			if(data.code==200){
                $("#resar").text(data.imgCode1);
                $("#resbr").text(data.imgCode2);
                $("#resar").css("display","block");
                $("#resbr").css("display","block");
                $("#resar").css("opacity","1");
                $("#resbr").css("opacity","1");
            }
			else
				alert("分析失败！");
	    },
		error:function(err){
			alert("请求失败！")
		},
		beforeSend:function(){
			$("#shadowl").addClass("notclick");
			$("#submitl").addClass("notclick");
		},
		complete:function(){
			$("#shadowl").removeClass("notclick");
			$("#submitl").removeClass("notclick");
		}
	});
}
function changetip() {
	var fileInput = document.getElementById('file');
	var tip = document.getElementById('tip');
	tip.innerHTML = fileInput.value;
}
function gores(){
	var formData = new FormData();
	var parpath="../media/";
	$.ajax({
		url: "http://127.0.0.1:8000/imgProcess/createImg",
	    type: "post",
	    data: formData,
	    dataType: "json",
	    cache: false,
	    processData: false,
	    contentType: false,
		success: function (datas) {
			data = eval(datas)
			console.log(data)
			if(data.code==200){
                $("#resimg").attr("src",parpath+data.img);
                $("#resal").text(data.imgCode1);
                $("#resbl").text(data.imgCode2);
                $("#resal").css("display","block");
                $("#resbl").css("display","block");
                $("#resal").css("opacity","1");
                $("#resbl").css("opacity","1");
            }
			else
				alert("分析失败！");
		},
		error:function(err){
			alert("请求失败！")
		},
		beforeSend:function(){
			$("#shadowr").addClass("notclick");
			$("#submitr").addClass("notclick");
		},
		complete:function(){
			$("#shadowr").removeClass("notclick");
			$("#submitr").removeClass("notclick");
		}
	});
}
function work() {
	alert(timgCode);
}


