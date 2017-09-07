#_*_coding:utf-8_*_
import requests
import re


from bs4 import BeautifulSoup

one_div='''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html class='csdn-bbs'>
  <head>
    <script type="text/javascript" src="http://bbs.csdn.net/tingyun-rum.js"></script>
    <script id="allmobilize" charset="utf-8" src="http://a.yunshipei.com/1327c36bdd7197e30fd9f4b48d1a5bcc/allmobilize.min.js"></script>
<meta http-equiv="Cache-Control" content="no-transform" />
<link rel="alternate" media="handheld" href="#" />

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>ImageIO.write 写入gif 图片 报错 图片黑屏不会动-CSDN论坛</title>

    <link href="/assets/main-04b3fba31882b890bdb2025041262d05.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="//c.csdnimg.cn/public/themes/default/css/btn.css" media="screen" rel="stylesheet" type="text/css" />
    <script src="/assets/application-73a79ab67b5eca88701b728d54cb956b.js" type="text/javascript"></script>
    <script src="http://c.csdnimg.cn//atsuggest/atsuggest.js" type="text/javascript"></script>
    <meta content="authenticity_token" name="csrf-param" />
<meta content="JrmxnrS9i/bGIAZufh8IcXAdrkDlP+GTe+D9d6bhyZ8=" name="csrf-token" />
    <link href="http://c.csdnimg.cn/public/favicon.ico" rel="SHORTCUT ICON">
<link rel="stylesheet" href="http://c.csdnimg.cn/public/common/toolbar/css/index.css">
<script language="javascript" type="text/javascript" src="http://ads.csdn.net/js/tracking.js"></script>
<script type="text/javascript">
    document.domain = "csdn.net";
    var proxy_url = "http://internalapi.csdn.net/proxy.html";
		var ajaxProxyCaches = {};
		function ajaxProxy(proxyUrl, opts) {
		    var c = ajaxProxyCaches[proxyUrl];
		    if (c === undefined) {
		        c = ajaxProxyCaches[proxyUrl] = [];
		        var func = arguments.callee;
		        $('<iframe class="poxy_uc" src="' + proxyUrl + '" style="display:none">').load(function () {
		            c.contentWindow = this.contentWindow;
		            func(proxyUrl, opts);
		        }).prependTo('body');
		    } else if (c.contentWindow === undefined) {
		        c.push(opts);
		    } else {
		        do {
		            c.contentWindow.jQuery.ajax(opts);
		        } while (opts = c.shift());
		    }
		}
</script>
      <link href="/assets/sh-7ba87e2a26838d9e4e41a78d9a2405e6.css" media="all" rel="stylesheet" type="text/css" />
  <script src="/assets/sh-83dfe6b3d61bfd8fe4da30e0d7046ae0.js" type="text/javascript"></script>
  <script src="http://passport.csdn.net/content/loginbox/login.js" type="text/javascript"></script>
    <style>
        #topic-detail-ad-ul{width:960px;float:left;font-size:1px;margin:0;padding:0}
        #topic-detail-ad-l{float:left;}
        #topic-detail-ad-r{float:right;}
        #topic-detail-ad-ul li{list-style: none;}
    </style>
  <script>
	var _hmt = _hmt || [];
	(function() {
	 var hm = document.createElement("script");
	 hm.src = "//hm.baidu.com/hm.js?6bcd52f51e9b3dce32bec4a3997715ac";
	 var s = document.getElementsByTagName("script")[0];
	 s.parentNode.insertBefore(hm, s);
	})();
	</script>

    <!--  js for ask-->
      <script type="text/javascript" >
          window.bbsInfoflag = true;
      </script>

    <link href="http://c.csdnimg.cn/comm_ask/css/ask_float_block.css" rel="stylesheet" type="text/css" />

    <script type="text/javascript" src="http://c.csdnimg.cn/comm_ask/js/libs/wmd.js"></script>

    <script type="text/javascript" src="http://c.csdnimg.cn/comm_ask/js/libs/showdown.js"></script>

    <script type="text/javascript" src="http://c.csdnimg.cn/comm_ask/js/libs/prettify.js"></script>

    <script type="text/javascript" src="http://c.csdnimg.cn/comm_ask/js/apps/ask_float_block.js"></script>

      <script type="text/javascript">
          // 快速回复
          $(document).ready(function () {
          $("#com-quick-reply-bbs").bind("click", function(){
              //_gaq.push(['_trackEvent','function', 'onclick', 'BBS_articles_youhuifu']);
              $("#post_body").focus();
              window.scrollTo(0, $(document).height());
          });
        });
      </script>
    <!--  js for ask  end-->
        <link ref="canonical" href="http://bbs.csdn.net/topics/392258624">

  </head>
  <body id='topics-show'>
    <!-- <script type="text/javascript" src="http://c.csdnimg.cn/pubnav/js/pub_topnav_2011.js"></script> -->

<!--全屏-->
<ins data-revive-zoneid="149" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
<!--全屏-->

<script id="toolbar-tpl-scriptId" skin="black" prod="bbs" fixed="true" src="http://c.csdnimg.cn/public/common/toolbar/js/html.js" type="text/javascript"></script>
      <!-- 统计代码 -->
<script type="text/javascript">
  var protocol = window.location.protocol;
  document.write('<script type="text/javascript" src="' +protocol+ '//csdnimg.cn/pubfooter/js/repoAddr2.js?v=' + Math.random() + '"></'+'script>');
</script>


    <div class="news-nav">
  <div class="container">
    <div class="nav-bar">
      <a href="/home" class="">首页</a>
      <span class="dropdown">
  <a href="#">精选版块</a>
  <span class="caret"></span>
  <div class="dropdown-menu">
    <dl>
      <dt><a href="/forums/Mobile">移动开发</a></dt>
      <dd>
        <a href="/forums/ios">iOS</a>
        <a href="/forums/Android">Android</a>
        <a href="/forums/Qt">Qt</a>
        <a href="/forums/WindowsMobile">WP</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/CloudComputing">云计算</a></dt>
      <dd>
        <a href="/forums/AWS">IaaS</a>
        <a href="/forums/CloudFoundry">Pass/SaaS</a>
        <a href="/forums/hadoop">分布式计算/Hadoop</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/Java">Java技术</a></dt>
      <dd>
        <a href="/forums/J2SE">Java SE</a>
        <a href="/forums/Java_WebDevelop">Java Web 开发</a>
        <a href="/forums/J2EE">Java EE</a>
        <a href="/forums/JavaOther">Java其他相关</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/DotNET">.NET技术</a></dt>
      <dd>
        <a href="/forums/DotNETFramework">.NET Framework</a>
        <a href="/forums/CSharp">C#</a>
        <a href="/forums/DotNETAnalysisAndDesign">.NET分析与设计</a>
        <a href="/forums/ASPDotNET">ASP .NET</a>
        <a href="/forums/VBDotNET">VB .NET</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/WebDevelop">Web开发</a></dt>
      <dd>
        <a href="/forums/PHP">PHP</a>
        <a href="/forums/JavaScript">JavaScript</a>
        <a href="/forums/ASP">ASP</a>
        <a href="/forums/HTMLCSS">HTML(CSS)</a>
        <a href="/forums/HTML5">HTML5</a>
        <a href="/forums/Apache">Apache</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="#">开发语言/框架</a></dt>
      <dd>
        <a href="/forums/Delphi">Delphi</a>
        <a href="/forums/VC">VC/MFC</a>
        <a href="/forums/VB">VB</a>
        <a href="/forums/Cpp">C/C++</a>
        <a href="/forums/BCB">C++ Builder</a>
        <a href="/forums/OtherLanguage">其他开发语言</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="#">数据库开发</a></dt>
      <dd>
        <a href="/forums/MSSQL">MS-SQL Server</a>
        <a href="/forums/Oracle">Oracle</a>
        <a href="/forums/PowerBuilder">PowerBuilder</a>
        <a href="/forums/Informatica">Informatica</a>
        <a href="/forums/OtherDatabase">其他数据库开发</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/Embedded">硬件/嵌入式开发</a></dt>
      <dd>
        <a href="/forums/WinCE">嵌入开发(WinCE)</a>
        <a href="/forums/Embedded_driver">驱动开发/核心开发</a>
        <a href="/forums/Embedded_hardware">硬件设计</a>
        <a href="/forums/Embedded_SCM">单片机/工控</a>
        <a href="/forums/ASM">汇编语言</a>
        <a href="/forums/VxWorks">VxWorks开发</a>
      </dd>
    </dl>
    <dl>
      <dt><a href="/forums/Linux">Linux/Unix社区</a></dt>
      <dd>
        <a href="/forums/Linux_System">系统维护与使用区</a>
        <a href="/forums/Linux_Development">应用程序开发区</a>
        <a href="/forums/Linux_Kernel">内核源代码研究区</a>
        <a href="/forums/Linux_Driver">驱动程序开发区</a>
        <a href="/forums/Linux_Hardware">CPU和硬件区</a>
      </dd>
    </dl>
  </div>
</span>

      <a href="/help" class="">论坛帮助</a>
      <a href="/rank" class="">论坛牛人</a>
      <a href="/map" class="">论坛地图</a>
      <a href="/ask" class="">专家问答</a>
    </div>
  </div>
</div>
    <div class="wraper">
        <!-- 页顶通栏 -->
    <div id="Topic_Top">
      <!--<style type="text/css">-->
          <!--/*body,ul{width:960px;float:left;font-size:1px;margin:0;padding:0}*/-->
          <!--/*ul li.l{float:left;}*/-->
          <!--/*ul li.r{float:right;}*/-->
          <!--/*li{list-style: none;}*/-->
      <!--</style>-->
      <!--<body>-->
      <ul id="topic-detail-ad-ul">
      	<li>
          <script type="text/javascript"><!--
          google_ad_client = "ca-pub-8990951720398508";
          /* 论坛帖子页置顶Banner-960*90 */
          google_ad_slot = "8267689356/1778791602";
          google_ad_width = 960;
          google_ad_height = 90;
          //-->
          </script>
          <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"></script>
      	</li>
        <!--<li class="l" id="topic-detail-ad-l">
          <ins data-revive-zoneid="53" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
        </li>
        <li class="r" id="topic-detail-ad-r">
          <ins data-revive-zoneid="54" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
        </li>-->
      </ul>
      <!--</body>-->
    </div>

      <!--[if IE]>
<style type="text/css" media="screen">
  .control_area .control .drop_menu{border:3px solid #ccc \9; _*border:3px solid #ccc;}
</style>
<![endif]-->

<!-- 页顶Button (D3) -->
<div marginwidth="0" marginheight="0" scrolling="no" width="100%">
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <style>
      body {margin:0px;padding:0px;}
      .bbs_top_ad{clear:both; text-align:left; display:block; *display:inline-block; width:960px; margin:2px 0; padding:2px 9px; border:solid 1px #a9cbee; /* -moz-border-radius:8px; background:#d8d8d8; */ color:#000; list-style:none; font-size:12px; line-height:20px;}
      .bbs_top_ad:after{content:"."; display:block; height:0; clear:both; visibility:hidden;}
      .bbs_top_ad a{color:#666; text-decoration:none;}
      .bbs_top_ad a:hover{text-decoration:underline;}
      .bbs_top_ad *{margin:0; padding:0; list-style:none;}
      .bbs_top_ad h3{width:330px; max-width:330px; height:20px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; font-size:14px; line-height:20px;}
      .bbs_top_ad h3:after{content:"...";}
      .bbs_top_ad h3 a{color:#000;}
      .bbs_top_ad .area_1 li,
      .bbs_top_ad .area_2 li{padding:0 0 0 9px; background:url(http://c.csdnimg.cn/www/images/point_1.gif) no-repeat left 8px; width:340px; height:20px; overflow:hidden; display:inline-block;}
      .bbs_top_ad .area_1{float:left; width:350px; overflow:hidden; margin:0 10px 0 0; padding:4px 0; /*background:#f8f8f8;*/}
      .bbs_top_ad .area_2{position:relative; float:left; width:355px; overflow:hidden; margin:0 20px 0 0; padding:4px 0; /*background:#f8f8f8;*/}
      .bbs_top_ad .area_2 ul{height:80px; overflow:hidden;}
      .area_1 ul {height:40px; overflow:hidden;}
      #scrollDiv li { display:inherit; width:200px; }
      #scrollDiv2 li { background:url(http://c.csdnimg.cn/www/images/point_pin.gif) no-repeat left 4px; }
      .bbs_top_ad #btn1{float:left; width:15px; height:15px; border:none; background:#5d5d5d; color:#fff; font-size:12px; line-height:15px; cursor:pointer;}
      .bbs_top_ad #btn2{float:left; margin-left:10px; width:15px; height:15px; border:none; background:#5d5d5d; color:#fff; font-size:12px; line-height:15px; cursor:pointer;}
      .bbs_top_ad .area_3{float:left; width:220px; overflow:hidden; padding:4px 0 0 0;}
      .bbs_top_ad .area_3 a{color:#000;}
      .bbs_top_ad .area_3 dt{margin-bottom: 5px;}
      .bbs_top_ad .area_3 dd{width:193px; height:20px; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; padding:0 0 0 17px; background:url(http://c.csdnimg.cn/www/images/point_huo.gif) no-repeat left 3px;}
      /* .bbs_top_ad .area_3 dd:after{content:"...";}*/
      .bbs_top_ad .area_1 h3 li,.bbs_top_ad .area_2 h3 li { list-style:none; background:none; padding:0;}
  </style>
  <script type="text/javascript" src="http://ag.csdn.net/js/jquery.scroll.js"></script>
  <script type="text/javascript">
      $(document).ready(function () {
          $("#scrollDiv").Scroll({ line: 4, speed: 1, timer: 6000, left: "btn1", right: "btn2" });
          $("#scrollDiv2").Scroll({ line: 8, speed: 1, timer: 6000 });
          jQuery.noConflict();
      });
  </script>
</head>

<body>
<div class="bbs_top_ad">
  <div class="area_1">
    <h3>
      <script type="text/javascript" src="http://ag.csdn.net/common/jobsget.ashx?rssurl=http://temp.csdn.net/Feed.aspx?Column=5001c99f-c2c9-4db6-b263-0c2c1c30f64b&count=1"></script>
    </h3>
    <ul>
      <script type="text/javascript" src="http://ag.csdn.net/common/jobsget.ashx?rssurl=http://temp.csdn.net/Feed.aspx?Column=df5147d1-1fb4-434c-be66-2293268d8920&count=2"></script>
    </ul>
    <div style="float:left;width:260px;">
      <div id="scrollDiv1">
        <script type="text/javascript" src="http://ag.csdn.net/common/ArticleGet.ashx"></script>
      </div>
    </div><div style="float:left;padding-top:22px;">
    <button id="btn1">&lt;&lt;</button>
    <button id="btn2">&gt;&gt;</button></div>
  </div>
  <div class="area_2">
    <h3>
      <script type="text/javascript" src="http://ag.csdn.net/common/getcmsad.ashx?column=1463c0fb-6332-4732-aa50-cc4c0668a14e&count=1"></script>
    </h3>
    <div id="scrollDiv" class="scrollDiv">
      <ul>
        <!--<script type="text/javascript">-->
        <!--var url = encodeURIComponent(location.href);-->
        <!--var id = 3;-->
        <!--function ad_two_callback(ad_result){-->
        <!--$('#scrollDiv2 ul').append(ad_result);-->
        <!--};-->
        <!--document.write(unescape('%3Cscript%20src%3D%22http%3A//a.pongo.cn/Job/GetAdForCallBack%3Fid%3D'+id+'%26UrlAdParam%3D'+encodeURIComponent(url)+'%26CallBack%3D'+ 'ad_two_callback' +'%22%20type%3D%22text/javascript%22%3E%3C/script%3E')); -->
        <!--</script>-->
        <script type="text/javascript" src="http://ag.csdn.net/common/getcmsad.ashx?column=69f12a65-956a-4647-b352-642016a4d64d&count=1"></script>
      </ul>
    </div>
  </div>
  <div class="area_3">
    <dl>
      <dt>
        <script type="text/javascript">
          /*论坛帖子页右侧Button-220*120，创建于 2015-11-10*/
          var cpro_id = "u2394820";
        </script>
        <script type="text/javascript" src="http://cpro.baidustatic.com/cpro/ui/c.js"></script>
      </dt>

    </dl>
  </div>
</div>
</body>
</div>
<!--<iframe id="frm_tt1" marginwidth="0" marginheight="0" frameborder="0" scrolling="no" width="100%" src="/sda/TopicBodyTop.htm?v=1"></iframe>-->
<script type="text/javascript">
//  setTimeout(function () { document.getElementById("frm_tt1").src = "/sda/TopicBodyTop.htm?v="+new Date().getTime(); }, 5000);

  $(function(){
      //获取要定位元素距离浏览器顶部的距离
      $ = jQuery;
      var navH = $(".detail_title_fixed").offset().top;
      $(".detail_title_fixed").hide();

      var show_detail_title_fixed = true;
      //滚动条事件
      $(window).scroll(function(){

          //获取滚动条的滑动距离
          var scroH = $(this).scrollTop();

          //滚动条的滑动距离大于等于定位元素距离浏览器顶部的距离，就固定，反之就不固定
          if(show_detail_title_fixed){
              if(scroH>=navH){
                  $(".detail_title_fixed").css({"position":"fixed","top":"0","border":"1px #198cc5 solid","z-index":"99999"});
                  $(".detail_title_fixed").show();
              }else if(scroH<navH){
                  $(".detail_title_fixed").css({"position":"static"});
                  $(".detail_title_fixed").hide();
              }
          }
      });

      $("#close_detail_title_fixed").click(function(){
          show_detail_title_fixed = false;
          $(".detail_title_fixed").hide();
      });

      $("#com-back-home").click(function(){
        window.location.href="/";
      });

      $("#com-back-channel").click(function(){
          window.location.href="/forums/J2EE";
      });
  })
</script>

  <script type="text/javascript">
      //百度代码：
      (function(){
      var bp = document.createElement('script');
      var curProtocol = window.location.protocol.split(':')[0];
      if (curProtocol === 'https') {
          bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
      }else{
          bp.src = 'http://push.zhanzhang.baidu.com/push.js';
      }
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(bp, s);
      })();
  </script>

  <script type="text/javascript">
      //360代码：
      (function(){
          var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?c71f2015985311cb113b45ca024ff1ec":"https://jspassport.ssl.qhimg.com/11.0.1.js?c71f2015985311cb113b45ca024ff1ec";
          document.write('<script src="' + src + '" id="sozz"><\/script>');
      })();
  </script>



<div class="bread_nav">
  <a href="http://www.csdn.net" target="_blank">CSDN</a> <em>&gt;</em>
  <a href="/" target="_blank">CSDN论坛</a> <em>&gt;</em>
    <a href="/forums/Java" target="_blank">Java</a> <em>&gt;</em>
  <a href="/forums/J2EE" target="_blank">Java EE</a>
</div>

<div class="flash_messages">
</div>

<div class="control_area top">
  <form name="form" id="form">
    
    <span class='back_to_forum_list'><a href="/forums/J2EE">返回列表</a></span>
    <div class="control">
      <ul>
        <li class="drop_menu_wrap drop_menu_down">
          <a href="#" class="drop_toggle btn_1 " rel='nofollow'>
            <span>
              <img src="/assets/ico_set.gif" alt="" />管理菜单<img src="/assets/arrow_down.gif" alt="" />
            </span>
          </a>
          <ul class="drop_menu" style="display: none; top:26px;">
              <li><a href="/topics/392258624/top" class="fancybox" rel="nofollow">置顶</a></li>

  <li><a href="/topics/392258624/recommend" data-confirm="您确定要推荐该帖吗？帖子被推荐后将奖励发帖用 户88个可用分和3个C币!" data-method="put" rel="nofollow">推荐</a></li>

  <li><a href="/topics/392258624/lock" class="fancybox" rel="nofollow">锁定</a></li>

<li><a href="/topics/392258624/move" class="fancybox" rel="nofollow">移动</a></li>
<li><a href="/topics/392258624/edit" class="fancybox" rel="nofollow">编辑</a></li>
<li><a href="/topics/392258624/destroy_edit" class="fancybox" rel="nofollow">删除</a></li>
<li><a href="/topics/392258624/add_point" class="fancybox" rel="nofollow">帖子加分</a></li>
  <li><a href="/topics/392258624/highlight" class="fancybox" rel="nofollow">帖子高亮</a></li>

          </ul>
        </li>
        <li>
          <a href="/topics/392258624/close" class="btn_1 close_topic" rel='nofollow'>
            <span><img src="/assets/ico_over.gif" alt="" />结帖</span>
          </a>
        </li>
        <li>
          <a href="/topics/new?forum_id=J2EE" class="btn_1 create_topic" rel='nofollow'>
            <span><img src="/assets/ico_publish.gif" alt="" />发帖</span>
          </a>
        </li>
        <li>
          <a href="#new_post" class="btn_1 reply_topic" rel='nofollow'>
            <span><img src="/assets/ico_return.gif" alt="" />回复</span>
          </a>
        </li>
          <li>
            <a href="/topics/392258624/attetion" class="btn_1 reply_topic" rel='nofollow'>
              <span><img src="/assets/ico_attention_topic.png" title="关注" />关注</span>
            </a>
          </li>
      </ul>
    </div>
  </form>
</div>

<div class="h-entry">
  <a class="p-author" href="#">sinat_19250161</a>
</div>


<div class="detail_tbox">
    <div class="detail_title_fixed">
      <h1>
            <span class="title text_overflow">ImageIO.write 写入gif 图片 报错 图片黑屏不会动</span>
        <span>
          [问题点数：100分]
        </span>
      </h1>

      <div class="fixed-r">
        <a href="#new_post" class="bbs-btn-blue26">快速回复</a>
            <a href="/topics/392258624?list=lz" class="bbs-btn-blue26">只显示楼主</a>
            <a href="/topics/392258624/attetion" class="bbs-btn-blue26">关注帖子</a>
        <a href="javascript:void(0);" id="close_detail_title_fixed" class="bbs-btn-close"> </a>
      </div>
    </div>
    <div class="detail_title">
      <h1>
          <span class="title text_overflow">ImageIO.write 写入gif 图片 报错 图片黑屏不会动</span>
        <span>
          [问题点数：100分]
        </span>
      </h1>
      <div class="fr">
        <select name="filter_posts">
          <option value="default">不显示删除回复</option>
          <option value="all">显示所有回复</option>
          <option value="star">显示星级回复</option>
          <option value="pointed">显示得分回复</option>
          <option value="lz">只显示楼主</option>
        </select>
        <a href="http://my.csdn.net/my/favorite/miniadd?u=http://bbs.csdn.net/topics/392258624&amp;t=ImageIO.write%20%E5%86%99%E5%85%A5gif%20%E5%9B%BE%E7%89%87%20%E6%8A%A5%E9%94%99%20%E5%9B%BE%E7%89%87%E9%BB%91%E5%B1%8F%E4%B8%8D%E4%BC%9A%E5%8A%A8" id="fav" class="fav" rel='nofollow'><img src="/assets/nolines_plus.gif" alt="" />收藏</a>
      </div>
    </div>
</div>
<div class="detailed">
    

<table border="0" cellspacing="0" cellpadding="0" id="post-402710995"
  class="post topic "
  data-post-id="402710995" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info topic" data-username="sinat_19250161" data-floor="">
        
        <div class="post_body">

              <div class="tag">
                  <span><a href="http://www.csdn.net/tag/gif" target="_blank">gif</a></span>
                  <span><a href="http://www.csdn.net/tag/ImageIO" target="_blank">ImageIO</a></span>
                  <span><a href="http://www.csdn.net/tag/Toolkit" target="_blank">Toolkit</a></span>
                  <span><a href="http://www.csdn.net/tag/BufferedImage" target="_blank">BufferedImage</a></span>
              </div>
                  <pre class="brush: java">	<br />
//&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;String&nbsp;path&nbsp;=&nbsp;PropertityUtils.getValue("picPath")+imagePath;<br />
		String&nbsp;path&nbsp;=&nbsp;"E:/a.gif";<br />
		File&nbsp;srcFile&nbsp;=&nbsp;new&nbsp;File(path);<br />
		<br />
		if(srcFile.exists()){<br />
			<br />
			try&nbsp;{<br />
				BufferedImage&nbsp;srcImg&nbsp;=&nbsp;ImageIO.read(srcFile);<br />
				BufferedImage&nbsp;buffImg&nbsp;=&nbsp;null;<br />
				buffImg&nbsp;=&nbsp;new&nbsp;BufferedImage(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.TYPE_INT_RGB);<br />
				&nbsp;java.awt.Image&nbsp;image&nbsp;=Toolkit.getDefaultToolkit().createImage(&nbsp;TestImageBinary.class.getResource(path));<br />
				&nbsp;buffImg.getGraphics().drawImage(image,&nbsp;0,0,&nbsp;null);<br />
				&nbsp;<br />
//				&nbsp;buffImg.getGraphics().drawImage(<br />
//						srcImg.getScaledInstance(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.SCALE_SMOOTH),&nbsp;0,<br />
//						0,&nbsp;null);<br />
			<br />
				buffImg.getGraphics().dispose();<br />
				ImageIO.write(buffImg,&nbsp;"JPEG",&nbsp;response.getOutputStream());<br />
			}&nbsp;catch&nbsp;(IOException&nbsp;&nbsp;e)&nbsp;{<br />
				//&nbsp;TODO&nbsp;Auto-generated&nbsp;catch&nbsp;block<br />
				e.printStackTrace();<br />
			}<br />
			<br />
			<br />
		}<br />
</pre><br />
<br />
以上是我的代码<br />
报错信息<br />
<pre class="brush: java"><br />
Uncaught&nbsp;error&nbsp;fetching&nbsp;image:<br />
java.lang.NullPointerException<br />
	at&nbsp;sun.awt.image.URLImageSource.getConnection(URLImageSource.java:116)<br />
	at&nbsp;sun.awt.image.URLImageSource.getDecoder(URLImageSource.java:126)<br />
	at&nbsp;sun.awt.image.InputStreamImageSource.doFetch(InputStreamImageSource.java:263)<br />
	at&nbsp;sun.awt.image.ImageFetcher.fetchloop(ImageFetcher.java:205)<br />
	at&nbsp;sun.awt.image.ImageFetcher.run(ImageFetcher.java:169)<br />
DEBUG[com.frontdo.travel.interceptor.AuthInterceptor]-信息:request&nbsp;/travel/action/acquireUploadImage,prcess&nbsp;time&nbsp;:244ms<br />
DEBUG[org.mybatis.spring.SqlSessionUtils]-信息:Creating&nbsp;a&nbsp;new&nbsp;SqlSession<br />
</pre><br />
页面显示<br />
黑屏&nbsp;只有个宽高



              <div id='topic-extra-info'>
                <div class='social-share' >
  <!-- Baidu Button BEGIN -->
  <span id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
    <a class="bds_tsina"></a>
    <a class="bds_tqq"></a>
    <span class="bds_more">更多</span>
    <a class="shareCount"></a>
  </span>
  <span class='prompt'>分享到：</span>
  <script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=3329407" ></script>
  <script type="text/javascript" id="bdshell_js"></script>
  <script type="text/javascript">
    var bds_config = {
      "snsKey": { 
        'tsina': '3657746030',
        'tqq': '801356742',
      }
    };

    document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000)
  </script>
  <!-- Baidu Button END -->
</div>

                <!-- 广告位开始 -->
                <script type="text/javascript"><!--
                google_ad_client = "ca-pub-8990951720398508";
                /* 论坛帖子页下方Banner1-728*90 */
                google_ad_slot = "8267689356/7950890202";
                google_ad_width = 728;
                google_ad_height = 90;
                //-->
                </script>
                <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"></script>
                <!-- 广告位结束 -->
              </div>

              <!-- 主帖下Banner (D4) -->
              <!-- 主帖下文字 (D5) -->
                  <div marginwidth="0" marginheight="0" scrolling="no" width="100%">
                    <style type="text/css">
    /***Business text AD***/
    /*body {margin:0; padding: 0;font:normal 12px simsun; }*/
    .adtxt{text-align:center;}
    .adtxt ul{margin:5px 0;border-top:1px solid #B9B9B9;border-bottom:1px solid #B9B9B9;background-color:#F2F6FB;padding:5px 0;}
    .adtxt ul li{display: inline-block;font-size:12px;}
    .adtxt ul li a{color:#333;}
    /*a{color: #002D93;text-decoration:none;}*/
    /*a:visited{color: #B00;text-decoration:none;}*/
    /*a:hover{color: #B00; text-decoration: underline;}*/
</style>

<body>
<div id="bd_ad_2" style="margin:0; padding-bottom:5px; display:block; text-align: center">
  <script type="text/javascript"><!--
  google_ad_client = "ca-pub-8990951720398508";
  /* 论坛帖子页下方banner2-728*90 */
  google_ad_slot = "8267689356/8197924482";
  google_ad_width = 728;
  google_ad_height = 90;
  //-->
  </script>
  <script type="text/javascript"
          src="//pagead2.googlesyndication.com/pagead/show_ads.js">
  </script>
</div>
<div class="adtxt">
  <ul>
    <li style="margin-top:0px;vertical-align:top;margin-right:35px;max-width:230px;max-height:20px;overflow:hidden;">
      <ins data-revive-zoneid="59" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
    </li>
    <li style="margin-right:35px;">
      <script type="text/javascript">
        /*论坛帖子页下方文字链2 创建于 2014-07-03*/
        var cpro_id = "u1636201";
      </script>
      <script type="text/javascript" src="http://cpro.baidustatic.com/cpro/ui/c.js"></script>
    </li>
    <li>
      <script type="text/javascript">
        /*论坛帖子页下方文字链3创建于 2014-07-03*/
        var cpro_id = "u1636204";
      </script>
      <script type="text/javascript" src="http://cpro.baidustatic.com/cpro/ui/c.js"></script>
    </li>
  </ul>
</div>
</body>
                  </div>
        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              发表于：
    2017-09-05 11:56:59
  </span>


      <strong class="fr">
        楼主
      </strong>

  <div class="fr">
      <a href="/posts/402710995/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402710995/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402710995/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/topics/392258624/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/topics/392258624/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>
    <span class="return_time">回复次数：14</span>


</div>


      </td>
  </tr>
</table>


    <div id="topic-suggest">
        <div id="real_topic">
          <div class="related-tags" id="suggest_tags">
</div>

          <div class="related-topics tracking-ad" data-pid="bbs" data-mod="popu_18"  id="suggest_topics">
</div>
          <div class="related-topics" data-pid="bbs" data-mod="popu_84" id="suggest_course">
</div>
        </div>
        <!--<div id="job_bbs_reco">-->
          <!--<script src="http://c.csdnimg.cn/jobreco/job_reco.js" type="text/javascript"></script>-->
        <!--</div>-->
</div>
    <script>
        var topic_suggest = $('#topic-suggest');
        $('#topic-extra-info').append(topic_suggest);
      </script>
    <script type="text/javascript">
		$(function(){
			  document.domain = 'csdn.net';
			  ajaxProxy(proxy_url, {
		        headers: {
		            'X-acl-token': 'FdGFBxj3XMufW1DtRaB7cPrnT1MK'
		        },
		        type: "post",
		        url: "http://internalapi.csdn.net/knowledge/api/api/base/getInfoByKeyword",
		        data: {keyword: "gif,ImageIO,Toolkit,BufferedImage"},        
		        dataType: "json",
		        success: function(data) {
		        	document.domain = 'csdn.net';
		            
							if (data.bases != undefined) {	
								var html = '<span>相关知识库：</span>';
								for(var i = 0; i < data.bases.length; i++){
							    var item = data.bases[i];	    
							    html +=  '<a target="_blank" href="'+item.url+'">'+item.name.replace(/知识库/,'')+'</a>';
							  }	
								$("#suggest_tags").append(html).fadeIn();       
							} else {
								$('#suggest_tags').remove();
							}
		        },
		        error: function(err){
		        	$('#suggest_tags').fadeOut();
		        	console.log(err);
		        }
		    });
		})
		</script>


  

<table border="0" cellspacing="0" cellpadding="0" id="post-402710997"
  class="post  "
  data-post-id="402710997" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="1">
        
        <div class="post_body">

                  <img src="http://img.bbs.csdn.net/upload/201709/05/1504583848_33449.png" alt="" />&nbsp;页面就这个样子



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 11:57:42
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402710997">#1</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-1'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402710997/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402710997/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402710997/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402710997/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402710997/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711001"
  class="post  "
  data-post-id="402711001" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="2">
        
        <div class="post_body">

                  快来个大神&nbsp;帮帮忙



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 11:58:27
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711001">#2</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-2'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711001/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711001/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711001/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711001/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711001/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711104"
  class="post  "
  data-post-id="402711104" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="q54244125">
            <a href="http://my.csdn.net/q54244125" rel="nofollow" target="_blank"><img alt="q54244125" class="avatar" src="http://avatar.csdn.net/C/C/A/1_q54244125.jpg" /></a>
          </dt>
              <!--<dd id="65219680_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/65219680/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="65219680_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/65219680/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/q54244125" rel="nofollow" target="_blank" title="q54244125">q54244125</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">q54244125</span>
            <img alt="T3" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t3.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：730
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：0%
总发帖：0
正常结帖：0
未结帖：0">结帖率：0%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="q54244125" data-floor="3">
        
        <div class="post_body">

                  是不是&nbsp;没有正常初始化对象，导致空指针的。



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 12:37:08
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711104">#3</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-3'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711104/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711104/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711104/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711104/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711104/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711169"
  class="post  "
  data-post-id="402711169" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="4">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;3&nbsp;楼&nbsp;q54244125&nbsp;的回复:</legend><blockquote>是不是&nbsp;没有正常初始化对象，导致空指针的。</blockquote></fieldset><br />
你指的是哪个？



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 13:00:34
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711169">#4</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-4'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711169/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711169/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711169/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711169/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711169/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711314"
  class="post  "
  data-post-id="402711314" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="u010049086">
            <a href="http://my.csdn.net/u010049086" rel="nofollow" target="_blank"><img alt="u010049086" class="avatar" src="http://avatar.csdn.net/5/E/B/1_u010049086.jpg" /></a>
          </dt>
              <!--<dd id="31261698_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/31261698/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="31261698_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/31261698/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/u010049086" rel="nofollow" target="_blank" title="u010049086">u010049086</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">u010049086</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：206
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：0%
总发帖：0
正常结帖：0
未结帖：0">结帖率：0%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="u010049086" data-floor="5">
        
        <div class="post_body">

                  用FileInputStream吧，管它是文本还是图片，都可以还原，



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 13:39:29
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711314">#5</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-5'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711314/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711314/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711314/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711314/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711314/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711433"
  class="post  "
  data-post-id="402711433" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="JJYYyibanhua">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank"><img alt="JJYYyibanhua" class="avatar" src="http://avatar.csdn.net/8/B/8/1_jjyyyibanhua.jpg" /></a>
          </dt>
              <!--<dd id="18550789_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/18550789/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="18550789_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/18550789/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank" title="JJYYyibanhua">JJYYyibanhua</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">JJYYyibanhua</span>
            <img alt="T3" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t3.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：832
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：100%
总发帖：3
正常结帖：3
未结帖：0">结帖率：100%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="JJYYyibanhua" data-floor="6">
        
        <div class="post_body">

                  看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 14:01:16
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711433">#6</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-6'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711433/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711433/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711433/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711433/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711433/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711652"
  class="post  "
  data-post-id="402711652" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="7">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote>看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 14:52:09
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711652">#7</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-7'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711652/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711652/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711652/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711652/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711652/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711746"
  class="post  "
  data-post-id="402711746" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="JJYYyibanhua">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank"><img alt="JJYYyibanhua" class="avatar" src="http://avatar.csdn.net/8/B/8/1_jjyyyibanhua.jpg" /></a>
          </dt>
              <!--<dd id="18550789_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/18550789/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="18550789_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/18550789/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank" title="JJYYyibanhua">JJYYyibanhua</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">JJYYyibanhua</span>
            <img alt="T3" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t3.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：832
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：100%
总发帖：3
正常结帖：3
未结帖：0">结帖率：100%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="JJYYyibanhua" data-floor="8">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;7&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><fieldset><legend>Quote: 引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过</blockquote></fieldset><br />
怎么会编译不通过，报的什么错？ImageIcon这里？



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 15:14:50
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711746">#8</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-8'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711746/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711746/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711746/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711746/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711746/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711768"
  class="post  "
  data-post-id="402711768" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="9">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;8&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><fieldset><legend>Quote: 引用&nbsp;7&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过</blockquote></fieldset><br />
怎么会编译不通过，报的什么错？ImageIcon这里？</blockquote></fieldset><br />
通过了&nbsp;&nbsp;又出新错误了&nbsp;<br />
java.lang.OutOfMemoryError:&nbsp;Java&nbsp;heap&nbsp;space<br />
<br />
<br />
<br />
<br />
BufferedImage&nbsp;srcImg&nbsp;=&nbsp;ImageIO.read(srcFile);<br />
				BufferedImage&nbsp;buffImg&nbsp;=&nbsp;null;<br />
				buffImg&nbsp;=&nbsp;new&nbsp;BufferedImage(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.TYPE_INT_RGB);<br />
				FileInputStream&nbsp;inStream&nbsp;=&nbsp;new&nbsp;FileInputStream(srcFile);<br />
				byte[]&nbsp;inOutb&nbsp;=&nbsp;new&nbsp;byte[inStream.available()];<br />
				java.awt.Image&nbsp;image&nbsp;=Toolkit.getDefaultToolkit().createImage(inOutb);<br />
				ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image);<br />
				buffImg.getGraphics().drawImage(image,&nbsp;0,0,&nbsp;null);<br />
				&nbsp;<br />
//				&nbsp;buffImg.getGraphics().drawImage(<br />
//						srcImg.getScaledInstance(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.SCALE_SMOOTH),&nbsp;0,<br />
//						0,&nbsp;null);<br />
			<br />
				buffImg.getGraphics().dispose();<br />
				ImageIO.write(buffImg,&nbsp;"JPEG",&nbsp;response.getOutputStream());



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 15:18:53
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711768">#9</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-9'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711768/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711768/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711768/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711768/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711768/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402711920"
  class="post  "
  data-post-id="402711920" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="JJYYyibanhua">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank"><img alt="JJYYyibanhua" class="avatar" src="http://avatar.csdn.net/8/B/8/1_jjyyyibanhua.jpg" /></a>
          </dt>
              <!--<dd id="18550789_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/18550789/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="18550789_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/18550789/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/JJYYyibanhua" rel="nofollow" target="_blank" title="JJYYyibanhua">JJYYyibanhua</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">JJYYyibanhua</span>
            <img alt="T3" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t3.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：832
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：100%
总发帖：3
正常结帖：3
未结帖：0">结帖率：100%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="JJYYyibanhua" data-floor="10">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;9&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><fieldset><legend>Quote: 引用&nbsp;8&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;7&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过</blockquote></fieldset><br />
怎么会编译不通过，报的什么错？ImageIcon这里？</blockquote></fieldset><br />
<br />
通过了&nbsp;&nbsp;又出新错误了&nbsp;<br />
java.lang.OutOfMemoryError:&nbsp;Java&nbsp;heap&nbsp;space<br />
<br />
<br />
<br />
<br />
BufferedImage&nbsp;srcImg&nbsp;=&nbsp;ImageIO.read(srcFile);<br />
				BufferedImage&nbsp;buffImg&nbsp;=&nbsp;null;<br />
				buffImg&nbsp;=&nbsp;new&nbsp;BufferedImage(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.TYPE_INT_RGB);<br />
				FileInputStream&nbsp;inStream&nbsp;=&nbsp;new&nbsp;FileInputStream(srcFile);<br />
				byte[]&nbsp;inOutb&nbsp;=&nbsp;new&nbsp;byte[inStream.available()];<br />
				java.awt.Image&nbsp;image&nbsp;=Toolkit.getDefaultToolkit().createImage(inOutb);<br />
				ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image);<br />
				buffImg.getGraphics().drawImage(image,&nbsp;0,0,&nbsp;null);<br />
				&nbsp;<br />
//				&nbsp;buffImg.getGraphics().drawImage(<br />
//						srcImg.getScaledInstance(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.SCALE_SMOOTH),&nbsp;0,<br />
//						0,&nbsp;null);<br />
			<br />
				buffImg.getGraphics().dispose();<br />
				ImageIO.write(buffImg,&nbsp;"JPEG",&nbsp;response.getOutputStream());</blockquote></fieldset><br />
<br />
内存溢出。。。java&nbsp;堆内存溢出了。。。&nbsp;重启再试下&nbsp;&nbsp;&nbsp;这是设置的有多大。。。



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 15:49:39
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402711920">#10</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-10'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402711920/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402711920/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402711920/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402711920/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402711920/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402712010"
  class="post  "
  data-post-id="402712010" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="11">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;10&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><fieldset><legend>Quote: 引用&nbsp;9&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;8&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;7&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过</blockquote></fieldset><br />
怎么会编译不通过，报的什么错？ImageIcon这里？</blockquote></fieldset><br />
<br />
通过了&nbsp;&nbsp;又出新错误了&nbsp;<br />
java.lang.OutOfMemoryError:&nbsp;Java&nbsp;heap&nbsp;space<br />
<br />
<br />
<br />
<br />
BufferedImage&nbsp;srcImg&nbsp;=&nbsp;ImageIO.read(srcFile);<br />
				BufferedImage&nbsp;buffImg&nbsp;=&nbsp;null;<br />
				buffImg&nbsp;=&nbsp;new&nbsp;BufferedImage(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.TYPE_INT_RGB);<br />
				FileInputStream&nbsp;inStream&nbsp;=&nbsp;new&nbsp;FileInputStream(srcFile);<br />
				byte[]&nbsp;inOutb&nbsp;=&nbsp;new&nbsp;byte[inStream.available()];<br />
				java.awt.Image&nbsp;image&nbsp;=Toolkit.getDefaultToolkit().createImage(inOutb);<br />
				ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image);<br />
				buffImg.getGraphics().drawImage(image,&nbsp;0,0,&nbsp;null);<br />
				&nbsp;<br />
//				&nbsp;buffImg.getGraphics().drawImage(<br />
//						srcImg.getScaledInstance(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.SCALE_SMOOTH),&nbsp;0,<br />
//						0,&nbsp;null);<br />
			<br />
				buffImg.getGraphics().dispose();<br />
				ImageIO.write(buffImg,&nbsp;"JPEG",&nbsp;response.getOutputStream());</blockquote></fieldset><br />
<br />
内存溢出。。。java&nbsp;堆内存溢出了。。。&nbsp;重启再试下&nbsp;&nbsp;&nbsp;这是设置的有多大。。。</blockquote></fieldset><br />
重启了&nbsp;也没用&nbsp;&nbsp;byte[]&nbsp;inOutb&nbsp;=&nbsp;new&nbsp;byte[inStream.available()];&nbsp;这里报错<br />




        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 16:12:37
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402712010">#11</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-11'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402712010/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402712010/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402712010/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402712010/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402712010/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402712117"
  class="post  "
  data-post-id="402712117" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="12">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;10&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><fieldset><legend>Quote: 引用&nbsp;9&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;8&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;7&nbsp;楼&nbsp;sinat_19250161&nbsp;的回复:</legend><blockquote><br />
<fieldset><legend>Quote: 引用&nbsp;6&nbsp;楼&nbsp;JJYYyibanhua&nbsp;的回复:</legend><blockquote><br />
看报错，创建img失败了。<br />
<br />
先用字节流读取下，再调用下边<br />
Image&nbsp;image&nbsp;=&nbsp;Toolkit.getDefaultToolkit.createImage(byte[]&nbsp;args)<br />
ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image)</blockquote></fieldset><br />
这样编译不通过</blockquote></fieldset><br />
怎么会编译不通过，报的什么错？ImageIcon这里？</blockquote></fieldset><br />
<br />
通过了&nbsp;&nbsp;又出新错误了&nbsp;<br />
java.lang.OutOfMemoryError:&nbsp;Java&nbsp;heap&nbsp;space<br />
<br />
<br />
<br />
<br />
BufferedImage&nbsp;srcImg&nbsp;=&nbsp;ImageIO.read(srcFile);<br />
				BufferedImage&nbsp;buffImg&nbsp;=&nbsp;null;<br />
				buffImg&nbsp;=&nbsp;new&nbsp;BufferedImage(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.TYPE_INT_RGB);<br />
				FileInputStream&nbsp;inStream&nbsp;=&nbsp;new&nbsp;FileInputStream(srcFile);<br />
				byte[]&nbsp;inOutb&nbsp;=&nbsp;new&nbsp;byte[inStream.available()];<br />
				java.awt.Image&nbsp;image&nbsp;=Toolkit.getDefaultToolkit().createImage(inOutb);<br />
				ImageIcon&nbsp;imgIcon&nbsp;=&nbsp;new&nbsp;ImageIcon(image);<br />
				buffImg.getGraphics().drawImage(image,&nbsp;0,0,&nbsp;null);<br />
				&nbsp;<br />
//				&nbsp;buffImg.getGraphics().drawImage(<br />
//						srcImg.getScaledInstance(srcImg.getWidth(null),&nbsp;srcImg.getHeight(null),&nbsp;BufferedImage.SCALE_SMOOTH),&nbsp;0,<br />
//						0,&nbsp;null);<br />
			<br />
				buffImg.getGraphics().dispose();<br />
				ImageIO.write(buffImg,&nbsp;"JPEG",&nbsp;response.getOutputStream());</blockquote></fieldset><br />
<br />
内存溢出。。。java&nbsp;堆内存溢出了。。。&nbsp;重启再试下&nbsp;&nbsp;&nbsp;这是设置的有多大。。。</blockquote></fieldset><br />
现在不报错了&nbsp;&nbsp;&nbsp;但还是&nbsp;黑屏



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 16:33:36
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402712117">#12</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-12'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402712117/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402712117/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402712117/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402712117/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402712117/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402712363"
  class="post  "
  data-post-id="402712363" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="pany1209">
            <a href="http://my.csdn.net/pany1209" rel="nofollow" target="_blank"><img alt="pany1209" class="avatar" src="http://avatar.csdn.net/A/0/6/1_pany1209.jpg" /></a>
          </dt>
              <!--<dd id="62435370_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/62435370/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="62435370_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/62435370/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/pany1209" rel="nofollow" target="_blank" title="pany1209">pany1209</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">pany1209</span>
            <img alt="T7" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t7.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：26719
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：98.97%
总发帖：97
正常结帖：96
未结帖：1">结帖率：98.97%</dd>

          <dd class="showTittleDD">
                <span>
                   <img  src="http://c.csdnimg.cn/jifen/images/xunzhang/xunzhang/honghua.png" alt="Blank"  class="xunZhang" >
                   <div class="showTittle">
                     <div style="left: 18%; top: -8px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;"></div>
                     <dl>
                       <dt><img src="http://c.csdnimg.cn/jifen/images/xunzhang/xunzhang/honghuamiddle.png"></dt>
                       <dd>
                         <strong>红花</strong>
                         2017年8月 Java大版内专家分月排行榜第一<br/>2017年7月 Java大版内专家分月排行榜第一<br/>2017年6月 Java大版内专家分月排行榜第一<br/>2017年5月 Java大版内专家分月排行榜第一<br/>2017年4月 Java大版内专家分月排行榜第一<br/>2017年3月 Java大版内专家分月排行榜第一<br/>2017年2月 Java大版内专家分月排行榜第一
                       </dd>
                     </dl>
                   </div>
                </span>

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info star" data-username="pany1209" data-floor="13">
        
        <div class="post_body">

                  为什么不使用img标签显示就好了？？？



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 17:22:14
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402712363">#13</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-13'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402712363/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[1]</a>
      <a href="/posts/402712363/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402712363/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402712363/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402712363/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>





<table border="0" cellspacing="0" cellpadding="0" id="post-402712513"
  class="post  "
  data-post-id="402712513" data-is-topic-locked="false">
  <colgroup><col width="180" /><col /></colgroup>
  <tr>
      <td rowspan="2" valign="top" class="wirter">
                <dl class="user_info ">
          <dt class="user_head" data-username="sinat_19250161">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank"><img alt="sinat_19250161" class="avatar" src="http://avatar.csdn.net/0/F/5/1_sinat_19250161.jpg" /></a>
          </dt>
              <!--<dd id="41831643_bbs-btn-close-attention" class="bbs-user-att" style="display:none;">-->
                <!--<a href="/users/41831643/cancel_attention" class="bbs-btn-blue25 bbs-btn-close-attention" data-method="get" data-remote="true">取消关注</a>-->
              <!--</dd>-->
              <!--<dd id="41831643_bbs-btn-attention" class="bbs-user-att">-->
                <!--<a href="/users/41831643/attention" class="bbs-btn-blue25 bbs-btn-attention" data-method="get" data-remote="true">关注</a>-->
              <!--</dd>-->


          <dd class="username">
            <a href="http://my.csdn.net/sinat_19250161" rel="nofollow" target="_blank" title="sinat_19250161">sinat_19250161</a>
            

          </dd>
          <dd class="nickname">
            <span class="name2nick">sinat_19250161</span>
            <img alt="T2" class="topic_show_user_level" src="http://c.csdnimg.cn/jifen/images/xunzhang/t/t2.png" />
            <div class="topic_show_posts">
              <div class="smallTittle">
                <div class="JianJiao" style="left: 40%; top: -5px; position: absolute; width: 0; height: 0;border-left: 10px solid transparent;border-right: 10px solid transparent; border-bottom: 8px solid #ffffff;" ></div>
                本版专家分：266
              </div>
            </div>
          </dd>



          <dd class="close_rate" title="用户结帖率：94.74%
总发帖：19
正常结帖：18
未结帖：1">结帖率：94.74%</dd>

          <dd class="showTittleDD">

          </dd>

        </dl>

      </td>
      <td valign="top" class="post_info " data-username="sinat_19250161" data-floor="14">
        
        <div class="post_body">

                  <fieldset><legend class="font_bold">引用&nbsp;13&nbsp;楼&nbsp;pany1209&nbsp;的回复:</legend><blockquote>为什么不使用img标签显示就好了？？？</blockquote></fieldset><br />
接口&nbsp;给手机端用的



        </div>

      </td>
    </tr>
    <tr>
      <td valign="bottom">
          
<div class="control">

  <span class="time">
              回复于：
    2017-09-05 17:55:18
  </span>


            <span class="fr" style="margin-left:50px;">
              <a href="#post-402712513">#14</a>
              得分：0
            </span>

    <div id='post-forum-bulletin-14'  class='fl tracking-ad' data-mod='popu_9'>
    </div>
  <div class="fr">
      <a href="/posts/402712513/digg?topic_id=392258624" class="red digg" data-method="put" data-remote="true" rel="nofollow">对我有用[0]</a>
      <a href="/posts/402712513/bury?topic_id=392258624" class="bury" data-method="put" data-remote="true" rel="nofollow">丢个板砖[0]</a>
      <a href="#quote" class="quote" rel='nofollow'>引用</a> |
      <a href="/posts/402712513/report?topic_id=392258624" class="fancybox red report_spam" rel="nofollow">举报 </a> |
    <span class="manage-toggle">
      <div class="manage" style="display: none;">
          <a href="/posts/402712513/edit" class="fancybox" rel="nofollow">编辑</a>
          <a href="/posts/402712513/destroy_edit" class="fancybox" rel="nofollow">删除</a>
      </div>
      管理
    </span>
  </div>


</div>


      </td>
  </tr>
</table>




</div>

<script type="text/javascript" charset="utf-8">
    $(function(){
        topics_page_js.show_page();
    });
</script>

<input type="hidden" id="autosave_post_val" value="" />
<input type="hidden" id="autosave_old_post_val"  />
<!-- <div class='around&#45;topics'> -->
<!--   <span class='preview'> -->
<!--      -->
<!--   </span> -->
<!--   | -->
<!--   <span class='next'> -->
<!--      -->
<!--   </span> -->
<!-- </div> -->

<div class="control_area bottom">
  <form name="form" id="form">
    
    <span class='back_to_forum_list'><a href="/forums/J2EE">返回列表</a></span>
    <div class="control">
      <ul>
        <li class="drop_menu_wrap drop_menu_up">
          <a href="#" class="drop_toggle btn_1 drop_toggle_up" rel='nofollow'>
            <span>
              <img src="/assets/ico_set.gif" alt="" />管理菜单<img src="/assets/arrow_down.gif" alt="" />
            </span>
          </a>
          <ul class="drop_menu" style="display: none; bottom:26px">
              <li><a href="/topics/392258624/top" class="fancybox" rel="nofollow">置顶</a></li>

  <li><a href="/topics/392258624/recommend" data-confirm="您确定要推荐该帖吗？帖子被推荐后将奖励发帖用 户88个可用分和3个C币!" data-method="put" rel="nofollow">推荐</a></li>

  <li><a href="/topics/392258624/lock" class="fancybox" rel="nofollow">锁定</a></li>

<li><a href="/topics/392258624/move" class="fancybox" rel="nofollow">移动</a></li>
<li><a href="/topics/392258624/edit" class="fancybox" rel="nofollow">编辑</a></li>
<li><a href="/topics/392258624/destroy_edit" class="fancybox" rel="nofollow">删除</a></li>
<li><a href="/topics/392258624/add_point" class="fancybox" rel="nofollow">帖子加分</a></li>
  <li><a href="/topics/392258624/highlight" class="fancybox" rel="nofollow">帖子高亮</a></li>

          </ul>
        </li>
        <li>
          <a href="/topics/392258624/close" class="btn_1 close_topic" rel='nofollow'>
            <span><img src="/assets/ico_over.gif" alt="" />结帖</span>
          </a>
        </li>
        <li>
          <a href="/topics/new?forum_id=J2EE" class="btn_1 create_topic" rel='nofollow'>
            <span><img src="/assets/ico_publish.gif" alt="" />发帖</span>
          </a>
        </li>
        <li>
          <a href="#new_post" class="btn_1 reply_topic" rel='nofollow'>
            <span><img src="/assets/ico_return.gif" alt="" />回复</span>
          </a>
        </li>
          <li>
            <a href="/topics/392258624/attetion" class="btn_1 reply_topic" rel='nofollow'>
              <span><img src="/assets/ico_attention_topic.png" title="关注" />关注</span>
            </a>
          </li>
      </ul>
    </div>
  </form>
</div>
<!--AdForward Begin:-->
<script type="text/javascript"><!--
google_ad_client = "ca-pub-8990951720398508";
/* 论坛帖子页回复框上Banner-960*90 */
google_ad_slot = "8267689356/2556735882";
google_ad_width = 960;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js"></script>
<!--AdForward End-->
<!-- 广告位：PC端-论坛帖子页-底部banner-960*190-2017/08/30 -->
<script>
    (function() {
        var s = "_" + Math.random().toString(36).slice(2);
        document.write('<div id="' + s + '"></div>');
        (window.slotbydup=window.slotbydup || []).push({
            id: '4708843',
            container: s,
            size: '960,190',
            display: 'inlay-fix'
        });
    })();
</script>

<div class="comt">
  <div class="ad_l">
    <!-- 回复框文字 (D6) -->
    <div id="topic_buttom_left_ad">
      <ins data-revive-zoneid="63" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
    </div>
    <ul class='tracking-ad' data-mod='popu_10'>
        <li><a href="http://ask.csdn.net/subjects/35" class="title_style_blue title_style_bold" target="_blank">高手问答--Linux内核专场</a></li>
        <li><a href="http://edu.csdn.net/huiyiCourse/detail/284" class="title_style_red title_style_bold" target="_blank">博客专家带你学swift</a></li>
        <li><a href="http://bbs.csdn.net/topics/392066539" class="title_style_black" target="_blank">晒图谱，涨知识，得好礼</a></li>
        <li><a href="http://e.cn.miaozhen.com/r/k=6002065&amp;p=4hU&amp;ctid=1&amp;rt=2&amp;ns=__IP__&amp;ni=__IESID__&amp;v=__LOC__&amp;vo=3b56fd611&amp;vr=2&amp;o=http%3A%2F%2Fwww.ibm.com%2Fdeveloperworks%2Fcn%2Fmobile%2Fzones%2Fswift%2Fq_a%2Findex.html%3Fcm_mmc%3Ddwchina-_-homepage-_-csdn-_-learn" class="title_style_red title_style_bold" target="_blank">Swift 问题与解答</a></li>
    </ul>
    <div class="ad_new tracking-ad" style='padding: 0 0 50px 0' data-mod='popu_11'>
      <h4><img alt="" src="http://c.csdnimg.cn/www/images/csdn_logo_blue.gif"></h4>
      <p class='title'>
      
      </p>
      <p class='con'>
      
      </p>
    </div>
  </div>
  <div class="reply">
      <form accept-charset="UTF-8" action="/posts?topic_id=392258624" class="new_post" id="new_post" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="JrmxnrS9i/bGIAZufh8IcXAdrkDlP+GTe+D9d6bhyZ8=" /></div>        <div>
          <strong>回复内容</strong>
            <span class="login">匿名用户不能发表回复！<a  href="javascript:void(0); " onclick='loginbox();' >登录</a>|<a href="https://passport.csdn.net/account/register" target="_blank">注册</a></span>
          &nbsp;&nbsp;<a href="http://www.csdn.net/app/" target="_blank" style="color: red">移动客户端回帖所得专家分翻倍，下载体验！</a>
        </div>
        <div class="editor">
          <textarea class="required quoteOnly" cols="40" id="post_body" name="post[body]" rows="20" style="width:100%;height:200px;">
</textarea>
          <div class="pub">
            <span class="fr">
              每天回帖即可获得10分可用分！小技巧：<a href="/help#common_problem" target="_blank" rel='nofollow'>教您如何更快获得可用分</a>
              <span id="body_count_notice" class="body_count_notice_fixed">你还可以输入10000个字符</span>
            </span>
            <input class="btn_b" id="submit_new_post_form" name="commit" type="submit" value="提交回复" />(Ctrl+Enter)
          </div>
        </div>
        <ol class="notice">
          <li>请遵守CSDN<a href='/help#user_criterion' rel='nofollow'>用户行为准则</a>，不得违反国家法律法规。</li>
          <li>转载文章请注明出自“CSDN（www.csdn.net）”。如是商业用途请联系原作者。</li>
        </ol>
</form>      <script id="countTemplate" type="text/x-jquery-tmpl">
        你还可以输入${count}个字符
      </script>

  </div>
</div>
<script>
  $(function(){
    $('.refresh-captcha').on('click', function(e){
      e.preventDefault();
      $('.captcha').load('/captchas/new');
    });
  });
  $(function(){
      showsuggest('post_body');
  });
</script>



<!-- 对联广告 -->
<div id="ad_left" style="display:none">
  <div>
    <ins data-revive-zoneid="56" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
<script type="text/javascript">  
  $(function(){
      if ($(parent.window).width() >= 1280) {
          parent.$('#ad_left').show();
      }
  });
</script>
  </div>
</div>
<div id="ad_right" style="display:none">
  <div>
    <ins data-revive-zoneid="57" data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57"></ins>
<script type="text/javascript">    
    $(function(){
        if ($(parent.window).width() >= 1280) {
            parent.$('#ad_right').show();
        }
    });
</script>
  </div>
</div>

<script>
  $(function(){
    window.onresize = function(){
      if($(parent.window).width() <= 1280){
        $('#ad_right').hide();
        $('#ad_left').hide();
      } else {
          $('#ad_right').show();
          $('#ad_left').show();
      }
    };
      if ($(parent.window).width() >= 1280) {
          $('#ad_right').show();
          $('#ad_left').show();
      }
  });

</script>


<!-- 浮层弹窗广告 -->
<!--AdForward Begin:-->
<div id="ad_pop">
  <div class="J_adv" data-view="true" data-mod="ad_popu_64" data-mtp="62" data-order="21" data-con="ad_content_2070">
    <script id="popuLayer_js_q" src="http://ads.csdn.net/js/popuLayer.js" defer="" type="text/javascript"></script>
    <div id="layerd" style="position: fixed; bottom: 0px; right: 0px; line-height: 0px; z-index: 1000; width: 300px; height: 278px;">
      <div class="J_close layer_close" style="display:block;background-color:#efefef;padding:0px;color:#333;font:12px/24px Helvetica,Tahoma,Arial,sans-serif;text-align:right;">
        关闭
      </div>
    <!--广告占位容器-->
    <div id="ad_abc">
      <script type="text/javascript">
        /*论坛帖子页弹窗广告-300*250*/
        var cpro_id = "u2895106";
      </script>
      <script type="text/javascript" src="http://cpro.baidustatic.com/cpro/ui/c.js"></script>
    </div>
    <script>document.getElementById('popuLayer_js_q').onload=function(){var styObjd=styObj={width:'300px','height':parseInt(250)+28};window.CSDN.Layer.PopuLayer('#layerd',{storageName:'layerd',styleObj:styObjd,total:50,expoire:1000*60});}</script>
  </div>
  </div>
</div>
<!--AdForward End-->


<!-- go-backhome   go-backchannel-->
<!-- <button id="com-back-home" class="btn btn-top bbs-btn-gray28 bbs-btn-backhome" title="回到首页" style="cursor: pointer; border: 0px none; bottom: 35px; width: 80px; height: 28px; margin: 0px; padding: 0px; position: fixed; right: 40px; display: block; padding-right:13px;">回到首页</button>-->
<!-- <button id="com-back-channel" class="btn btn-top bbs-btn-gray28 bbs-btn-backchannel" title="回到频道" style="cursor: pointer; border: 0px none; bottom:68px; width: 80px; height: 28px; margin: 0px; padding: 0px; position: fixed; right: 40px; display: block; padding-right:13px;">回到频道</button> -->
    </div>
            <script type="text/javascript">
            $(function()
                {
                    posts_page_js._form_page();
                });
        </script>
<script type="text/javascript" language="javascript" charset="utf-8">
window.bbsInfoflag = true;

//<![CDATA[
$(function(){
  $('.post .post_body fieldset+br').remove();
  $('.post .post_body blockquote').each(function(index, item) {
    var first_child = $(item).find(':first');
    if($(item).contents().get(0) !== undefined &&
      $(item).contents().get(0).nodeName.toLowerCase() === 'br' &&
      first_child.prop('tagName').toLowerCase() === 'br') {
      first_child.remove();
    }
  });
  
});

$(".showTittleDD span").hover(
        function () {
            $(this).find(".showTittle")[0].style.display="inline-block";
        },
        function () {
                $(this).find(".showTittle")[0].style.display="none";
        }
);

$(".topic_show_user_level").hover(
    function () {
    $(this).next().find(".smallTittle")[0].style.display="inline-block";


    },
    function () {
        $(this).next().find(".smallTittle")[0].style.display="none";
    }
);
//]]>
var auto_save_time = null;
$(document).ready(function(){
    autosavecontent = $("#autosave_post_val").val();
    if(autosavecontent != ''){$("#post_body").val(autosavecontent);}
    auto_save_time = setInterval(autosave, 90*1000);
});
function autosave(){
    var content =  $("#post_body").val();
    var old_content = $("#autosave_old_post_val").val();
    topic_id = 392258624
    if(content != "" && content != old_content) {
        $.ajax({
            type: 'post',
            dataType: 'json',
            url: '/posts/autosave_post',
            data: {
                content: content,
                topic_id: topic_id
            },
            success: function (result) {
                $("#autosave_old_post_val").val(content);
            },
            error: function (result) {
              if(result.status == 403 && result.responseText == '需要登录'){
                  clearInterval(auto_save_time);
              }
            }
        })
    }
}

$(function(){
    // 课程推荐
    $.ajax({
        url: "http://internalapi.csdn.net/psearch/psearch/query",
        type: "GET",
        data: {_client_: "rcommend_course",
                pro_id: "392258624",
                pro_type: "discussion_topic",
                fields: "created_at,tag,id,title,pic,stu_count,good_ratio,rc_flag,source_type",
                size: 4,
                user_id: "",
                index_name: "pro_course_v2",
                "x-acl-token": "wU4kru3sXrPwPGLhVloh9PV-n4YK"
               },
        dataType: 'JSONP',
        success: function(result){
            var res_arr = result['hits'];
            var text = "";
            if(res_arr.length > 0){
                text = "<span>相关推荐：</span><ul>";
                for(var key in res_arr){
                    var id = res_arr[key]['object']['id'];
                    var title = res_arr[key]['object']['title'];
                    text += "<li><a href='http://edu.csdn.net/course/detail/" +  id + "?ref=bbs&loc=0'" + " target='_blank'>" + title + "</a></li>";
                }
                text += "</ul>";
            }

            $('#suggest_course').html(text);

            var m = $("#suggest_course");

            //控制新创基数据触发曝光开关
            if(m.length>0){
                m.each(function(i){
                    console.log(i);
                    trackingAd($(this));
                });
            }
        }
    });

    // 标签推荐
    $.ajax({
        type: 'get',
        url: 'http://internalapi.csdn.net/recommend/tag/suggest',
        dataType: 'JSONP',
        data: {title: "ImageIO.write 写入gif 图片 报错 图片黑屏不会动",
                body: "[code=java]//Stri...",
                type: "csdn",
                "x-acl-token": "b4PPTlauakrI2cRr1Tg3PzfykTMK"
        },
        success: function(data){
            var text= "";
            var es = [];
            if(data.length > 0){
                text += "<span>相关主题推荐：</span>";
                for(var key in data){
                    var name = data[key]['name'];
                    es[key] = name;
                    text += "<a href='http://www.csdn.net/tag/" +  name + "'" + " target='_blank'>" + name + "</a>";
                }
            }


            //$('#suggest_tags').html(text);

            // 帖子推荐
            if(es.length > 0){
                $.ajax({
                    url: "http://internalapi.csdn.net/tag/tag/search",
                    size: 4,
                    type: "GET",
                    data: {
                        types: "topic",
                        tagNames: es.join(','),
                        size: 4,
                        "x-acl-token": "dDH/ijXIA58154g38-QLg8mnNAsK"
                    },
                    dataType: 'JSONP',
                    success: function(result){
                        var res_arr = result['result'];
                        var text = "";
                        if(res_arr.length > 0){
                            text = "<span>相关推荐：</span><ul>";
                            for(var key in res_arr){
                                var id = res_arr[key]['id'];
                                var title = res_arr[key]['title'];
                                var url = res_arr[key]['url'];
                                text += "<li><a href='" +  url + "'" + " target='_blank'>" + title + "</a></li>";
                            }
                            text += "</ul>";
                        }

                        $('#suggest_topics').html(text);
                    }
                });     
            }

        }
    });

});


</script>

    
<div id="pop_win" style="display:none ;position: absolute; z-index: 10000; border: 1px solid rgb(220, 220, 220); top: 222.5px; left: 630px; opacity: 1; background: none 0px 0px repeat scroll rgb(255, 255, 255);">
    
</div>
<div id="popup_mask"></div>
<style>
    #popup_mask
    {
        position: absolute;
        width: 100%;
        height: 100%;
        background: #000;
        z-index: 9999;
        left: 0px;
        top: 0px;
        opacity: 0.3;
        filter: alpha(opacity=30);
        display: none;
    }
 
</style>

    <script src="http://c.csdnimg.cn/www/js/component.js"></script>
    <script language="javascript" type="text/javascript" src="http://ads.csdn.net/js/async_new.js"></script>
<div id="a9784604d" style="width: 1px; height: 1px; display: none;">
	<script id="adJs9784604"></script>
	<script>document.getElementById("adJs9784604").src = "http://ads.csdn.net/js/opt/9784604.js?t=" + Math.random();</script>
</div>
<script type="text/javascript">
  document.write('<script type="text/javascript" src="http://c.csdnimg.cn/pubfooter/js/publib_footer.js?' + Math.floor(new Date()/120000).toString(36) + '="></'+'script>');
</script>
<script type="text/javascript" src="http://www.csdn.net/ui/scripts/Csdn/counter.js"></script>

<script type="text/javascript" src="http://c.csdnimg.cn/pig/pubjs/cnick.js"></script>
<script id="csdn-toolbar-id" btnId="header_notice_num" wrapId="note1" count="5" subCount="5" type="text/javascript" src="http://c.csdnimg.cn/public/common/toolbar/js/toolbar.js"></script>
  </body>
</html>


'''

Re_sub_reply=re.compile(r'<fieldset>[^|]*<\/fieldset>')
Re_sub_fenxiangdao=re.compile(r'<span id="bdshare"[^|.]*?分享到：<\/span>')


result_div=Re_sub_reply.sub('',one_div)

print result_div
# datasoup=BeautifulSoup(result_div,'lxml')
# print datasoup.select('.post_body')[0].text.strip()