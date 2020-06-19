### **前端代码规范**

#### Ⅰ.HTML

##### 1.语法规范

- 嵌套的节点应该缩进

- 在属性上，使用双引号，不要使用单引号

- 属性名全小写，用 -(中划线) 做分隔符

- 不自动闭合标签必须闭合

- 不要在自动闭合标签结尾处使用斜线（HTML5 规范 指出他们是可选的）

  ```html
  <!DOCTYPE html>
  <html>
      <head>
          <title>Page title</title>
      </head>
      <body>
          <img src="/static/bg.png" alt="暂无图片">
          <h1 class="hello-world">Hello, world!</h1>
      </body>
  </html>
  ```

##### 2.属性顺序

标签属性应该按照特定的顺序出现以保证易读性（按以下顺序，但重点是前两条）

1. class  class属性是为高可复用组件设计的，所以应处在第一位

2. id  id属性更加具体且应该尽量少使用，所以将它放在第二位

3. name

4. data-*

5. src , for , type , href , value , max-length , max , min , pattern

6. placeholder , title , alt

7. aria-* , role

8. required , readonly , disabled

   

#### **Ⅱ、CSS**

##### **1. 分号**

- 每个属性声明末尾一定加分号

##### 2. 空格

无需空格

- 属性名后
- 多个规则的分隔符 , 前
- !important 中的 ! 后
- 属性值中 （ 后和 ) 前
- 行末不要有多余的空格

需要空格

- 属性值前
- 选择器 > , + , ~ 前后
- 代码块 { 前
- !important 中的 ! 前
- 属性值中的 , 后
- 注释 /* 后和 */ 前

```css
/*not good*/
.element {
    color :red! important;
    background-color: rgba(0,0,0,.5);
}

/* good */
.element {
    color: red !important;
    background-color: rgba(0, 0, 0, 0.5);
}

/* not good */
.element ,
.dialog{
    ...
}

/* good */
.element,
.dialog {

}

/* not good */
.element>.dialog{
    ...
}

/* good */
.element > .dialog{
    ...
}

```

##### 3.空行

} 后跟一个空行

```css
/* not good */
.element {
    ...
}
.dialog {
    ...
}

/* good */
.element {
    ...
}

.dialog {
    ...
}

```

##### 4.换行

无需换行

- { 前

需要换行

- { 后， } 前
- 每个属性独占一行
- 多个规则的分隔符 , 后

```css
/* not good */
.element
{color: red; background-color: black;}

/* good */
.element {
    color: red;
    background-color: black;
}

/* not good */
.element, .dialog {
    ...
}

/* good */
.element,
.dialog {
    ...
}

```

#### **Ⅲ、JavaScript**

##### 1.定义变量

1.1 基本规范

尽量使用 let 进行定义且使用字面量创建对象，（除常量外）变量命名都以类型前缀 + 有意义的单词组成，单词首字母都需要大写，用 驼峰命名法（除第一个字母外，每个单词的首字母大写）
每一个变量声明都应该只对应着一个变量。不应该出现像 let a = 1,b = 2; 这样的语句。

1.2 常量定义

常量一般视为全局变量的一种，定义用 const 且全大写，一经定义不可修改，用 _(下划线) 进行分隔

```javascript
const PI = 3.1415926; // const - 不可重定义 且 无法重新赋值
const BASE_URL = 'http://10.0.2.212:19110'
```

1.3 类的定义

- 请使用 class 进行定义且使用 帕斯卡命名法（每个单词的首字母大写）
- 尽量避免使用 ES5 老语法 function 定义类，易造成混淆

注： 关于 ES6 class类 的学习可以参考 —— MDN上的《 类 》这篇教程

```javascript
class Rectangle {
    //...代码块
}
```

1.4 字符串定义相关

- 定义字符串使用单引号 ‘’ (因为大多时候我们的字符串。特别是html会出现 " )
- 减少字符串的换行和拼接，使用 ES6 语法的 `` 格式化字符串

1.5 特例

- for 等循环语句中定义的 局部变量 ，使用 i, j, k
- 作用域不大 临时变量  可以简写，例如：str, num, bol, obj, arr, fun

##### 2.if 条件判断

- 合理使用三目运算符减少 if 语句的使用
- 避免 if 语句的深层次嵌套

2.1 switch 语句

- switch 适用于条件的值等情况下

- 如果条件较小的话选用 if else 比较合适

- 条件数量较大建议选用 switch

- 大多数的情况下 switch 比 if else 运行的更加快

  案例：滁州项目中通过 sos 字段返回值判断手环的状态

  ```javascript
  // if语句代码如下：
  
  if (rowData.sos == 1) {
      return '进入围栏';
  } else if (rowData.sos == 2) {
      return '出围栏';
  } else if (rowData.sos == 3) {
      return '低电量';
  } else if (rowData.sos == 5) {
      return 'sos告警';
  } else if (rowData.sos == 14) {
      return '离线报警';
  } else if (rowData.sos == 15) {
      return '开机报警';
  } else if (rowData.sos == 16) {
      return '关机报警';
  } else if (rowData.sos == 65) {
      return '脱落报警';
  } else if (rowData.sos == 66) {
      return '蓝牙丢失报警';
  } else if (rowData.sos == 104) {
      return '佩戴报警';
  } else if (rowData.sos == 200) {
      return '温度心率超过阀值报警';
  } else {
      return '-';
  }
  
  // 即便使用if语句，也建议把常用项放到第一位，减少判断次数，譬如rowData.sos == 5
  
  // switch语句代码如下：
  
  switch (rowData.sos) {
      case '1':
          return '进入围栏';
          break;
      case '2':
          return '出围栏';
          break;
      case '3':
          return '低电量';
          break;
      case '5':
          return 'sos告警';
          break;                        
      case '14':
          return '离线报警';
          break;
      case '15':
          return '开机报警';
          break;
      case '16':
          return '关机报警';
          break;
      case '65':
          return '脱落报警';
          break;
      case '66':
          return '蓝牙丢失报警';
          break;
      case '104':
          return '佩戴报警';
          break; 
      case '200':
          return '温度心率超过阀值报警';
          break;                         
      default :
          return '-';
  }
  
  // 可读性相对if语句更高
  
  ```

2.2 推荐解决方案

- 针对日常开发中类似问题，推荐统一使用书写和阅读更为明了易懂的 数组 / 对象字面量方法

```javascript
 // 例1：
 // 后台返回字段 fruit 该字段返一个数字 
 // 0 = 苹果, 1 = 梨子, 2 = 桔子, 3 = 柠檬, 4 = 芒果...
 let aFruit = ['苹果', '梨子', '桔子', '柠檬', '芒果'];
 let sFruit = aFruit[fruit];
 console.log(sFruit);

 // 例2：
 // 用对象方法解决上述的 if / switch 案例，后台传入rowData.sos前端体现状态
 let oWatchStatus = {
     "1": "进入围栏",
     "2": "出围栏",
     "3": "低电量",
     "5": "sos告警",
     "14": "离线报警",
     "15": "开机报警",
     "16": "关机报警",
     "65": "脱落报警",
     "66": "蓝牙丢失报警",
     "104": "佩戴报警",
     "200": "温度心率超过阀值报警"
 }
 return oWatchStatus[rowData.sos];

```

##### 3.注释

3.1 注释原则

- **As short as possible（如无必要，勿增注释）**：尽量提高代码本身的清晰性、可读性
- **As long as necessary（如有必要，尽量详尽）**：合理的注释、空行排版等，可以让代码更易阅读、更具美感

3.2 单行注释

- // 后跟一个空格，缩进与下一行被注释说明的代码一致，最好独占一行
- 避免使用 /*…*/ 这样的多行注释
- 有多行注释内容时，请使用多个单行注释

```javascript
例1：				
// not good：
map.centerAndZoom(point, 16); //初始化地图,设置中心点坐标和地图级别

// good：
map.centerAndZoom(point, 16); // 初始化地图,设置中心点坐标和地图级别

// perfect：
// 初始化地图,设置中心点坐标和地图级别
map.centerAndZoom(point, 16);
例2：
// not good： --> 多行注释
/*label.setStyle({
    position: "relative",
    border: "1px solid rgb(204, 204, 204)",
    color: "rgb(0, 0, 0)",
    textAlign: 'center',
    borderRadius: "10px",
    padding: "5px",
    background: "rgb(255, 255, 255)",
});*/


// good： --> 分行注释
// label.setStyle({
//     position: "relative",
//     border: "1px solid rgb(204, 204, 204)",
//     color: "rgb(0, 0, 0)",
//     textAlign: 'center',
//     borderRadius: "10px",
//     padding: "5px",
//     background: "rgb(255, 255, 255)",
// });

```

3.3 函数 / 方法注释

- 函数 / 方法注释必须包含函数说明，有参数和返回值时必须使用注释标识
- 参数和返回值注释必须包含类型信息和说明
  - @description： 本方法作用的描述
  - @method ： 方法名（可写 / 可不写）
  - @author ： 编写者的名字（方便找到编写者快速解决问题）
  - @param {参数的数据类型} 参数1： 参数1的说明
  - @param {参数的数据类型} 参数2： 参数2的说明
  - @return {返回值的数据类型}： 返回值描述

```javascript
/**
* @description : 通过设置面板设置该元素css属性
* @method setCss
* @param {string} key : css的key值
* @param {any} value : css的value值 / 若flag为true -- 为携带value值的dom元素
* @param {boolean} flag : 用于区分传入的是否是需要正则转换的对象
*/
function setCss(key, value, flag) {
    if (!flag) {
        switch (key) {
            case "cycleNum":
                if (value) {
                    $("#imageCyclesCount").attr("disabled", "disabled");
                    value = "infinite";
                } else {
                    $("#imageCyclesCount").removeAttr("disabled");
                    var aniNum = $("#imageCyclesCount").val();
                    aniNum == "" ? value = 0 : value = aniNum;
                }
                break;
        }
        Widget.widgetData.currentObject.setProperty(key, value);
    } else {
        // 当echarts组件调用该方法时传入true
        Widget.widgetData.currentObject.setProperty(key, value, true);
    }
}

```

拓展：for…of 的对象遍历

```javascript
varobj = {
    name: "hello",
    age: "18"
};
for(var i of Object.keys(obj)){
    console.log(i);
    // name
    // age
}
for(var i of Object.values(obj)){
    console.log(i);
    // hello
    // 18
}
for(var i of Object.entries(obj)){
    console.log(i);
    // ["name", "hello"]
    // ["age", "18"]
}

```

##### 4.代码书写规范

4.1 分号

- 每个语句以分号结尾，不可依赖于JS自动添加分号的功能（return）
- 代码块 ｝ 后不加分号

注：想要 return 的值，不可换行书写

```javascript
return
"<div class='ace-widget parentdiv' style='" + style + "'>" +
    "	 <style>" + keyFrames + "</style>" +
    "	 <div style='overflow: hidden;width: 100%;height: 100%'>" +
    "	 <div class='f-family'>" + this.nodeProperties.text +
    "	 	 </div>" +
    "	 </div>" +
    "</div>";
// 该段程序运行报错，就是JS自动添加分号的功能造成的，直接解析为 return;中断代码执行

```

解决办法：

```javascript
return	"<div class='ace-widget parentdiv' style='" + style + "'>" +
    "	 <style>" + keyFrames + "</style>" +
    "	 <div style='overflow: hidden;width: 100%;height: 100%'>" +
    "	 <div class='f-family'>" + this.nodeProperties.text +
    "	 	 </div>" +
    "	 </div>" +
    "</div>";

```

4.2 空格

- 非末尾符号后加，运算、赋值等前后加空格

```javascript
let sUserName = 'Jack';

for (let i = 0; i < aMyArray.length; i ++) {...}

let oUser = {
    name: 'Tom',
    age: 15,
    hobbies: [
        reading: true,
        writing: false,
    ]
}

1 == 0 ? console.log(123) : console.log(456);

```

4.3 统一用词规范

- 在函数嵌套时，为了改变 this 的指向，统一使用 that 承接

  （现有代码中很多使用 _this 或 _self 不统一，且书写相对困难）

尽可能的使用 箭头函数 ，防止 this 指向发生改变而导致需要重新定义变量

```javascript
const that = this;
```

4.4 Axios 之后的链式写法

- 使用箭头函数时，无论参数的个数，都用 () 进行包裹，且 => 前后必须加空格
- .then / .catch 等类似链式写法包括其后的箭头函数，在 { 前统一不换行

```javascript
// not good -- 此段代码极其不规范
const validateExsit=(rule, value, callback) => {
	this.$axios({
		method:'get',
		params:{name:value},
		url:'/maintKind/isNameExists'
	})
    .then(
    	res=>{
        	let status=res
            if(status!=true) {
            	callback(new Error('该物种已存在'));
            }
            else{
                callback()
            }                         
        }
    )
};

// good
const validateExsit = (rule, value, callback) => {
	this.$axios({
		method: 'get',
	    params: {
	        name: value
	    },
	    url: '/maintKind/isNameExists'
	}).then((res) => {
	    let status = res;
	    if (status!=true) {
	        callback(new Error('该物种已存在'));
	    } else {
	        callback();
	    }
	}).catch((rej) => {
		console.log(rej);
	});
}

```

4.5 setTimeout / setInterval

- 清除计时器请使用对应的方法：clearTimeout / clearInterval 语义更明确
- 若非必须无限计时的计时器，请在使用完毕后清除
- 请按照规范书写计时器的格式

```javascript
setTimeout(function () {
      console.log('Hello World')
}, 1000)

```

