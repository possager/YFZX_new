#_*_coding:utf-8_*_

from bs4 import BeautifulSoup
import requests

text1111112='''

<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="zh-CN" http-equiv="content-language"/>
<meta content="讲座,预告,书店,城市" name="Keywords"/>
<meta content="一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？" name="Description"/>
<meta content="width=device-width, initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no" name="viewport"/>
<meta content="max-age=1700" http-equiv="Cache-control"/>
<meta content="no" name="apple-mobile-web-app-capable"/>
<meta content="black" name="apple-mobile-web-app-status-bar-style"/>
<meta content="telephone=no" name="format-detection"/>
<meta content="yes" name="apple-touch-fullscreen"/>
<meta content="on" http-equiv="cleartype"/>
<title>一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？_翻书党_澎湃新闻-The Paper</title>
<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(2),u=e(3),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}finally{f.emit("fn-end",[c.now()],t)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now()])}},{}],2:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],3:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],4:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=m(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){v[e]=m(e).concat(n)}function m(e){return v[e]||[]}function w(e){return p[e]=p[e]||o(t)}function g(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var v={},y={},b={on:l,emit:t,get:w,listeners:m,context:n,buffer:g,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(2),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=h.info=NREUM.info,n=d.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+h.offset],null,"api");var t=d.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===d.readyState&&i()}function i(){f("mark",["domContent",a()+h.offset],null,"api")}function a(){return E.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-h.offset}var u=(new Date).getTime(),f=e("handle"),c=e(2),s=e("ee"),p=window,d=p.document,l="addEventListener",m="attachEvent",w=p.XMLHttpRequest,g=w&&w.prototype;NREUM.o={ST:setTimeout,SI:p.setImmediate,CT:clearTimeout,XHR:w,REQ:p.Request,EV:p.Event,PR:p.Promise,MO:p.MutationObserver};var v=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1044.min.js"},b=w&&g&&g[l]&&!/CriOS/.test(navigator.userAgent),h=n.exports={offset:u,now:a,origin:v,features:{},xhrWrappable:b};e(1),d[l]?(d[l]("DOMContentLoaded",i,!1),p[l]("load",r,!1)):(d[m]("onreadystatechange",o),p[m]("onload",r)),f("mark",["firstbyte",u],null,"api");var x=0,E=e(4)},{}]},{},["loader"]);</script><link href="http://file.thepaper.cn/wap/v3/img/deskicon.png" rel="apple-touch-icon" sizes="64x64"/>
<link href="http://file.thepaper.cn/wap/v3/img/thepaper.ico" rel="icon"/>
<link href="http://file.thepaper.cn/wap/v3/css/main.css?v=4.9.2" rel="stylesheet" type="text/css"/>
<link href="http://file.thepaper.cn/wap/v3/css/rest.css?v=4.9.2" rel="stylesheet" type="text/css"/>
<link href="http://file.thepaper.cn/wap/v3/css/homepage.css?v=4.9.2" rel="stylesheet"/>
<link href="http://file.thepaper.cn/wap/v3/css/newsinfo.css?v=4.9.2" rel="stylesheet"/>
<link href="http://file.thepaper.cn/wap/v3/css/hotqa.css?v=4.9.2" rel="stylesheet"/>
<link href="http://file.thepaper.cn/wap/v3/css/base.css?v=4.9.2" rel="stylesheet"/>
<link href="http://file.thepaper.cn/wap/v3/css/head.css?v=4.9.2" rel="stylesheet"/>
<style>
	.zt-head{margin-top:0px;}
.FTS-opt{top:0px;}
.tu-list2{margin-bottom:0px;}

</style>
<script src="http://file.thepaper.cn/wap/v3/js/jquery-1.8.3.min.js" type="text/javascript"></script>
<script src="http://file.thepaper.cn/wap/v3/js/main-1.1.js?v=4.9.2" type="text/javascript"></script>
<script src="http://file.thepaper.cn/wap/v3/js/main-1.2.js?v=4.9.2" type="text/javascript"></script>
<script src="http://file.thepaper.cn/wap/v3/js/header.js?v=4.9.2" type="text/javascript"></script>
<script src="http://file.thepaper.cn/wap/v3/js/sp.js??v=4.9.2" type="text/javascript"></script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?d07e4d64d5cde19b5351e7032beaef1a";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
!function(e, n) {
	var t, i = n.documentElement, a = i.dataset.designWidth || 640, o = "orientationchange" in window ? "orientationchange"
			: "resize";
	/iphone|ipod|ipad/gi.test(navigator.userAgent)
			&& i.classList.add("iosx" + e.devicePixelRatio);
	var r = function() {
		var e = Math.min(i.clientWidth, a);
		t = e / a * 100, i.style.fontSize = t + "px"
	};
	r(), e.px2rem = function(e) {
		return parseFloat(e) / 100
	}, e.rem2px = function(e) {
		return parseFloat(e) * t
	}, e.addEventListener(o, r, !1)
}(window, document)
</script>
</head>
<body>
<!--01-->
<div class="header-v4">
<!-- logo -->
<div class="header-container">
<h1 class="logo">
<a class="login" href="http://m.thepaper.cn/" title="pengpai"></a>
<!-- 竖线 -->
<span class="logon-shuline"></span>
<!-- 预留文字位 -->
</h1>
</div>
<!-- hanbao 默认状态-->
<div class="burger-abox">
<a class="burger-a" data-moblink="demo/a?contType=2&amp;contId=1787647" id="moblink_top_detail_xiazai" moblink-featured="">下载APP</a>
</div>
<div class="burger-p" id="burger">
<div class="burger opaque"><div></div><div></div><div></div></div>
</div>
<!-- 分类按钮 -->
<div class="fl-icon-panel">
</div>
<div class="fl-icon"></div>
<!-- 直播区域 -->
<a href="living_commtaq.jsp?n=">
<div class="zb-icon">
<span></span>
</div>
</a>
<!-- 专题区域 -->
<div class="zt-icon-p" id="fx"></div>
<!-- 右边文字区域  新闻问答详情页右侧-->
<div class="right-cont" id="news_right_cont">
<a href="newsDetail_forward_1787647">进入原新闻</a>
</div>
<!-- 右边文字区域  话题问答详情页右侧-->
<div class="right-cont" id="ask_right_cont">
<a href="asktopic_detail_">进入原话题</a>
</div>
<!-- 政务相关-->
<div class="politics_head politics_head_download">
<a class="txt" data-moblink="demo/a?contType=25&amp;contId=" id="moblink_top_wz_xiazai" moblink-featured="">下载澎湃APP</a>
<a class="icon icon_search" href="govSearch.jsp"></a>
</div>
<div class="politics_head politics_head_ask">
<a class="txt" data-moblink="demo/a?contType=&amp;contId=1787647" id="moblink_top_tiwen" moblink-featured="">去提问</a>
<a class="icon icon_share"></a>
</div>
<div class="politics_head politics_head_unlogin">
<a class="politics_txt" onclick="registerwdsshow()">注册</a>/<a class="politics_txt" onclick="lgwdsshow()">登录</a>
</div>
<div class="politics_head politics_head_login">
<a class="txt" data-moblink="demo/a?contType=25&amp;contId=" id="moblink_top_xiazai" moblink-featured="">下载澎湃APP</a>
<a class="icon icon_header" href="modifyInfo.jsp"></a>
</div>
<!-- 右边图片区域 -->
<div data-url="http://m.thepaper.cn/download?id=3" id="ask_app_down02">
<a class="right-img" data-moblink="demo/a?contType=7&amp;contId=" href="javascript:allPageAppdowncheck('ask_app_down02','',7);" id="moblink_topichead_" moblink-featured="" style="position:fixed;">
			打开澎湃客户端提问
		</a></div>
</div>
<!-- open -->
<div class="sy-downward">
<div class="upv30-icon"></div>
<div class="sy-downward-cont">
<div class="user-view-info">
<div id="_no_login">
<ul class="sections-list-big"><li><a class="" href="javascript:void(0)" onclick="lgwdsshow()"><i></i><span>登录</span></a></li><li><a class="serch" href="search.jsp"><i></i><span>搜索</span></a></li></ul>
</div>
</div>
<div class="cont-list">
<div class="scrolly">
<div class="sections-panel ">
<ul class="sections-nav ">
<li class=" cur-state">视频<em class="tabline-lf"></em></li>
<li class="">时事<em class="tabline-lf"></em></li>
<li class="">财经<em class="tabline-lf"></em></li>
<li class="">思想<em class="tabline-lf"></em></li>
<li class="">生活<em class="tabline-lf"></em><em class="tabline-rg"></em></li>
</ul>
</div>
<ul class="sections-list" style="display: block;">
<li><a href="list_26912">上直播</a></li>
<li><a href="list_26918">@所有人</a></li>
<li><a href="list_26919">中国政前方</a></li>
<li><a href="list_26965">温度计</a></li>
<li><a href="list_26906">大都会</a></li>
<li><a href="list_26907">湃客科技</a></li>
<li><a href="list_26908">一级视场</a></li>
<li><a href="list_27260">World湃</a></li>
<li><a href="list_26909">追光灯</a></li>
<li><a href="list_26910">运动装</a></li>
<li><a href="list_26911">围观</a></li>
<li><a href="list_26913">七环视频</a></li>
<li><a href="list_26914">健寻记</a></li>
<li><a href="list_26915">场所</a></li>
</ul>
<ul class="sections-list" style="display: none;">
<li><a href="list_25462">中国政库</a></li>
<li><a href="list_25488">中南海</a></li>
<li><a href="list_25489">舆论场</a></li>
<li><a href="list_25490">打虎记</a></li>
<li><a href="list_25423">人事风向</a></li>
<li><a href="list_25426">法治中国</a></li>
<li><a href="list_25424">一号专案</a></li>
<li><a href="list_25463">港台来信</a></li>
<li><a href="list_25491">长三角政商</a></li>
<li><a href="list_25428">直击现场</a></li>
<li><a href="list_27604">暖闻</a></li>
<li><a href="list_25464">知食分子</a></li>
<li><a href="list_25425">绿政公署</a></li>
<li><a href="list_25429">澎湃国际</a></li>
<li><a href="list_25481">外交学人</a></li>
<li><a href="list_25430">澎湃防务</a></li>
<li><a href="list_25678">唐人街</a></li>
<li><a href="list_25427">澎湃人物</a></li>
<li><a href="list_25422">浦江头条</a></li>
<li><a href="list_25487">教育家</a></li>
<li><a href="list_25634">全景现场</a></li>
<li><a href="list_25635">美数课</a></li>
<li><a href="list_25600">快看</a></li>
</ul>
<ul class="sections-list" style="display: none;">
<li><a href="list_25434">10%公司</a></li>
<li><a href="list_25436">能见度</a></li>
<li><a href="list_25433">地产界</a></li>
<li><a href="list_25438">财经上下游</a></li>
<li><a href="list_25435">金改实验室</a></li>
<li><a href="list_25437">牛市点线面</a></li>
<li><a href="list_27234">科技湃</a></li>
<li><a href="list_25485">澎湃商学院</a></li>
<li><a href="list_25432">自贸区连线</a></li>
</ul>
<ul class="sections-list" style="display: none;">
<li><a href="list_25444">社论</a></li>
<li><a href="list_27224">澎湃评论</a></li>
<li><a href="list_26525">思想湃</a></li>
<li><a href="list_26878">上海书评</a></li>
<li><a href="list_25483">思想市场</a></li>
<li><a href="list_25457">私家历史</a></li>
<li><a href="list_25574">翻书党</a></li>
<li><a href="list_25455">艺术评论</a></li>
<li><a href="list_26937">古代艺术</a></li>
<li><a href="list_25450">文化课</a></li>
<li><a href="list_25482">逝者</a></li>
<li><a href="list_25445">澎湃研究所</a></li>
<li><a href="list_25456">市政厅</a></li>
<li><a href="list_25446">请讲</a></li>
<li><a href="list_25536">专栏</a></li>
<li><a href="list_26506">异次元</a></li>
</ul>
<ul class="sections-list" style="display: none;">
<li><a href="list_25448">有戏</a></li>
<li><a href="list_26609">文艺范</a></li>
<li><a href="list_25942">身体</a></li>
<li><a href="list_26015">私·奔</a></li>
<li><a href="list_25599">运动家</a></li>
<li><a href="list_25842">私家地理</a></li>
<li><a href="list_26862">楼市</a></li>
<li><a href="list_25769">生活方式</a></li>
<li><a href="list_25990">澎湃联播</a></li>
<li><a href="list_26173">视界</a></li>
<li><a href="list_26202">亲子学堂</a></li>
<li><a href="list_26404">赢家</a></li>
<li><a href="list_26490">汽车圈</a></li>
</ul>
</div>
</div>
</div>
<!-- end -->
</div>
<!-- share box -->
<div class="v3-shareBox">
<h2>分享</h2>
<div class="share-list">
<!--<img src="../img/detail-share.png" alt="" />-->
<ul>
<li><a class="wb" href="javascript:ToSina('一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？','http://image1.thepaper.cn/image/6/121/15.jpg',1);" id="news_weibo"></a></li>
<li><a class="tx" href="javascript:ToTencent('一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？','http://image1.thepaper.cn/image/6/121/15.jpg',1);" id="news_qq"></a></li>
<li><a class="db" href="javascript:Torenren('一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？','http://image1.thepaper.cn/image/6/121/15.jpg','“2017成都国际书店论坛”即将在方所成都店开幕。本次论坛汇聚了全球十数家重量级书店及其主理人，呈现书店人如何借由书店传达个人的文化态度和美学追求。',1);" id="news_renren"></a></li>
<li class="nol"><a class="kj" href="javascript:ToQzone('一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？','http://image1.thepaper.cn/image/6/121/15.jpg',1,'“2017成都国际书店论坛”即将在方所成都店开幕。本次论坛汇聚了全球十数家重量级书店及其主理人，呈现书店人如何借由书店传达个人的文化态度和美学追求。');" id="news_qzone"></a></li>
</ul>
</div>
<span class="closeS"></span>
</div>
<!-- 分类帅选 -->
<div class="sy-downward sy-downward-sort" id="sy-downward-sort">
<div class="upv30-icon upv30-icon-pos"></div>
<div class="sy-downward-flcont">
<ul class="sort-cont">
<li>
<a href="ask_index.jsp?sort=">
<span class="c1" style="color: #00a4eb;">精选</span>
<span class="c2" style="color: #00a4eb;">Front Page</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26971&amp;sort=">
<span class="c1">目击</span>
<span class="c2">Witness</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26162&amp;sort=">
<span class="c1">焦点</span>
<span class="c2">Focus</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26164&amp;sort=">
<span class="c1">思想</span>
<span class="c2">Thoughts</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26978&amp;sort=">
<span class="c1">健康</span>
<span class="c2">Health</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26980&amp;sort=">
<span class="c1">教育</span>
<span class="c2">Education</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26982&amp;sort=">
<span class="c1">法律</span>
<span class="c2">Legal</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=27129&amp;sort=">
<span class="c1">政务</span>
<span class="c2">Government Affairs</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26983&amp;sort=">
<span class="c1">探索</span>
<span class="c2">Discovery</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26979&amp;sort=">
<span class="c1">文艺</span>
<span class="c2">Arts</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26165&amp;sort=">
<span class="c1">明星</span>
<span class="c2">Celebrity</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26163&amp;sort=">
<span class="c1">商界</span>
<span class="c2">Business</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26984&amp;sort=">
<span class="c1">品位</span>
<span class="c2">Taste</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26203&amp;sort=">
<span class="c1">运动</span>
<span class="c2">Sports</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26167&amp;sort=">
<span class="c1">百科</span>
<span class="c2">General</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26166&amp;sort=">
<span class="c1">投资</span>
<span class="c2">Investment</span>
</a>
</li>
<li>
<a href="ask_index.jsp?category=26981&amp;sort=">
<span class="c1">讨论</span>
<span class="c2">Discussion</span>
</a>
</li>
</ul>
<!-- 操作按钮 -->
<span class="retract-up"></span>
</div>
</div>
<!-- 分类帅选 -->
<!-----------------------以下是原来的部分1------------------------------->
<script type="text/javascript">
$(document).ready(function(){
	$(".list_lanmu").click(function(){
		if($(".lanmu_q").css("display")=="none"){
			$(".list_lanmu").addClass("bt_cur");
			$(".lanmu_q").css('display','block');
		}else{
			$(".list_lanmu").removeClass("bt_cur");
			$(".lanmu_q").css('display','none');
		}
	});

	$(".lanmu_shouqi").click(function(){
		$(".list_lanmu").removeClass("bt_cur");
		$(".lanmu_q").css('display','none');
	});

	var tbd=$("#lanmu_tb").filter(function(index) {return $("#lanmu_tb",this).css("display")!="none";});
	var tbdf=$("#lanmu_tb:eq(0)");
	var tbdl=$(".lanmu_tblast");	//var tbdl=$("#lanmu_tb").last();
	$(".lanmu_p").click(function(){
		if(tbd.prev("#lanmu_tb").length>0){
				tbd.css('display','none');
				tbd.prev("#lanmu_tb").css('display','');
				tbd=tbd.prev("#lanmu_tb");
		}else{
				tbd.css('display','none');
				tbdl.css('display','');
				tbd=tbdl;
		}
	});

	$(".lanmu_n").click(function(){
		if(tbd.next("#lanmu_tb").length>0){
				tbd.css('display','none');
				tbd.next("#lanmu_tb").css('display','');
				tbd=tbd.next("#lanmu_tb");
		}else{
				tbd.css('display','none');
				tbdf.css('display','');
				tbd=tbdf;
		}
	});

	$(".list_lm a").click(function(){
		$(this).addClass("on");
		$(this).siblings().removeClass("on");
		var sliderId=$(this).index();
		$("#slider"+sliderId).css("display","block");
		$("#slider"+sliderId).siblings(".sliderchl").css("display","none");
	});

});
</script>
<!-- 下载条 -->
<div id="pp-download-box">
<div class="icon"></div>
<div class="cont">澎湃新闻客户端</div>
<div class="close-1"></div>
<div class="xz"></div>
</div>
<!-- false -->
<script id="-moblink-js" src="//f.moblink.mob.com/moblink.js?appkey=1cedb268b6d05" type="text/javascript"></script>
<script type="text/javascript">
$(document).ready(function(){
	
if(typeof(MobLink)!='undefined'){
MobLink.init({
	    mobid: "qE",
	    path: "demo/a",
showDefaultUI:false,
initCallback:initMobLink,
	    params:{"contType":"2","contId":"1787647"}
	});
}
});
</script>
<div class="app_fixed" id="moblink-href" style="display:none;z-index:100;">
<div class="app_down4" data-url="http://m.thepaper.cn/download?id=3" id="head_ask_app_down"><a href="javascript:void(0);"><img alt="澎湃" class="logimg" src="http://file.thepaper.cn/wap/v3/img/down_paper100.png"/><b class="first">你有权知道更多</b><br/><b>下载澎湃新闻客户端</b></a><img alt="下载" class="closeimg" onclick="closAllPageDownfixed();event.cancelBubble=true" src="http://file.thepaper.cn/wap/v3/img/down_close42.png"/><span onclick="javascript:void(0);">点击打开</span></div>
</div>
<input id="isdiscont" type="hidden" value="8"/>
<div class="bg-opacity30"></div>
<div id="v3cont_id">
<!-- 详情页-冠名 -->
<p class="detail-gm">
<span class="gg-gmcont"><a href="list_25574">翻书党</a></span></p>
<input id="loginstatus" type="hidden" value="false"/>
<div class="news_content">
<h1 class="t_newsinfo">一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？</h1>
<p class="about_news">杨卓君/整理<span class="FTS-opt" id="FTS-opt"></span></p>
<p class="about_news" style="padding-bottom:15px;">2017-09-08 10:30 

来源：澎湃新闻
</p>
<div class="news_part_father">
<div class="news_part news_part_limit"><div><div style="text-align:center;"><img alt="" height="800" src="http://image.thepaper.cn/www/image/6/120/873.jpg" width="450"/></div><strong>北京│从《劳燕》到《二十二》——战争与女性<br/><div class="contheight"></div>时间：</strong>9月8日（周五）19:00-21:00<br/><div class="contheight"></div><strong>地点：</strong>朝阳区望京中环南路1号社科院研究生院D座2层单向空间<br/><div class="contheight"></div><strong>嘉宾：</strong>郭柯（导演）、张翎（作家）<br/><div class="contheight"></div>电影《敦刻尔克》的导演诺兰关注的是被困于敦刻尔克海岸的40万英法士兵，用独特的影像语言呈现了自己对于战争的理解。就在前一段时间，两位中国的艺术家也用自己擅长的方式，再一次进入那场战争。不同于《敦刻尔克》中清一色的男性，这两位中国艺术家不约而同地聚焦于战争中的女性。本周五晚，《二十二》导演郭柯、《劳燕》作者张翎做客单向空间，带领大家再一次回到历史的现场，再一次思考战争中的女性、人性与命运。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="1066" src="http://image.thepaper.cn/www/image/6/120/876.jpg" width="600"/></div><strong>北京│请至少爱一个像男人的男人——张小娴读者见面会<br/><div class="contheight"></div>时间：</strong>9月9日（周六）14:30-16:00<br/><div class="contheight"></div><strong>地点：</strong>海淀区海淀图书城西大街35号3栋1F言几又书店<br/><div class="contheight"></div><strong>主讲人：</strong>张小娴（作家）<br/><div class="contheight"></div>张小娴的作品被很多女生视为“爱情圣经”，但她在谈及爱情时却认为自己从来就不是爱情导师，而爱情唯一的导师即是爱情本身。经历过、感受过、体验过、思考过，才会最终明白最适合自己的人是什么样的，最需要追求的人生是什么样的，当这一切都明了之际，对爱情的理解也就拨云见日了。9月9日，张小娴在言几又与你见面。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="353" src="http://image.thepaper.cn/www/image/6/120/872.jpg" width="600"/></div><strong>北京│做你自己，世界自然会供养你——舒国治X孙中伦和你一起聊聊关于出走、关于流浪<br/><div class="contheight"></div>时间：</strong>9月9日（周六）15:00-17:00<br/><div class="contheight"></div><strong>地点：</strong>朝阳区郎家园甲10号东朗电影创意产业园b103界面新闻<br/><div class="contheight"></div><strong>嘉宾：</strong>舒国治（作家）、孙中伦（美国波莫纳学院学生、罗德奖学金最终候选人）<br/><div class="contheight"></div>做自己，到底要付出多大的代价？要自由，是不是一件奢侈的事情？少数派，是主动的选择还是被动的边缘化？何时开始，“一场说走就走的旅行”变成了别人眼中的“秀”？何时开始，“流浪”成为少数人标榜的“文艺生活”，出走的动机变得重要？没车、没房、没户口、没有稳定的工作，我的人生是否一败涂地？没有安全的退路、没有充足的存款，我是否没有条件选择“出走”？舒国治与孙中伦，两代流浪者的对话。<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>北京│有理想的人如何运用老庄的智慧<br/><div class="contheight"></div>时间：</strong>9月10日（周日）14:00-16:00<br/><div class="contheight"></div><strong>地点：</strong>海淀区丹棱街16号海兴大厦C座海淀区图书馆四层多功能厅<br/><div class="contheight"></div><strong>主讲人：</strong>杜保瑞（台湾大学哲学系教授）<br/><div class="contheight"></div>杜保瑞，台湾大学哲学博士，曾任华梵大学哲学系主任、文学院院长，现为台湾大学哲学系教授，主要研究中国哲学史、道家学史、禅宗哲学、宋明儒学等，著有《庄周梦蝶》、《基本哲学问题》、《北宋儒学》、《南宋儒学》等。本次讲座围绕以下内容展开：孔孟所追求的以及所面对的理想是什么？庄子所追求的以及所面对的理想是什么？老子所追求的以及所面对的理想是什么？一个儒者如何学习庄子的智慧？<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="800" src="http://image.thepaper.cn/www/image/6/120/874.jpg" width="514"/></div><strong>北京│美术馆的反叛与孤独——从波德莱尔到毕加索<br/><div class="contheight"></div>时间：</strong>9月10日（周日）14:30-17:00<br/><div class="contheight"></div><strong>地点：</strong>朝阳区酒仙桥北路9号北京民生现代美术馆<br/><div class="contheight"></div><strong>嘉宾：</strong>牧野（诗人、评论家）、汪海（中国人民大学比较文学与世界文学副教授）、帅好（独立批评家、历史学者）、艾蕾尔（清华大学美术学院博士、艺术批评家、策展人）<br/><div class="contheight"></div>“今天的革命者就是明天的经典大师”，我们如何定义经典？经典是反叛者的代名词吗？是否只有反判才能传世？诸如波德莱尔的吸毒、梵高的割耳、毕加索的风流韵事、普鲁斯特的神经衰弱、杜尚的神秘游离等等，可能我们能直接定义现代主义的范围，在这个大众传媒如此发达的时代，艺术的界限已经模糊，问题存在在哪里？9月10日，一起来听听学者和艺术家们的看法。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="800" src="http://image.thepaper.cn/www/image/6/124/105.jpg" width="571"/></div><strong>北京│像年轻时一样疯狂？——廖一梅“悲观主义三部曲”新书发布会<br/><div class="contheight"></div>时间：</strong>9月10日（周日）15:00-17:00<br/><div class="contheight"></div><strong>地点：</strong>朝阳区望京中环南路1号社科院尚8文创园D座2层单向空间<br/><div class="contheight"></div><strong>嘉宾：</strong>廖一梅（剧作家、作家）、史航（编剧）<br/><div class="contheight"></div>“悲观主义三部曲”（《恋爱的犀牛》、《琥珀》和《柔软》）基本上是完成于十年前，其中关于爱情和自我的讨论在当时成为热议，可以说是代表了十年前的年轻人对于爱情和自我的态度，疯狂的、不羁的、任性的、难以捉摸的。这么多年过去了，《恋爱的犀牛》还在上演着，演员班底换了一代又一代。那时的年轻人还像年轻时一样疯狂吗？如今的年轻人也如当初的他们一样疯狂吗？久未在公众场合露面的廖一梅老师、鹦鹉史航，邀请年轻人们一起来探讨两代人的观念碰撞，爱与自我这一永恒的话题。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="848" src="http://image.thepaper.cn/www/image/6/120/875.jpg" width="600"/></div><strong>北京│上传之后<br/><div class="contheight"></div>时间：</strong>9月10日（周日）18:30-20:30<br/><div class="contheight"></div><strong>地点：</strong>朝阳区百子湾路32号今日美术馆未来馆大厅<br/><div class="contheight"></div><strong>嘉宾：</strong>韩松（科幻作家）、杨平（科幻作家）、谭昶（科大讯飞大数据研究院副院长）、吴珏辉（新媒体艺术家）、高鹏（今日美术馆馆长）、李兆欣（科幻评论家）<br/><div class="contheight"></div>宇宙就是上帝不小心点开的压缩包，不同格式喷薄而出：.txt、.jpg、.avi、.ppt、.pdf……格式是万物的后缀，包括人类自身。在这里，你可以选择以任意方式入网：手机是移动接口，电流是神经递质，身体是一个U盘，意识是一段代码。未来，当我们把意识上传到网络空间，“人”的定义会发生怎样的改变？个体的“我”是否会消解？在那样一个世界，会诞生怎样的艺术和思考？未来事务管理局与今日美术馆合作，在这场赛博之旅结束前，邀请科幻作家、艺术家和科大讯飞的人工智能专家，一起讨论意识上传后的生活。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="887" src="http://image.thepaper.cn/www/image/6/120/886.jpg" width="600"/></div><strong>上海│宇宙不只属于人类——聊聊科幻电影<br/><div class="contheight"></div>时间：</strong>9月8日（周五）19:30-21:30<br/><div class="contheight"></div><strong>地点：</strong>浦东新区东园路18号中国金融信息中心金领驿站<br/><div class="contheight"></div><strong>主讲人：</strong>王侃瑜（作家）<br/><div class="contheight"></div>刚刚结束的2017上海国际文学周，科幻成为了国内外作家和书迷们一起讨论的主题。不得不说，近年来科幻作品吸引了越来越多的书迷，包括影迷。本期电影沙龙活动，我们就将邀请作家王侃瑜来和大家一起聊聊科幻电影，带你一起回顾科幻经典《银翼杀手》、《星际穿越》和《风之谷》。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="899" src="http://image.thepaper.cn/www/image/6/120/882.jpg" width="600"/></div><strong>上海│东方佛教的第一圣地<br/><div class="contheight"></div>时间：</strong>9月9日（周六）10:00-12:00<br/><div class="contheight"></div><strong>地点：</strong>浦东新区陆家嘴富城路99号震旦博物馆一楼多功能厅<br/><div class="contheight"></div><strong>主讲人：</strong>张焯（云冈石窟研究院院长）<br/><div class="contheight"></div>佛教自东汉时期传入中国，得益于五胡十六国民族大迁徙的历史机缘，四世纪以后在中华大地上开花结果。而五世纪北魏首都平城（今山西大同）佛教的兴盛于云冈石窟的开凿，即是佛教东传至华夏大地奏响的一曲惊世乐章。本次讲座将对云冈石窟的开凿因缘、发展历程、艺术特色等进行解析。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="911" src="http://image.thepaper.cn/www/image/6/120/898.jpg" width="600"/></div><strong>上海│从虚幻中一瞥魔幻的现实——纳博科夫《看，那些小丑！》《庶出的标志》读书分享会暨签售会<br/><div class="contheight"></div>时间：</strong>9月9日（周六）14:00-16:00<br/><div class="contheight"></div><strong>地点：</strong>徐汇区淮海中路1555号上海图书馆3楼音乐欣赏厅<br/><div class="contheight"></div><strong>嘉宾：</strong>金衡山（华东师范大学教授）、吴其尧（上海外国语大学教授）<br/><div class="contheight"></div>9月9日下午，“译文书友会”将为大家奉上高质量的阅读活动——纳博科夫作品《庶出的标志》和《看，那些小丑！》读书分享会暨签售会将于上海图书馆举行。此次活动有幸邀请到《庶出的标志》和《看，那些小丑！》的两位译者——华东师范大学的金衡山教授和上海外国语大学的吴其尧教授，来为读者解读纳博科夫其人其作。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="848" src="http://image.thepaper.cn/www/image/6/120/884.jpg" width="600"/></div><strong>上海│日本的女性摄影师们<br/><div class="contheight"></div>时间：</strong>9月9日（周六）14:00-16:00<br/><div class="contheight"></div><strong>地点：</strong>黄浦区南京西路231号人民公园7号门上海当代艺术馆<br/><div class="contheight"></div><strong>主讲人：</strong>竹内万里子（京都造形艺术大学教授）<br/><div class="contheight"></div>京都造形艺术大学的知名摄影评论家竹内万里子教授致力于研究日本19-21世纪女性摄影师及作品。无论日本与否，近年来涌现出大量的女性摄影师，但是从摄影史的角度来看，登场的却以男性居多。本周六，MoCA君邀请您来到上海当代艺术馆，一起听竹内万里子教授谈一谈日本19-21世纪女性摄影师及作品。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="1061" src="http://image.thepaper.cn/www/image/6/120/883.jpg" width="600"/></div><strong>上海│跨界的历史更精彩<br/><div class="contheight"></div>时间：</strong>9月9日（周六）19:00-20:30<br/><div class="contheight"></div><strong>地点：</strong>徐汇区淮海中路1834号—1大隐书局<br/><div class="contheight"></div><strong>嘉宾：</strong>张明扬（专栏作家）、徐瑾（经济学者）、饶佳荣（澎湃新闻编辑）<br/><div class="contheight"></div>《天命与剑》是国内第一本专注于帝制时代合法性的通俗写史作品，带着问题意识深入中国帝制时代的风暴口。9月9日，本书作者张明扬与经济学者徐瑾、澎湃新闻私家历史编辑饶佳荣将作客大隐书局（武康大楼店），他们将就《天命与剑》展开一些深入的讨论，并现场畅谈跨界的历史。历史不仅仅是历史，还是政治史、经济史、文明史，与多种学科结合起来之后，阅读历史将更加精彩。热爱历史的你，又怎么可以错过这场“历史的小九九”探讨会？<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="879" src="http://image.thepaper.cn/www/image/6/120/871.jpg" width="529"/></div><strong>上海│“我知道什么？”——《蒙田全集》新书分享会<br/><div class="contheight"></div>时间：</strong> 9月9日（周六）19:00<br/><div class="contheight"></div><strong>地点：</strong>黄浦区复兴中路505号思南文学之家<br/><div class="contheight"></div><strong>嘉宾：</strong>马振骋（法语文学翻译家）、袁筱一（华东师范大学法语系教授）<br/><div class="contheight"></div>蒙田（1533-1592）是法国文艺复兴后重要的人文主义作家，启蒙运动前的一位知识权威和批评家，也是一位人类感情的冷峻的观察家，一位对各民族文化，特别是西方文化进行冷静研究的学者。他从人文主义出发，更多指出人与生俱来的弱点与缺陷，要人看清自己是什么，然后才能正确对待自己、他人与自然，才能活得自在与惬意。蒙田要追问“我知道什么”，并教我们如何学会“光明正大地享受自己的存在”。本期思南读书会，邀请到《蒙田全集》翻译者马振骋先生、著名翻译家袁筱一女士，来和读者一起走近蒙田的思想文学世界。<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>上海│从苏东坡到叶芝——中西诗画姻缘举隅<br/><div class="contheight"></div>时间：</strong>9月9日（周六）19:00<br/><div class="contheight"></div><strong>地点：</strong>徐汇区淮海中路1555号上海图书馆西区二楼报告厅<br/><div class="contheight"></div><strong>主讲人：</strong>叶扬（美国加州大学河滨分校比较文学系教授、复旦大学顾问教授）<br/><div class="contheight"></div>诗书画同列传统中国文化的“三绝”，苏东坡曾云“诗画本一律”。作为语言艺术的诗，和作为视觉艺术的画，究竟有何异同？二者之间，又存在着怎样的“姻缘”？此讲座由中西文艺传统中历来对于此类问题的阐述入手，再将韩幹笔下的马、王诜的山水与东坡的诗，王冕的《墨梅图》及自题诗、达·芬奇、米开朗琪罗、高雷琪奥等大师以希腊神话“莉达与天鹅”为主题的绘画与叶芝的诗两相比较，分别作观赏及细读，以探讨中西传统中诗画之间有趣的互动。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="900" src="http://image.thepaper.cn/www/image/6/120/885.jpg" width="600"/></div><strong>上海│画以载道——从董其昌谈传统书画鉴赏<br/><div class="contheight"></div>时间：</strong>9月10日（周日）10:30-12:00<br/><div class="contheight"></div><strong>地点：</strong>黄浦区福州路401号上海古籍书店6楼多功能厅<br/><div class="contheight"></div><strong>主讲人：</strong>颜晓军（上海博物馆馆员）<br/><div class="contheight"></div>董其昌生活的晚明时代，正当心学大盛而儒释道三教融合，形成了新兴的儒学。董氏早年在儒学上的造诣对他鉴赏古画、写生山水都有很深的影响，进而与其风格的形成有着直接关系。他的绘画艺术在画坛上能够独领一派，与其新颖独特的风格有关。本讲座就从多个方面详细分析了董其昌所处的儒学环境对其艺术思想产生的重要影响。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="900" src="http://image.thepaper.cn/www/image/6/120/880.jpg" width="600"/></div><strong>广州│《樱桃青衣》新书分享会<br/><div class="contheight"></div>时间：</strong>9月9日（周六）14:00-18:00<br/><div class="contheight"></div><strong>地点：</strong>天河区天河路123号广州购书中心二楼中庭<br/><div class="contheight"></div><strong>主讲人：</strong>张怡微（作家）<br/><div class="contheight"></div>荣获第36届时报文学奖短篇小说首奖、入围第14届华语文学传媒大奖最具潜力新人奖的青年作家张怡微，将携其新作《樱桃青衣》于9月9日下午，来到广州购书中心“读领风骚”现场，与各位读者分享她的创作。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="849" src="http://image.thepaper.cn/www/image/6/120/881.jpg" width="600"/></div><strong>广州│悠悠咸水歌 浓浓珠江情——水上居民与“广州咸水歌”的前世今生<br/><div class="contheight"></div>时间：</strong>9月9日（周六）15:00-17:00<br/><div class="contheight"></div><strong>地点：</strong>海珠区小洲村小洲东路138号小洲艺术区二区小洲艺坊<br/><div class="contheight"></div><strong>主讲人：</strong>谢棣英（广东咸水歌省级代表性传承人）<br/><div class="contheight"></div>在讲座中，将通过呈现泛黄的疍家历史照片、聆听独具岭南水乡特色的咸水歌、展示原生态的疍家服饰等途径，广东咸水歌省级代表性传承人谢棣英带您一起领略水上居民（旧时称之为“疍民”）的酸甜苦辣和广州咸水歌的前世今生！<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>广州│临终关怀和葬礼的社会意义<br/><div class="contheight"></div>时间：</strong>9月12日（周二）19:00-21:00<br/><div class="contheight"></div><strong>地点：</strong>天河区花城大道85号高德置地广场春广场B座12楼<br/><div class="contheight"></div><strong>主讲人：</strong>程瑜（中山大学社会学与人类学学院教授、中山医学院教授）<br/><div class="contheight"></div>科技给我们提供了许多便利，同时又极其缺乏人文关怀。每年的医患问题及其他社会冲突层出不穷，这个深层的社会问题并不能依赖科技来解决。怎么解决呢？让我们一起回归本质需求，聆听程教授讲述临终关怀和葬礼的社会意义。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="831" src="http://image.thepaper.cn/www/image/6/120/879.jpg" width="600"/></div><strong>成都│书店与城市风格<br/><div class="contheight"></div>时间：</strong>9月8日（周五）19:00-22:00、9月9日（周六）14:30-21:30、9月10日（周日）14:30-19:00<br/><div class="contheight"></div><strong>地点：</strong>锦江区中纱帽街8号成都远洋太古里M68-70号方所<br/><div class="contheight"></div><strong>嘉宾：</strong>钱小华（先锋书店创始人）、吴雅慧（台湾旧香居书店店主）、内沼晋太郎（日本本屋B&amp;B店主）、何光伦（四川省图书馆馆长）、Fabio Herz（巴西文化书店董事）、Katherine Orphan（美国“最后一家”书店经理）等<br/><div class="contheight"></div>由方所主办的“2017成都国际书店论坛”即将于9月8日-10日在方所成都店开幕。本次论坛汇聚了全球十数家重量级书店及其主理人，呈现书店人如何借由书店传达个人的文化态度和美学追求，探讨书店与城市风格之间的关联，书店如何成为地域风格的象征，以及书店对于城市是否具备指标意义。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="882" src="http://image.thepaper.cn/www/image/6/120/878.jpg" width="600"/></div><strong>成都│纳凉特辑·精怪故事<br/><div class="contheight"></div>时间：</strong>9月8日（周五）19:30-21:00<br/><div class="contheight"></div><strong>地点：</strong>金牛区交大路183号凯德广场·金牛二期四楼西西弗书店<br/><div class="contheight"></div><strong>嘉宾：</strong>迟元美（出版人）、叶扬斌（出版人）<br/><div class="contheight"></div>女娲补天，夸父逐日、精卫填海，这些耳熟能详的神话寓言故事，都是来自于中国这部古老的地理书——《山海经》。但古老的就是枯燥的么？9月8日，“知中ZHICHINA”内容监制迟元美、叶扬斌一起解读《山海经》里的精怪故事，娓娓道来中日妖怪文化。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="1065" src="http://image.thepaper.cn/www/image/6/120/877.jpg" width="600"/></div><strong>成都│《我们与我们的城市》：城市之美，在于每一个人的故事——三明治MOOK分享会·成都站<br/><div class="contheight"></div>时间：</strong>9月9日（周六）15:00-17:00<br/><div class="contheight"></div><strong>地点：</strong>锦江区红星路三段1号IFS国际金融中心LG223言几又书店<br/><div class="contheight"></div><strong>嘉宾：</strong>李梓新（杂志主编）、王牧之（杂志主编）<br/><div class="contheight"></div>9月9日，“中国第一本以城市作为经脉维度讲述故事的杂志书”《三明治：我们与我们的城市》对话“成都第一本大体量城市指南”《一筑一事 城市指南·成都》，为我们分享城市之美。<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>成都│青铜视野下的商周文明：中心化、制度化和文化交流活动<br/><div class="contheight"></div>时间：</strong>9月10日（周日）14:00-16:30<br/><div class="contheight"></div><strong>地点：</strong>青羊区人民西路4号四川省图书馆<br/><div class="contheight"></div><strong>主讲人：</strong>杰西卡·罗森（牛津大学副校长）<br/><div class="contheight"></div>本次讲座通过对商周时期的青铜器、周代贵族间流行的草原风格器物、秦及欧亚草原和地中海帝国既有区别又有联系的遗迹遗物等代表器物的研究，深入地探讨欧亚大陆不同时代的主流文化之间的联系，织就密密麻麻的各种关系网络，并试图寻求每一个网络形成的推动力，以及不同的推动力所导致的不同方向的扩散传播。<br/><div class="contheight"></div><div style="text-align:center;"><img alt="" height="960" src="http://image.thepaper.cn/www/image/6/120/887.jpg" width="600"/></div><strong>郑州│百战经典：《孙子兵法》中的谋略与智慧<br/><div class="contheight"></div>时间：</strong>9月9日（周六）15:00-17:30<br/><div class="contheight"></div><strong>地点：</strong>金水区农业路8号河南博物院西配楼二楼<br/><div class="contheight"></div><strong>主讲人：</strong>王宏林（河南大学文学院教授、博士生导师）<br/><div class="contheight"></div>作为中国古典军事文化遗产中的璀璨瑰宝、中国优秀传统文化的重要组成部分，《孙子兵法》为世人熟知，但是它的作者孙武却鲜为人知，有人甚至把孙武和孙膑混为一谈，孙武作为《孙子兵法》的作者，未见以前有他的战争经历的记载，为什么一出手就写出兵法十三篇，成为千古兵家的圣典？9月9日下午，河南大学文学院教授、博士生导师王宏林和您一起品读《孙子兵法》，看奇人奇书的独特魅力。<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>郑州│《娥眉月》新书分享会<br/><div class="contheight"></div>时间：</strong>9月10日（周日）15:00-17:00<br/><div class="contheight"></div><strong>地点：</strong>中原区建设路秦岭路大摩西元广场三楼纸的时代书店<br/><div class="contheight"></div><strong>嘉宾：</strong>南希（纽约华文女作家协会理事）、青青（河南省诗歌学会副会长）<br/><div class="contheight"></div>娥眉月是弯月，弯月是缺月，人们只觉得它美，不觉得它缺。娥眉月蕴含着完满，从它的弧线沿伸，终究全回到原来的地方，完成了一个圆。南希的长篇小说《娥眉月》，讲述了一个圆中有缺，缺中有圆的动人故事。9月10日，两位作家与读者一起分享小说主人公从国内到国外的爱情、希望、奋斗、寻梦的曲折经历和心路历程。<br/><div class="contheight"></div><br/><div class="contheight"></div><strong>长沙│听“长沙活字典”顾庆丰讲述长沙的往事与变迁<br/><div class="contheight"></div>时间：</strong>9月10日（周日）15:00-16:30<br/><div class="contheight"></div><strong>地点：</strong>天心区湘江中路36号海信广场6层弘道书店<br/><div class="contheight"></div><strong>主讲人：</strong>顾庆丰（文化学者、中国民间文艺家协会会员）<br/><div class="contheight"></div>9月10日，文化学者、中国民间文艺家协会会员顾庆丰携著作《长沙的故事》来到弘道书店，从崭新的角度为读者解读长沙的历史和文化。</div></div>
<div class="news_part_all">点击查看全文 <span></span></div>
</div>
<div class="bottom_word_relation">
</div>
<div class="news_bl"><span style="float:left">责任编辑：顾明</span> 澎湃新闻，未经授权不得转载。新闻报料：4009-20-4009</div>
<!-- 分享or点赞 -->
<div class="fxOrdz">
<a class="fx" href="javascript:void(0);" onclick="showShareBox()"><em></em>分享</a>
<a class="dz" href="javascript:voteContxq('1787647','27');" id="news_praise">
<em></em>
	                			26</a>
</div>
<div class="news_open_app"> <a data-moblink="demo/a?contType=2&amp;contId=1787647&amp;optType=1" href="javascript:void(0);" id="moblink_morecomm" moblink-featured=""> 打开澎湃新闻APP，发表评论 </a></div>
<script src="http://ad.thepaper.cn/s?z=paper&amp;c=910" type="text/javascript"></script>
</div>
<div data-widget="plista_widget_webApp" style="display: block"></div>
<!-- 相关推荐 -->
<div class="news_panel" id="news_panel"></div>
<!-- 热门推荐 -->
<div class="news_panel">
<div class="news_panel_title">
<div class="title">热门推荐</div>
<div class="line"></div>
</div>
<ul class="news_ul">
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790874" href="javascript:void(0);" id="moblink_1790874" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="火车上偶遇未婚夫和他人暧昧，女子跳下站台撞火车被乘警拉回" class="item_left_img" src="http://image2.thepaper.cn/image/6/131/942.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">火车上偶遇未婚夫和他人暧昧，女子跳下站台撞火车被乘警拉回</div>
<div class="item_right_footer clearfix">
<div>一号专案</div>
<div>2小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790189" href="javascript:void(0);" id="moblink_1790189" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="林毅夫吉林报告为啥引发东北热议：体制机制改革才是破局关键" class="item_left_img" src="http://image1.thepaper.cn/image/6/129/538.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">林毅夫吉林报告为啥引发东北热议：体制机制改革才是破局关键</div>
<div class="item_right_footer clearfix">
<div>财经上下游</div>
<div>1天前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790195" href="javascript:void(0);" id="moblink_1790195" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="我国首条地铁、北京地铁1号线已全线安装安全门并投入使用" class="item_left_img" src="http://image1.thepaper.cn/image/6/129/571.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">我国首条地铁、北京地铁1号线已全线安装安全门并投入使用</div>
<div class="item_right_footer clearfix">
<div>中国政库</div>
<div>23小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790399" href="javascript:void(0);" id="moblink_1790399" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="“魔盗团”香港盗走价值1500万项链惊动公安部，三人获刑" class="item_left_img" src="http://image2.thepaper.cn/image/6/130/256.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">“魔盗团”香港盗走价值1500万项链惊动公安部，三人获刑</div>
<div class="item_right_footer clearfix">
<div>一号专案</div>
<div>7小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790191" href="javascript:void(0);" id="moblink_1790191" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="深圳首批历史建筑公示：国贸大厦、地王大厦、上海宾馆入列" class="item_left_img" src="http://image.thepaper.cn/image/6/129/633.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">深圳首批历史建筑公示：国贸大厦、地王大厦、上海宾馆入列</div>
<div class="item_right_footer clearfix">
<div>中国政库</div>
<div>23小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790694" href="javascript:void(0);" id="moblink_1790694" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="湖州通报偷埋病死猪案件最新进展：约300吨先后6次被掩埋" class="item_left_img" src="http://image1.thepaper.cn/image/6/131/245.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">湖州通报偷埋病死猪案件最新进展：约300吨先后6次被掩埋</div>
<div class="item_right_footer clearfix">
<div>长三角政商</div>
<div>6小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790126" href="javascript:void(0);" id="moblink_1790126" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="美已育5子妇女怀孕查出癌症：为生子弃疗，生孩子2天后去世" class="item_left_img" src="http://image.thepaper.cn/image/6/129/528.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">美已育5子妇女怀孕查出癌症：为生子弃疗，生孩子2天后去世</div>
<div class="item_right_footer clearfix">
<div>澎湃国际</div>
<div>1天前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790366" href="javascript:void(0);" id="moblink_1790366" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="重案组揭秘沈阳CS基地杀人案：私拿手机被杀、训练中被勒死" class="item_left_img" src="http://image.thepaper.cn/image/6/130/44.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">重案组揭秘沈阳CS基地杀人案：私拿手机被杀、训练中被勒死</div>
<div class="item_right_footer clearfix">
<div>一号专案</div>
<div>20小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=2&amp;contId=1790273" href="javascript:void(0);" id="moblink_1790273" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="甘肃兰州警察下班途中遇男子持刀行凶，与群众合力刀下救人" class="item_left_img" src="http://image1.thepaper.cn/image/6/129/751.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">甘肃兰州警察下班途中遇男子持刀行凶，与群众合力刀下救人</div>
<div class="item_right_footer clearfix">
<div>直击现场</div>
<div>22小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
<li class="news_item">
<a class="clearfix" data-moblink="demo/a?contType=10&amp;contId=1790260" href="javascript:void(0);" id="moblink_1790260" moblink-featured="" style="display:block;">
<div class="item_left">
<img alt="男童打盹前后摇摆，身旁女童伸手去护" class="item_left_img" src="http://image1.thepaper.cn/image/6/129/700.jpg"/>
</div>
<div class="item_right">
<div class="item_title 1">男童打盹前后摇摆，身旁女童伸手去护</div>
<div class="item_right_footer clearfix">
<div>@所有人</div>
<div>22小时前</div>
<div class="news_open_app">打开APP查看 </div>
</div>
</div>
</a>
</li>
</ul>
</div>
<!-- 分享开始 -->
<script src="http://res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>
<script>
var shareInfo = {
    title:"一周文化讲座｜书店与城市风格：书店对于城市有指标意义吗？_翻书党_澎湃新闻-The Paper" , 
    desc:"“2017成都国际书店论坛”即将在方所成都店开幕。本次论坛汇聚了全球十数家重量级书店及其主理人，呈现书店人如何借由书店传达个人的文化态度和美学追求。",
    link:location.href,
	img:"http://image.thepaper.cn/image/6/121/28.jpg"
    };
var wxConfigParams={};
wxShare(shareInfo);
</script>
<div class="back-to" id="toolBackTop"><a class="back-top" href="#top" id="backtotop" title="返回顶部"><!--返回顶部--></a></div>
</div>
<div class="v3-footer">
<ul>
<li class="sel"><a href="about_paper.jsp">关于澎湃</a></li>
<li class="sel"><a href="contact_us.jsp">联系我们</a></li>
<li><a href="friendly_links.jsp">友情链接</a></li>
<li class="sel"><a href="copyright_statement.jsp">版权声明</a></li>
<li class="sel"><a href="work_us.jsp">在澎湃工作</a></li>
<li><a href="paper_ad.jsp">澎湃广告</a></li>
</ul>
<div class="v3-footer-ic">
<p>Copyright © 2014~2017 The Paper All rights reserved.</p>
<p>上海东方报业有限公司</p>
<p>沪ICP证：沪B2-20170116 | 沪ICP备14003370号</p>
<p>互联网新闻信息服务许可证：3112014002</p>
<div style="width:300px;margin:0 auto; padding:0;">
<a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010602000299" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;" target="_blank">
<img src="http://file.thepaper.cn/wap/v3/img/ghs.png" style="float:left;margin: 0px 0px 0px 50px;"/>
<p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#FFFFFF;text-align:center;">沪公网安备 31010602000299号
		    </p>
</a>
</div>
</div>
</div>
<script src="http://file.thepaper.cn/wap/v3/js/login.js?v=4.9.2" type="text/javascript"></script>
<div id="bg_overlay" style="display:none;"></div>
<!-- cnzz statistic code -->
<div id="cnzz_wap" style="display: none">
<script type="text/javascript">
		var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");
		document.write(unescape("%3Cspan id='cnzz_stat_icon_1261102516'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s4.cnzz.com/z_stat.php%3Fid%3D1261102516' type='text/javascript'%3E%3C/script%3E"));
	</script>
</div><script type="text/javascript">

function detailHotPrise(obj){
	var id = $(obj).attr("id");
	var times = parseInt($(obj).text())+1;
	$(obj).html(times+'<span class="icon_praised"></span>');
	$(obj).removeAttr("onclick");

	$.ajax( {
  		type : "post",
  		url : priseUrl,
  		data : "commentId=" + id,
  		timeout : 30000,
  		dataType : "json",
  		success : function(data) {},
  		error : function(XMLHttpRequest, textStatus, errorThrown) {}
	});
}

function is_weixin(){
    var ua = navigator.userAgent.toLowerCase();
    if(ua.match(/MicroMessenger/i)=="micromessenger") {
        return true;
    } else {
        return false;
    }
}
var ad = true;

if(ad && !is_weixin()){
	document.write('<div style="position:fixed;bottom:80px;right:10px" id="ad_demo"><script src="http://ad.thepaper.cn/s?z=paper&c=2940"><\/script></div>');
}
openComment();
function onloadRecomm(){
   $.ajax({
        type:"get",
        url: "recommend.jsp",
        data:"contid=1787647", //
        timeout:30000,
        dataType:"html",
        cache: false,
        success: function(html){
            $("#news_panel").html(html);
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            //
        }
   }); 
}


function onloadCommt(){
    $.ajax({
          type:"get",
          url:"newDetail_commt.jsp",
          cache: false,
          data:"contid=1787647",
          timeout:30000,
          dataType:"html",
          success: function(html){           
                $("#commt_list").html(html);
          },
          error:function(XMLHttpRequest, textStatus, errorThrown){
                //
          }
    });
}


    var bt = $('#toolBackTop');
    $(window).scroll(function() {
        bt.show();
        var st = $(window).scrollTop() || document.documentElement.scrollTop || document.body.scrollTop;
        if(st > 100){
            bt.show();
        }else{
            bt.hide();
        }
    });
$.ajax({          
           url: "/wap/pageVisit.msp",
           data:"contId=1787647&type=1",
           cache: false,
           success: function(html){
           },
           failure: function(html){}
        });
$(document).ready(function(){
	onloadRecomm();
	try
	{ 
var contentHeight = $('.news_part_limit >div').height(); 
if(contentHeight > 700){
	        $('.news_part_all').show();
	    }
    }catch(e){};
    $("#tiptitleOK").click(function(){
    $("#overlay").css('display','none').hide();
    $("#tiptitle").css('display','none').hide();
    $("#tiptitleNO").css('display','none').hide();
    $("#tiptitleStr").text("");
    });

    $('#cur_ans').click(function(){
        $("#cur_ans").addClass("cur");
        $("#comm_span").removeClass("cur");
        $("#commt_list").css("display","none");
        $("#aq_commt").css("display","");
    });

    $("#comm_span").click(function(){
        $("#cur_ans").removeClass("cur");
        $("#comm_span").addClass("cur");
        $("#aq_commt").css("display","none");
        $("#commt_list").css("display","");
    });
    
    $(".news_part_all").on("click",function(){
        $(".news_part_limit").css("max-height","initial");
        $(this).hide();
    });
    
});

function showShareBox(){
            $('.bg-opacity30').show();
            $(".header-v4").slideDown("150");
            $('.v3-shareBox').slideDown("150");

}
</script>
<div class="overlay" id="overlay" style="display:none; height: 100%; "></div>
<div class="tiptitle" id="tiptitle" style="display: none;">
<div class="tiptitlebd">
<div class="tiptitleStr" id="tiptitleStr"></div>
<span class="tipbtspan">
<div class="tiptitleOK" id="tiptitleOK" onclick="closeNotice()">确 定</div>
<div class="tiptitleNO" id="tiptitleNO" onclick="closeNotice()" style="display: none;">取消</div>
</span>
</div>
</div>
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"applicationID":"50694380","applicationTime":186,"beacon":"bam.nr-data.net","queueTime":0,"licenseKey":"bc78c5daa2","transactionName":"ZwZVN0ADXEdZBUNcVl5MfTBiTUQHFwxERRZeBkAQdgdGVVEKaAUJBQVRDEAVU0ZcSF1GSQ==","agent":"","errorBeacon":"bam.nr-data.net"}</script></body>
</html>

'''



datasoup=BeautifulSoup(text1111112,'lxml')
print datasoup.select('#v3cont_id > div.news_content ')