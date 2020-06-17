var fil;
function uploadFile() {
	var formData = new FormData();
	fil = document.getElementById('file').files[0];
	formData.append("img", fil);
	$.ajax({
		url: "http://"+window.location.host+"/imgProcess/upload",
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
function gores(){
	var formData = new FormData();
	var parpath="../media/";
	console.log(window.location.host);
	$.ajax({
		url: "http://"+window.location.host+"/imgProcess/createImg",
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
window.onload = function(){  
     var uuz = document.getElementById('shadowl');  
     uuz.ondragenter = function(e){  
         e.preventDefault();  
     }  

     uuz.ondragover = function(e){  
         e.preventDefault();  
    }  

     uuz.ondragleave = function(e){  
         e.preventDefault();  
     }  
     uuz.ondrop = function(e){  
         e.preventDefault();  
         fil = e.dataTransfer.files[0]; //获取要上传的文件对象(可以上传多个)  
		 var fr = new FileReader();
		 fr.readAsDataURL(fil);
		 fr.onload=function(e){
		 	console.log(this.result);
		 	$("#hxian").css("display","block");
		 	$("#hximg").attr("src",e.target.result);
		 	$(".fake").css("display","none");
			$("#tix").css("display","none");
		 	// $("#hxian").css("background-image","url(this.result)");
		 }
     }
 }


