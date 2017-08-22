#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
import requests
import re



headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

# response1=requests.request(method='get',url='http://www.thepaper.cn/newsDetail_forward_1769701')
#
#
# datasoup=BeautifulSoup(response1.text,'lxml')
# print datasoup.select('body > div.video_main.pad60.nav_container > div.video_bo > div > div.video_txt_l > div > div.video_info > span.reply')
# print datasoup.select('')


datatext='''
<div class="neirong">
<h2>这个五一小长假 唱游古镇黄龙溪</h2>
<p class="jieshao">
<span>编辑：许雯</span><span>责任编辑：马兰</span><span>
        来源：
                        							<a href="http://cd.newssc.org/system/20150504/001635880.htm" target="_blank" title="这个五一小长假 唱游古镇黄龙溪">四川新闻网</a>
</span><br/><span>2015-06-11 18:17</span></p>
<!-- 编辑自定义内容 -->
<article>
<p><img alt="" border="0" src="http://upload.chengdu.cn/2015/0612/1434097679943.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p style="text-align: center;"><span style="color: #008000; font-size: 12px;">人气依然高居不下</span></p>
<p>今年的五一小长假，对于四川景区来说，几乎都是人气爆棚，络绎不绝的省内外游客涌向省内各大景区。连续两年五一小长假人气居冠的黄龙溪古镇，人气依然高居不下，三天接待游客三十余万人次。看来是，越来越多的游客，开始爱上这种既可以选择一日往返，也可以在古镇上小住一、两天，感受古镇的悠闲生活的感觉。</p>
<p>没有去黄龙溪的小伙伴，这就随记者一起去看看，今年五一小长假的黄龙溪古镇都有些什么精彩节目吧！</p>
<p><strong>唱游互动很受欢迎</strong></p>
<p>史上最任性女教师世界之旅第一步定位黄龙溪，五一小长假，跟上她的脚步，唱民谣、烧火龙、玩游戏，让我们出发吧！五一期间，黄龙溪古镇推出“世界那么大 唱游黄龙溪”主题旅游活动，将以龙歌、龙舞、龙游戏等丰富多彩的民俗、游戏、娱乐活动，带领游客过一个独具黄龙溪特色的劳动节。</p>
<p><strong>古老与时尚和谐共现</strong></p>
<p>景区在演艺中心和凤岛广场设点，为广大游客精心准备了变脸、茶艺、武术、舞龙等传统民俗巡演以及参与性的“寻龙”互动游戏。更有成都本土摇滚乐队空降黄龙溪现场演出，相信每位游客都能找到自己的乐趣。</p>
<p><img alt="" border="0" src="http://upload.chengdu.cn/2015/0612/1434097679484.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p style="text-align: left;"><span style="color: #000000;"><strong><span style="font-size: 12px;">民俗的 世界的</span></strong></span></p>
<p>火随龙起，龙随火跃，精彩绝伦的“烧火龙”总是能给游客留下深刻的黄龙溪记忆。2015年5月1日及5月2日，曾赴澳洲、韩国、台湾等国家和地区演出的国家级非物质文化遗产“黄龙溪烧火龙”将在古镇民俗演艺中心内与游客共舞狂欢。夜晚掌灯时分，龙腾翻跃，人声鼎沸，欣赏完将黄龙溪的水文化、酒文化、茶文化、码头文化等融为一体的《水龙吟》表演后，游客可以到演艺中心内与火龙队员一同欢快地烧起火龙，共同祈福万事如意。</p>
<p><img alt="" border="0" src="http://upload.chengdu.cn/2015/0612/1434097679784.jpg" style="display: block; margin-left: auto; margin-right: auto;"/></p>
<p><strong>惊喜连连助商家 游客消费真实惠</strong></p>
<p>五一期间，为感谢广大游客朋友们的厚爱，景区内各大主要商家都推出了自己的优惠酬宾活动。黄龙丽景酒店的“谁是猜歌王”、欣瑞大酒店的“清爽过五一畅游黄龙溪”、千年一瞬酒吧的“午后民谣”等活动个个精彩，参与活动更可享受超值礼品，吃住游购爽翻天！</p> <!-- -->
</article>
</div>
'''

Re_find_img_url = re.compile(r'src=".*?"')
Re_find_test=re.compile(r'src')
img_find_by_re = Re_find_img_url.findall(datatext)
print img_find_by_re