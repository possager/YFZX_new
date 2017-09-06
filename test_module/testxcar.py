#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re
from lxml import html


response1=requests.get(url='http://bbs.csdn.net/topics/320264923')

# print response1.text
# Re_replace_js=re.compile(r'<script.*?>.*?</script>')


def handleContent(content): #去除文章中的html标签以及空格字符
   # html_re = re.compile(r"<.+?>",re.S)
   # content = html_re.sub("",content)
   # space_re = re.compile(r"\s+?",re.S)
   # content = space_re.sub("",content)
   script_re =re.compile(r'<script.*?>\s*[^|]*?<\/script>',re.S)
   content = script_re.sub("",content)
   style_re = re.compile(r'<style.*?>\s*[^|]*?<\/style>',re.S)
   content = style_re.sub("",content)
   # content=Re_replace_js.sub('',content)
   return content.strip()

response_text=handleContent(response1.text)
datasoup=BeautifulSoup(response_text,'lxml')
for i in datasoup.select('div.detailed table.post .post_body'):
    print i.text.strip()
    # content1=handleContent(i.text)
    print '----------------------------------------------------------------------------------------------------------'


thathdiv='''

<div class="post_body">
<div class="tag">
</div>
                  如题：我想购买一套带vxworks的ARM11开发板，请问各位有什么推荐啊？



              <div id="topic-extra-info">
<div class="social-share">
<!-- Baidu Button BEGIN -->
<span class="bdshare_t bds_tools get-codes-bdshare" id="bdshare">
<a class="bds_tsina"></a>
<a class="bds_tqq"></a>
<span class="bds_more">更多</span>
<a class="shareCount"></a>
</span>
<span class="prompt">分享到：</span>
<script data="type=tools&amp;uid=3329407" id="bdshare_js" type="text/javascript"></script>
<script id="bdshell_js" type="text/javascript"></script>
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
<script src="//pagead2.googlesyndication.com/pagead/show_ads.js" type="text/javascript"></script>
<!-- 广告位结束 -->
</div>
<!-- 主帖下Banner (D4) -->
<!-- 主帖下文字 (D5) -->
<div marginheight="0" marginwidth="0" scrolling="no" width="100%">
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
<div id="bd_ad_2" style="margin:0; padding-bottom:5px; display:block; text-align: center">
<script type="text/javascript"><!--
  google_ad_client = "ca-pub-8990951720398508";
  /* 论坛帖子页下方banner2-728*90 */
  google_ad_slot = "8267689356/8197924482";
  google_ad_width = 728;
  google_ad_height = 90;
  //-->
  </script>
<script src="//pagead2.googlesyndication.com/pagead/show_ads.js" type="text/javascript">
</script>
</div>
<div class="adtxt">
<ul>
<li style="margin-top:0px;vertical-align:top;margin-right:35px;max-width:230px;max-height:20px;overflow:hidden;">
<ins data-revive-id="8c38e720de1c90a6f6ff52f3f89c4d57" data-revive-zoneid="59"></ins>
</li>
<li style="margin-right:35px;">
<script type="text/javascript">
        /*论坛帖子页下方文字链2 创建于 2014-07-03*/
        var cpro_id = "u1636201";
      </script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</li>
<li>
<script type="text/javascript">
        /*论坛帖子页下方文字链3创建于 2014-07-03*/
        var cpro_id = "u1636204";
      </script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>
</li>
</ul>
</div>
</div>
</div>

# '''

# for i in Re_replace_js.findall(thathdiv):
#     print i

# print handleContent(thathdiv)