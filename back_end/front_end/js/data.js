// 柱状图模块1
(function() {
	// 1实例化对象
	var myChart = echarts.init(document.querySelector("#usage"));
	// 2. 指定配置项和数据
	option = {
		title: {
			text: '平均消除验证码时间(s)'
		},
		color: ['#3398DB'],
		tooltip: {
			trigger: 'axis',
			axisPointer: {            // 坐标轴指示器，坐标轴触发有效
				type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
			}
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis: [
			{
				type: 'category',
				data: ['每天上网', '每周上网', '每月上网'],
				axisTick: {
					alignWithLabel: true
				}
			}
		],
		yAxis: [
			{
				type: 'value'
			}
		],
		series: [
			{
				name: '直接访问',
				type: 'bar',
				barWidth: '60%',
				data: [8.3, 12.7, 10.5]
			}
		]
	};
	// 3. 把配置项给实例对象
	myChart.setOption(option);
	// 4. 让图表跟随屏幕自动的去适应
	//window.addEventListener("resize", function() {
	 // myChart.resize();
	//});
  })();