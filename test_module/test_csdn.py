#_*_coding:utf-8_*_
import requests
import re


from bs4 import BeautifulSoup

one_div='''

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

'''

Re_sub_reply=re.compile(r'<fieldset>[^|.]*<\/fieldset>')
Re_sub_fenxiangdao=re.compile(r'<span id="bdshare"[^|.]*?分享到：<\/span>')


result_div=Re_sub_fenxiangdao.sub('',one_div)

print result_div
datasoup=BeautifulSoup(result_div,'lxml')
print datasoup.select('.post_body')[0].text.strip()