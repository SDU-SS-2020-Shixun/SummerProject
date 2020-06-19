$(document).ready(function () {
	$("#shadowl").addClass("notclick");
	$("#submitl").addClass("notclick");
	$("#shadowr").addClass("notclick");
	$("#submitr").addClass("notclick");
});

function leftchange() {
	$("#left_title").css("top", "0");
	$("#left_title").css("left", "0");
	$("#left_btn").css("opacity", "0");
	$("#left-btn").css("z-index", "0");
	$("#shadowl").css("opacity", "1");
	$("#submitl").css("opacity", "1");
	$("#right_title").text("结果展示:");
	$("#right_title").css("top", "0");
	$("#right_title").css("left", "0");
	$("#right_btn").css("opacity", "0");
	$("#en-title").css("opacity", "0");
	$("#cn-title").css("top", "-35px");
	$("#left_btn").addClass("notclick");
	$("#right_btn").addClass("notclick");
	$("#shadowl").removeClass("notclick");
	$("#submitl").removeClass("notclick");
	$("#startone").css("left", "5%");
	$("#planar").css("display", "block");
	$("#planbr").css("display", "block");
	$("#planar").css("opacity", "1");
	$("#planbr").css("opacity", "1");
}

function rightchange() {
	$("#right_title").css("top", "0");
	$("#right_title").css("left", "0");
	$("#right_btn").css("opacity", "0");
	$("#shadowr").css("opacity", "1");
	$("#submitr").css("opacity", "1");
	$("#right-btn").css("z-index", "0");
	$("#left_title").text("结果展示:");
	$("#left_title").css("top", "0");
	$("#left_title").css("left", "0");
	$("#left_btn").css("opacity", "0");
	$("#en-title").css("opacity", "0");
	$("#cn-title").css("top", "-35px");
	$("#left_btn").addClass("notclick");
	$("#right_btn").addClass("notclick");
	$("#shadowr").removeClass("notclick");
	$("#submitr").removeClass("notclick");
	$("#startone").css("left", "50%");
	$("#planal").css("display", "block");
	$("#planbl").css("display", "block");
	$("#planal").css("opacity", "1");
	$("#planbl").css("opacity", "1");
}
