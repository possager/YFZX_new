#_*_coding:utf-8_*_
import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime,timedelta

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
user_agent2='Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

headers={
    'User-Agent':user_agent
}
# response1=requests.get(url='http://m.thepaper.cn/channel_25950',headers=headers)
# # print response1.text
# Re_pattern=re.compile(r'data.*?\:.*?\".*?Math\.random\b')
# datare=Re_pattern.findall(response1.text)
#
# url_in_content =datare[0].split('"')[1]
# nexturl='http://m.thepaper.cn/load_channel.jsp?'+url_in_content+str(1)
# print nexturl

# url1='http://m.thepaper.cn/load_channel.jsp?nodeids=nodeids=25448,26609,25942,26015,25599,25842,26862,25769,25990,26173,26202,26404,26490,&topCids=1762084,1759534&pageidx=0'
# url2='http://m.thepaper.cn/load_channel.jsp?nodeids=nodeids=25444,27224,26525,26878,25483,25457,25574,25455,26937,25450,25482,25445,25456,25446,25536,26506,&topCids=1763063&pageidx=0'
# url3='http://m.thepaper.cn/load_channel.jsp?nodeids=nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,&topCids=1762842,1762790,1763110&pageidx=0'
url4='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=26912,26918,26919,26965,26906,26907,26908,27260,26909,26910,26911,26913,26914,26915,&topCids=1763003,1763173,1762843&pageidx=18'#影视
# url5='http://m.thepaper.cn/load_channel.jsp?nodeids=nodeids=25462,25488,25489,25490,25423,25426,25424,25463,25491,25428,25464,25425,25429,25481,25430,25678,25427,25422,25487,25634,25635,25600,&topCids=1763004,1763242,1763002&pageidx=40'

# url_this='http://www.thepaper.cn/load_video_chosen.jsp?channelID=26916&pageidx=2'
# response1=requests.get(url=url_this,headers=headers)
# print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# print str(datasoup)
# print '------------------------------------------------------------------------------------------------------'
# for urlmark1 in  datasoup.select('body > div'):
#     # print urlmark1.get('href')#href
#     print urlmark1.select('h2 > a')[0].get('href')#url
#     print urlmark1.select('p')[0].text#abstract
#     print urlmark1.select('a')[2].text#publisher
#     print urlmark1.select('a')[1].text#title
#     try:
#         print urlmark1.select('a > span')[0].text#publish_time
#     except Exception as e:
#         print e
#     print urlmark1.select('span')[1].text#publish_date
#     # print urlmark1.select('div.news_li')[0].text
#     # print urlmark1.select('')
#     print urlmark1.select('h2 > a')[0].get('id')
#     # print urlmark1.select('span')[].text
#     try:
#         reply_count= urlmark1.select('span.trbszan')[0].text
#         if 'k' in reply_count:
#             reply_count = reply_count.replace('.', '').replace('k', '00')
#         print reply_count
#     except Exception as e:
#         print e
#         print 0\\


# for div_content in datasoup.select('body > div'):
#     try:
#         print 'http://m.thepaper.cn/'+div_content.select('div > a')[0].get('href')#url
#
#         publish_time= div_content.select('p > span')[0].text#publish_time
#         print div_content.select('div > p > a')[1].text#title
#         print div_content.select('div > p > a')[0].text#publish_user
#         print div_content
#         print publish_time
#         if u'分钟' in publish_time:
#             time_a=datetime.now()
#             minulate=publish_time.replace(u'分钟前','')
#             time_b=datetime.now()-timedelta(minutes=int(minulate))
#             print time_b
#             time_c=time_b.strftime('%Y-%m-%d %H:%M')
#             print time_c
#         elif u'小时前' in publish_time:
#             # time_a=datetime.now()
#             hourse=publish_time.replace(u'小时前','')
#             time_b=datetime.now()-timedelta(hours=int(hourse))
#             time_c=time_b.strftime('%Y-%m-%d %H:%M')
#             print time_c
#         elif u'天前' in publish_time:
#             days=publish_time.replace(u'天前','')
#             time_b=datetime.now()-timedelta(days=int(days))
#             time_c=time_b.strftime('%Y-%m-%d %H:%M')
#             print time_c
#
#     except Exception as e:
#         print e

# for jj in datasoup.select('li'):
#     print jj

# print str(datasoup)
# print str(datasoup)
# print datasoup.select('span.reply')[0].text

url6='http://yb.newssc.org/system/20170818/002252188.html'

one_div_wenti1='''
<div class="comment_que" id="comment12139905">
<div class="aq_write clearfix">
<div class="aqwleft">
<div class="ansleft_hdimg">
<a href="ask_user_home.jsp?userId=1093483&amp;commentId=12139905"><img src="http://image.thepaper.cn/publish/interaction/image/0/798/253.jpg"/><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"/></div></a>
</div>
</div>
<div class="aqwright">
<h3><a href="ask_user_home.jsp?userId=1093483&amp;commentId=12139905">小一</a><span>2017-08-11</span>
</h3>
<div class="ansright_cont">
<a href="javascript:replyFloor(12139905,12139905);">乱</a>
</div>
<div class="ansright_time">
<a class="ansright_zan" href="javascript:priseCommtFloor(12139905,12139905,0);" id="12139905">0</a>
<span>|</span>
<a href="javascript:replyFloor(12139905,12139905);">回复</a>
</div>
<div class="ansright_aqans" id="comm_textarea12139905" style="display:none">
<div class="point_top"></div>
<textarea class="input_aqw input_aqans" id="commText12139905" onblur="displayReplyFloor(12139905, 12139905)" onmousedown="clearReplyFloor(12139905, 12139905)" type="text"></textarea>
<div class="aqw_tip" id="icommt_commt12139905" onmouseover="disappearReplyFloor(12139905, 12139905)" style="top:7px;left:16px;">
<img alt="" src="../img/iask_tip.png"/>
<span>说你什么好呢</span>
</div>
<button class="aqw_pub" onclick="replyCommentFloor(1754327,1,false,12139905,12139905)">发表</button>
</div>
</div>
<div class="aqwright_bdbt"></div>
</div>
<div id="startId" pageindex="" startid="12062145" style="display:none;"></div>
</div>
'''
one_div_wenti2='''
<div id="commtid">
	<div class="com_write">
            <p class="com_input">
               <textarea type="text" onKeyDown="checkValue2()" onKeyUp="checkValue2()" onfocus="checkValue2();this.rows=3;" id="commText" rows="1" onclick="clearCommDft()" onmouseout="displayCommDft()" onblur="displayCommDft()" style="resize:none"></textarea>               
               <span class="tip_com" id="icommt_commt">我的评论是...(最多能输入800个汉字)</span> 
            </p>
            <p id="fabiao"><a href="javascript:pubFloorComment(1752350, 1, false);""disabled="false"><span class="bt_pub">发表</span></a></p>
        </div>

        <div class="list_com">
            <div id="aaa">
<div class="news_others_t">热评论</div>
<style>
</style>
<div class="qusans_bd bdbtline" id="floor_12051137" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">沧浪亭</span></a>
	                            <span class="time">2017-08-06</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12051137,'8')" id="12051137">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>7</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12051137')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12051137">清炒炒肉都是棒棒哒</div>
											<div class="com_writeans" id="com_write12051137" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12051137')" onKeyUp="checkValueid('12051137')" onfocus="checkValueid('12051137')" id="commText12051137" rows="4" onclick="clearCommDftid('12051137')" onmouseout="displayCommDftid('12051137')" onblur="displayCommDftid('12051137')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12051137">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12051137"><a href="javascript:replyFloorComment(1752350,1,false,12051137,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="news_others_t">新评论</div>
<div class="qusans_bd bdbtline" id="floor_12061617" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">我想说</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12061617,'1')" id="12061617">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12061617')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12061617">这么回事呀</div>
											<div class="com_writeans" id="com_write12061617" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12061617')" onKeyUp="checkValueid('12061617')" onfocus="checkValueid('12061617')" id="commText12061617" rows="4" onclick="clearCommDftid('12061617')" onmouseout="displayCommDftid('12061617')" onblur="displayCommDftid('12061617')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12061617">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12061617"><a href="javascript:replyFloorComment(1752350,1,false,12061617,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12060873" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">老人与海</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12060873,'1')" id="12060873">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12060873')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12060873">还真没吃过，不过看起来很好吃</div>
											<div class="com_writeans" id="com_write12060873" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12060873')" onKeyUp="checkValueid('12060873')" onfocus="checkValueid('12060873')" id="commText12060873" rows="4" onclick="clearCommDftid('12060873')" onmouseout="displayCommDftid('12060873')" onblur="displayCommDftid('12060873')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12060873">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12060873"><a href="javascript:replyFloorComment(1752350,1,false,12060873,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12060795" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">鸢尾丶</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12060795,'1')" id="12060795">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12060795')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12060795">一样吃</div>
											<div class="com_writeans" id="com_write12060795" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12060795')" onKeyUp="checkValueid('12060795')" onfocus="checkValueid('12060795')" id="commText12060795" rows="4" onclick="clearCommDftid('12060795')" onmouseout="displayCommDftid('12060795')" onblur="displayCommDftid('12060795')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12060795">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12060795"><a href="javascript:replyFloorComment(1752350,1,false,12060795,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12058110" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">廖瓦</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12058110,'1')" id="12058110">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12058110')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12058110">这个不知道，但是梨确实有公母之分，母梨好吃，特征是屁股大点</div>
											<div class="com_writeans" id="com_write12058110" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12058110')" onKeyUp="checkValueid('12058110')" onfocus="checkValueid('12058110')" id="commText12058110" rows="4" onclick="clearCommDftid('12058110')" onmouseout="displayCommDftid('12058110')" onblur="displayCommDftid('12058110')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12058110">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12058110"><a href="javascript:replyFloorComment(1752350,1,false,12058110,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12057112" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">CYWC☔️</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12057112,'1')" id="12057112">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12057112')">回复</span></div>
                        </div>
                        <!-- 2 === false====5-->
							<div class="comm_floor_main" id="comm_floor_12057112_1" style="">
									<div class="comm_floor_contains">
										<a><span class="floor_uername">yashmak</span>：</a>
			                            <span class="time">1楼</span>
			                            <div class="floor_hf" >
			                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12051407,'1')" id="12057112">
			                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
			                            &nbsp;<span>0</span></span>
			                            <span onclick="showcommtwrite('12057112_12051407')">回复</span>
			                            </div>
										<div class="floor_comment" id="comm_12057112_12051407">晚上刚吃了茭白炒毛豆子，白白绿绿的养眼</div>
											<div class="com_writeans" id="com_write12057112_12051407" style="display:none;">
											<p class="com_input">
											<textarea type="text" onKeyDown="checkValueid('12057112_12051407')" onKeyUp="checkValueid('12057112_12051407')" onfocus="checkValueid('12057112_12051407')" id="commText12057112_12051407" rows="4" onclick="clearCommDftid('12057112_12051407')" onmouseout="displayCommDftid('12057112_12051407')" onblur="displayCommDftid('12057112_12051407')" style="resize:none"></textarea>               
											<span class="tip_com" id="icommt_commt12057112_12051407">我的回复是...(最多能输入800个汉字)</span> 
											</p>
											<p id="fabiao12057112_12051407"><a href="javascript:replyFloorComment(1752350,1,false,12051407,1,'12057112_12051407');"><span class="bt_pubans" style="color:#FFFFFF;">发表</span></a></p>
					                     </div>
									</div>
							</div>
                        <div class="floor_bottxt" id="comm_12057112">美味啊，可以加点瘦肉肉丝…</div>
											<div class="com_writeans" id="com_write12057112" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12057112')" onKeyUp="checkValueid('12057112')" onfocus="checkValueid('12057112')" id="commText12057112" rows="4" onclick="clearCommDftid('12057112')" onmouseout="displayCommDftid('12057112')" onblur="displayCommDftid('12057112')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12057112">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12057112"><a href="javascript:replyFloorComment(1752350,1,false,12057112,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12056962" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">浮生物语</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12056962,'1')" id="12056962">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12056962')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12056962">哈哈</div>
											<div class="com_writeans" id="com_write12056962" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12056962')" onKeyUp="checkValueid('12056962')" onfocus="checkValueid('12056962')" id="commText12056962" rows="4" onclick="clearCommDftid('12056962')" onmouseout="displayCommDftid('12056962')" onblur="displayCommDftid('12056962')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12056962">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12056962"><a href="javascript:replyFloorComment(1752350,1,false,12056962,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12055427" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">仰望</span></a>
	                            <span class="time">2017-08-07</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12055427,'2')" id="12055427">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>1</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12055427')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12055427">公的是不长茭白</div>
											<div class="com_writeans" id="com_write12055427" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12055427')" onKeyUp="checkValueid('12055427')" onfocus="checkValueid('12055427')" id="commText12055427" rows="4" onclick="clearCommDftid('12055427')" onmouseout="displayCommDftid('12055427')" onblur="displayCommDftid('12055427')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12055427">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12055427"><a href="javascript:replyFloorComment(1752350,1,false,12055427,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12053409" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">小指一刀</span></a>
	                            <span class="time">2017-08-06</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12053409,'2')" id="12053409">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>1</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12053409')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12053409">饮食饮食，原本就是讲个口感，所以同一个食材也是有区别的。只是公母之分的说法不太科学，但是老百姓容易听得懂记得住，这就够了。</div>
											<div class="com_writeans" id="com_write12053409" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12053409')" onKeyUp="checkValueid('12053409')" onfocus="checkValueid('12053409')" id="commText12053409" rows="4" onclick="clearCommDftid('12053409')" onmouseout="displayCommDftid('12053409')" onblur="displayCommDftid('12053409')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12053409">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12053409"><a href="javascript:replyFloorComment(1752350,1,false,12053409,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12053144" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">大明湖畔</span></a>
	                            <span class="time">2017-08-06</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12053144,'1')" id="12053144">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12053144')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12053144">我的家乡不光有茭白，还有野生的黑茭白。</div>
											<div class="com_writeans" id="com_write12053144" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12053144')" onKeyUp="checkValueid('12053144')" onfocus="checkValueid('12053144')" id="commText12053144" rows="4" onclick="clearCommDftid('12053144')" onmouseout="displayCommDftid('12053144')" onblur="displayCommDftid('12053144')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12053144">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12053144"><a href="javascript:replyFloorComment(1752350,1,false,12053144,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd bdbtline" id="floor_12051407" style="padding:10px 0;">
						<div class="qusans_bdr floor_mopt">
                            	 <a><span class="floor_uername">yashmak</span></a>
	                            <span class="time">2017-08-06</span><div class="floor_hf">
	                            <span class="xiaoshou-d" onclick="priseFloorCommt(this,12051407,'1')" id="12051407">
	                            <img src="http://file.thepaper.cn/wap/v3/img/v3-015.png" width="14" height="14" style="margin-top:-5px;"/>
	                            &nbsp;<span>0</span></span>
	                            <span class="floor_line">|</span>
	                            <span  onclick="showcommtwrite('12051407')">回复</span></div>
                        </div>
                        <div class="floor_bottxt" id="comm_12051407">晚上刚吃了茭白炒毛豆子，白白绿绿的养眼</div>
											<div class="com_writeans" id="com_write12051407" style="display:none;">
				<p class="com_input">
				<textarea type="text" onKeyDown="checkValueid('12051407')" onKeyUp="checkValueid('12051407')" onfocus="checkValueid('12051407')" id="commText12051407" rows="4" onclick="clearCommDftid('12051407')" onmouseout="displayCommDftid('12051407')" onblur="displayCommDftid('12051407')" style="resize:none"></textarea>               
				<span class="tip_com" id="icommt_commt12051407">我的回复是...(最多能输入800个汉字)</span> 
				</p>
				<p id="fabiao12051407"><a href="javascript:replyFloorComment(1752350,1,false,12051407,1);"><span class="bt_pubans">发表</span></a></p>
                        </div>

            </div><div class="qusans_bd" id="startId1" startId="0" pageIndex="1" style="display:none;"></div>
</div>

        <p><a id="next" href="javascript:getMoreCommnet();"><span class="more_bt" id="bbb">加载更多…</span></a></p>
        </div>


</div>

<script type="text/javascript">
var g_pageidx = 1;
var maxLen = 800;
function getMoreCommnet(){
    //var startId = $("#aaa").children(".qusans_bd").last().attr("startId");
    //g_pageidx = parseInt($("#aaa").children(".qusans_bd").last().attr("pageIndex"));
    var startId = $('#startId' + g_pageidx).attr("startId");
    var joinStartId = "";
    var joinStartIdStr = "";
    if($("#joinStartId"+ g_pageidx).length>0){
		joinStartIdStr="&joinStartId="+joinStartId;
		joinStartId = $('#joinStartId' + g_pageidx).attr("startId");
    }
    g_pageidx = parseInt($('#startId' + g_pageidx).attr("pageIndex"));
    g_pageidx = g_pageidx + 1;
    if(startId == 0 && (joinStartId==""||joinStartId==0)){
        $("#bbb").html("没有更多的评论了...");
$("#next").attr("href","javascript:void(0)");
        disappearNotic();
        return;
    }
	$("#bbb").html("加载中...");
	$.ajax({
		 type : "post",
		 url: "load_newDetail_moreFCommt.jsp",
		 data:"contid=1752350&hotIds=12051137&ot=1&startId="+startId+"&pageidx="+g_pageidx+joinStartIdStr,
		 cache: false,             
		 success: function(html){   
				var data = $.trim(html); 
				if(data!= ''){
					$("#aaa").append(html);
					$("#bbb").html("加载更多...");
				} else {
					$("#bbb").html("没有更多的评论了...");
					$("#next").href="";
				}

				disappearNotic();
		 },
		 error : function(XMLHttpRequest, textStatus, errorThrown) {
			$("#bbb").html("加载更多...");
			mlAlert("系统出错");
		}
	  });

}

$(document).ready(function(){     
    $("#icommt_commt").click(function(){
          $("#icommt_commt").hide();
          $("#commText").focus(); 
    });


	$(".tip_com").each(function(){
		 $(this).mouseover(function(){
			$(this).hide();
			$(this).prev("textarea").focus();
		 });
		 $(this).click(function(){
			$(this).hide();
			$(this).prev("textarea").focus();
		 });
	});

      disappearNotic();
});



</script>

'''

one_div_wenti3='''
<div id="commtid">
	<div class="aq_write clearfix">
        <div class="aqwleft">
			<div class="ansleft_hdimg"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></div>
		</div>	
		<div class="aqwright">
			<textarea id="commText" class="input_aqw"></textarea>
			<div id="icommt_commt" class="aqw_tip"><img src="../img/iask_tip.png" alt="" /><span>我要跟帖</span></div>
			<button onclick="pubComment(1772462,1,false)" class="aqw_pub">发表</button>
		</div>

	</div>
    
    <div id="mainContent">
    	<div class="comment_title" style="margin-top:-30px;">热评论</div>
		<div class="comment_que" id="comment12406193">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=233348&commentId=12406193"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=233348&commentId=12406193">ontrain</a>
        		<span>15小时前</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12406193,12406193);">修条高铁吧，两个多小时就到了，每天来回都可以的。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12406193,12406193,19);" id="12406193" class="ansright_zan">19</a>
				<span>|</span>
				<a href="javascript:replyFloor(12406193,12406193);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12406193" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12406193" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12406193, 12406193)" onblur="displayReplyFloor(12406193, 12406193)"></textarea>
	       		<div id="icommt_commt12406193" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12406193, 12406193)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12406193,12406193)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	<div class="aqwright_bdbt"></div>
	</div>
		</div>
		<div class="comment_que" id="comment12406088">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=137406&commentId=12406088"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=137406&commentId=12406088">1614509545</a>
        		<span>15小时前</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12406088,12406088);">美国老干部局干嘛不帮忙？</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12406088,12406088,17);" id="12406088" class="ansright_zan">17</a>
				<span>|</span>
				<a href="javascript:replyFloor(12406088,12406088);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12406088" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12406088" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12406088, 12406088)" onblur="displayReplyFloor(12406088, 12406088)"></textarea>
	       		<div id="icommt_commt12406088" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12406088, 12406088)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12406088,12406088)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	<div class="aqwright_bdbt"></div>
	</div>
		</div>
		<div class="comment_que" id="comment12409069">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2821144294&commentId=12409069"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2821144294&commentId=12409069">淘折扣优惠券酱</a>
        		<span>12小时前</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12409069,12409069);">奥巴马真的是个好爸爸[good][good]</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12409069,12409069,4);" id="12409069" class="ansright_zan">4</a>
				<span>|</span>
				<a href="javascript:replyFloor(12409069,12409069);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12409069" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12409069" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12409069, 12409069)" onblur="displayReplyFloor(12409069, 12409069)"></textarea>
	       		<div id="icommt_commt12409069" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12409069, 12409069)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12409069,12409069)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	<div class="aqwright_bdbt"></div>
	</div>
		</div>
		<div class="comment_que" id="comment12407217">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2503439&commentId=12407217"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2503439&commentId=12407217"></a>
        		<span>14小时前</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12407217,12407217);">美国也有这种挤破头上名校的风气吗？</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12407217,12407217,4);" id="12407217" class="ansright_zan">4</a>
				<span>|</span>
				<a href="javascript:replyFloor(12407217,12407217);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12407217" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12407217" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12407217, 12407217)" onblur="displayReplyFloor(12407217, 12407217)"></textarea>
	       		<div id="icommt_commt12407217" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12407217, 12407217)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12407217,12407217)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	<div class="aqwright_bdbt"></div>
	</div>
		</div>
		<div class="comment_que" id="comment12411404">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=5014863112&commentId=12411404"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=5014863112&commentId=12411404">一个细心匹敌的心</a>
        		<span>11小时前</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12411404,12411404);">上大学还要家人送，这是美国吗，</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12411404,12411404,3);" id="12411404" class="ansright_zan">3</a>
				<span>|</span>
				<a href="javascript:replyFloor(12411404,12411404);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12411404" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12411404" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12411404, 12411404)" onblur="displayReplyFloor(12411404, 12411404)"></textarea>
	       		<div id="icommt_commt12411404" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12411404, 12411404)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12411404,12411404)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	</div>
		</div>
		<div class="comment_title" style="margin-top:20px;">新评论</div>
        <div class="comment_que" id="comment12414296">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1068903&commentId=12414296">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/900/412.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1068903&commentId=12414296">珑茉</a>
        		<span>1小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12414296,12414296);">等等他们是哈佛户口吗？怎么上哈佛那么容易</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12414296,12414296,1);" id="12414296" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12414296,12414296);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12414296" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12414296" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12414296, 12414296)" onblur="displayReplyFloor(12414296, 12414296)"></textarea>
	       		<div id="icommt_commt12414296" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12414296, 12414296)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12414296,12414296)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412227">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=5469135720&commentId=12412227">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=5469135720&commentId=12412227">我爸叫我小胖子</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412227,12412227);">每一个有女儿的父亲都是这样的[太开心]</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412227,12412227,1);" id="12412227" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412227,12412227);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412227" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412227" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412227, 12412227)" onblur="displayReplyFloor(12412227, 12412227)"></textarea>
	       		<div id="icommt_commt12412227" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412227, 12412227)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412227,12412227)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412226">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=6057506313&commentId=12412226">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=6057506313&commentId=12412226">惊梦_游</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412226,12412226);">回复@TBDXKA:我恨</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412226,12412226,0);" id="12412226" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412226,12412226);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412226" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412226" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412226, 12412226)" onblur="displayReplyFloor(12412226, 12412226)"></textarea>
	       		<div id="icommt_commt12412226" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412226, 12412226)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412226,12412226)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412223">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=5209247983&commentId=12412223">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=5209247983&commentId=12412223">Hiphop风格</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412223,12412223);">这个时候的奥巴马其实很帅哦！[嘻嘻]</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412223,12412223,1);" id="12412223" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412223,12412223);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412223" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412223" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412223, 12412223)" onblur="displayReplyFloor(12412223, 12412223)"></textarea>
	       		<div id="icommt_commt12412223" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412223, 12412223)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412223,12412223)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412218">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1945812997&commentId=12412218">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1945812997&commentId=12412218">Utah群星</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412218,12412218);">回复@Abby-779:虽然不少美国人租房子　但是大部分美国人工作稳定后还是买房子的。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412218,12412218,0);" id="12412218" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412218,12412218);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412218" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412218" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412218, 12412218)" onblur="displayReplyFloor(12412218, 12412218)"></textarea>
	       		<div id="icommt_commt12412218" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412218, 12412218)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412218,12412218)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412214">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1945812997&commentId=12412214">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1945812997&commentId=12412214">Utah群星</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412214,12412214);">回复@听雨煮梦:里根总统　当总统前是演员</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412214,12412214,0);" id="12412214" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412214,12412214);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412214" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412214" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412214, 12412214)" onblur="displayReplyFloor(12412214, 12412214)"></textarea>
	       		<div id="icommt_commt12412214" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412214, 12412214)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412214,12412214)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412211">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=3039803681&commentId=12412211">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=3039803681&commentId=12412211">开船儿的人</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412211,12412211);">不说别的……奥巴马的腿……[摊手][摊手][摊手][摊手][摊手]</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412211,12412211,1);" id="12412211" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412211,12412211);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412211" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412211" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412211, 12412211)" onblur="displayReplyFloor(12412211, 12412211)"></textarea>
	       		<div id="icommt_commt12412211" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412211, 12412211)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412211,12412211)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412210">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=5184901113&commentId=12412210">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=5184901113&commentId=12412210">迟迟O_o</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412210,12412210);">回复@RFeed:哈哈哈，一个表情引发的评论，绝了[允悲]</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412210,12412210,0);" id="12412210" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412210,12412210);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412210" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412210" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412210, 12412210)" onblur="displayReplyFloor(12412210, 12412210)"></textarea>
	       		<div id="icommt_commt12412210" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412210, 12412210)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412210,12412210)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412208">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=6079493494&commentId=12412208">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=6079493494&commentId=12412208">用户6079493494</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412208,12412208);">回复@XLFlag:国外大学很多办学资金来源于成功毕业生捐助，有钱人有地位的家庭肯定更容易成功。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412208,12412208,0);" id="12412208" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412208,12412208);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412208" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412208" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412208, 12412208)" onblur="displayReplyFloor(12412208, 12412208)"></textarea>
	       		<div id="icommt_commt12412208" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412208, 12412208)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412208,12412208)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12412207">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2933272802&commentId=12412207">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2933272802&commentId=12412207">佳东叫麻瓜</a>
        		<span>7小时前</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12412207,12412207);">我上大学要我爸送我去都让我自己去，羡慕那些有爸妈陪伴着的孩子</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12412207,12412207,0);" id="12412207" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12412207,12412207);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12412207" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12412207" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12412207, 12412207)" onblur="displayReplyFloor(12412207, 12412207)"></textarea>
	       		<div id="icommt_commt12412207" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12412207, 12412207)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1772462,1,false,12412207,12412207)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        </div>

    <div id="startId1" startId="12412206" pageIndex="1" style="display:none;"></div>
    <div id="addButton" class="add_more" style="display:block;"> <a id="next_comment" href="load_newDetail_moreCommt.jsp"></a></div>
</div>

<script type="text/javascript">
var g_pageidx = 1;
$(document).ready(function(){
    $('#mainContent').infinitescroll({
        navSelector  	: "#next_comment:last",
        nextSelector 	: "a#next_comment:last",
        itemSelector 	: ".comment_que",
        debug		: true,
        dataType	: 'html',
        loading: {
            msgText:'',
            img: "../img/loading.gif",
            selector: '#addButton'
        },
        pathParse: function(path,pageidx){   
            return function(pageidx){
                var startId = $('#startId' + g_pageidx).attr("startId");
                g_pageidx = parseInt($('#startId' + g_pageidx).attr("pageIndex"));
                var joinStartIdStr = "";
                if($("#joinStartId"+ g_pageidx).length>0){
                	joinStartIdStr="&joinStartId="+$('#joinStartId' + g_pageidx).attr("startId");
                }
                g_pageidx = g_pageidx + 1;
                return "load_moreFloorComment.jsp?contid=1772462&hotIds=12406193,12406088,12409069,12407217,12411404&pageidx="+g_pageidx+"&startId="+startId+joinStartIdStr;
            }
        }
    });

    $("#icommt_commt").mouseover(function(){
  		$("#icommt_commt").hide();
  		$("#commText").focus();
    });
    
    $("#commText").mousedown(function(){
		  $("#icommt_commt").hide();
    });
    
    $("#commText").blur(function(){
  		if ($("#commText").val() == ""){
  			$("#icommt_commt").show();
  		}   
    });
	
    // update num of comments
    var commPreHtml	= "评论<span>（";
    var commSurHtml	= "）</span>";
    $(".video_news_tit3 #comm_span").html(commPreHtml + "2k" + commSurHtml);
});

function expandcomment(commtId) {
	$("#comment"+ commtId + " #slideDown_Commt .ansright_contans").slideDown()
	$("#comment"+ commtId + " .expand_commt").hide();
}
</script>
'''

one_div_wenti2_diannao='''
<div id="commtid">
	<div class="aq_write clearfix">
        <div class="aqwleft">
			<div class="ansleft_hdimg"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></div>
		</div>	
		<div class="aqwright">
			<textarea id="commText" class="input_aqw"></textarea>
			<div id="icommt_commt" class="aqw_tip"><img src="../img/iask_tip.png" alt="" /><span>我要跟帖</span></div>
			<button onclick="pubComment(1752350,1,false)" class="aqw_pub">发表</button>
		</div>

	</div>
    
    <div id="mainContent">
    	<div class="comment_title" style="margin-top:-30px;">热评论</div>
		<div class="comment_que" id="comment12051137">
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1701609&commentId=12051137"><img src="http://image.thepaper.cn/publish/interaction/image/1/290/466.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1701609&commentId=12051137">沧浪亭</a>
        		<span>2017-08-06</span>
                </h3>
        	
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12051137,12051137);">清炒炒肉都是棒棒哒</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12051137,12051137,7);" id="12051137" class="ansright_zan">7</a>
				<span>|</span>
				<a href="javascript:replyFloor(12051137,12051137);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12051137" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12051137" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12051137, 12051137)" onblur="displayReplyFloor(12051137, 12051137)"></textarea>
	       		<div id="icommt_commt12051137" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12051137, 12051137)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12051137,12051137)" class="aqw_pub">发表</button>
	       	</div>
        	
        </div>
	</div>
		</div>
		<div class="comment_title" style="margin-top:20px;">新评论</div>
        <div class="comment_que" id="comment12061617">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2170805&commentId=12061617">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/942/956.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2170805&commentId=12061617">我想说</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12061617,12061617);">这么回事呀</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12061617,12061617,0);" id="12061617" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12061617,12061617);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12061617" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12061617" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12061617, 12061617)" onblur="displayReplyFloor(12061617, 12061617)"></textarea>
	       		<div id="icommt_commt12061617" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12061617, 12061617)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12061617,12061617)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12060873">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2156260&commentId=12060873">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/942/942.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2156260&commentId=12060873">老人与海</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12060873,12060873);">还真没吃过，不过看起来很好吃</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12060873,12060873,0);" id="12060873" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12060873,12060873);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12060873" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12060873" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12060873, 12060873)" onblur="displayReplyFloor(12060873, 12060873)"></textarea>
	       		<div id="icommt_commt12060873" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12060873, 12060873)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12060873,12060873)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12060795">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2175028&commentId=12060795">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/671/704.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2175028&commentId=12060795">鸢尾丶</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12060795,12060795);">一样吃</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12060795,12060795,0);" id="12060795" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12060795,12060795);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12060795" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12060795" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12060795, 12060795)" onblur="displayReplyFloor(12060795, 12060795)"></textarea>
	       		<div id="icommt_commt12060795" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12060795, 12060795)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12060795,12060795)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12058110">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1900648&commentId=12058110">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/444/128.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1900648&commentId=12058110">廖瓦</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12058110,12058110);">这个不知道，但是梨确实有公母之分，母梨好吃，特征是屁股大点</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12058110,12058110,0);" id="12058110" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12058110,12058110);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12058110" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12058110" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12058110, 12058110)" onblur="displayReplyFloor(12058110, 12058110)"></textarea>
	       		<div id="icommt_commt12058110" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12058110, 12058110)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12058110,12058110)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12057112">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=1169753&commentId=12057112">
	                <img src="http://image.thepaper.cn/publish/interaction/image/0/859/240.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=1169753&commentId=12057112">CYWC☔️</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="floor_content">
        			<div class="ansright_contans">
			                <div class="fansright_time">
									<a href="javascript:priseCommtFloor('12057112','12051407', 0)" id="12051407" class="fansright_zan">0</a>
									<span>|</span>
									<a href="javascript:replyFloor(12057112, 12051407);">回复</a>
								</div>
			        			<h3>
			        				<a href="ask_user_home.jsp?userId=585256&commentId=12051407">
			        					yashmak</a>
			        				<span>1楼</span>
			        			</h3>
			        			<div class="gl_cont">晚上刚吃了茭白炒毛豆子，白白绿绿的养眼</div>
			        			<div class="ansright_aqans" id="comm_textarea12051407" style="display:none">
					        		<div class="point_top"></div>
					        		<textarea type="text" id="commText12051407" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12057112, 12051407)" onblur="displayReplyFloor(12057112, 12051407)"></textarea>
					        		<div id="icommt_commt12051407" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12057112, 12051407)">
						        		<img src="../img/iask_tip.png" alt="" />
						        		<span>说你什么好呢</span>
					        		</div>
					        		<button onclick="replyCommentFloor(1752350,1,false,12057112,12051407)" class="aqw_pub">发表</button>
       							</div>
			        		</div>
			                </div>
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12057112,12057112);">美味啊，可以加点瘦肉肉丝…</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12057112,12057112,0);" id="12057112" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12057112,12057112);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12057112" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12057112" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12057112, 12057112)" onblur="displayReplyFloor(12057112, 12057112)"></textarea>
	       		<div id="icommt_commt12057112" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12057112, 12057112)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12057112,12057112)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12056962">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2169853&commentId=12056962">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/942/925.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2169853&commentId=12056962">浮生物语</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12056962,12056962);">哈哈</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12056962,12056962,0);" id="12056962" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12056962,12056962);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12056962" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12056962" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12056962, 12056962)" onblur="displayReplyFloor(12056962, 12056962)"></textarea>
	       		<div id="icommt_commt12056962" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12056962, 12056962)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12056962,12056962)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12055427">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2258867&commentId=12055427">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/745/469.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2258867&commentId=12055427">仰望</a>
        		<span>2017-08-07</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12055427,12055427);">公的是不长茭白</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12055427,12055427,1);" id="12055427" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12055427,12055427);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12055427" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12055427" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12055427, 12055427)" onblur="displayReplyFloor(12055427, 12055427)"></textarea>
	       		<div id="icommt_commt12055427" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12055427, 12055427)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12055427,12055427)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12053409">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2499001&commentId=12053409">
	                <img src="http://image.thepaper.cn/publish/interaction/image/1/956/639.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=2499001&commentId=12053409">小指一刀</a>
        		<span>2017-08-06</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12053409,12053409);">饮食饮食，原本就是讲个口感，所以同一个食材也是有区别的。只是公母之分的说法不太科学，但是老百姓容易听得懂记得住，这就够了。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12053409,12053409,1);" id="12053409" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12053409,12053409);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12053409" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12053409" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12053409, 12053409)" onblur="displayReplyFloor(12053409, 12053409)"></textarea>
	       		<div id="icommt_commt12053409" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12053409, 12053409)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12053409,12053409)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12053144">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=698386&commentId=12053144">
	                <img src="http://image.thepaper.cn/publish/interaction/image/0/473/298.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=698386&commentId=12053144">大明湖畔</a>
        		<span>2017-08-06</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12053144,12053144);">我的家乡不光有茭白，还有野生的黑茭白。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12053144,12053144,0);" id="12053144" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12053144,12053144);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12053144" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12053144" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12053144, 12053144)" onblur="displayReplyFloor(12053144, 12053144)"></textarea>
	       		<div id="icommt_commt12053144" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12053144, 12053144)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12053144,12053144)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        <div class="comment_que" id="comment12051407">
        
        <div class="aq_write clearfix">
            <div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=585256&commentId=12051407">
	                <img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div>
	                </a>
            </div>
        </div>
        <div class="aqwright">
        	<h3>
        		<a href="ask_user_home.jsp?userId=585256&commentId=12051407">yashmak</a>
        		<span>2017-08-06</span>
                </h3>
            
            <div class="ansright_cont">
	       		<a href="javascript:replyFloor(12051407,12051407);">晚上刚吃了茭白炒毛豆子，白白绿绿的养眼</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12051407,12051407,0);" id="12051407" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12051407,12051407);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12051407" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12051407" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12051407, 12051407)" onblur="displayReplyFloor(12051407, 12051407)"></textarea>
	       		<div id="icommt_commt12051407" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12051407, 12051407)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1752350,1,false,12051407,12051407)" class="aqw_pub">发表</button>
	       	</div>
        </div>
        <div class="aqwright_bdbt"></div>
	    </div>
		</div>
        </div>

    <div id="startId1" startId="12051137" pageIndex="1" style="display:none;"></div>
    <div id="addButton" class="add_more" style="display:block;"> <a id="next_comment" href="load_newDetail_moreCommt.jsp"></a></div>
</div>

<script type="text/javascript">
var g_pageidx = 1;
$(document).ready(function(){
    $('#mainContent').infinitescroll({
        navSelector  	: "#next_comment:last",
        nextSelector 	: "a#next_comment:last",
        itemSelector 	: ".comment_que",
        debug		: true,
        dataType	: 'html',
        loading: {
            msgText:'',
            img: "../img/loading.gif",
            selector: '#addButton'
        },
        pathParse: function(path,pageidx){   
            return function(pageidx){
                var startId = $('#startId' + g_pageidx).attr("startId");
                g_pageidx = parseInt($('#startId' + g_pageidx).attr("pageIndex"));
                var joinStartIdStr = "";
                if($("#joinStartId"+ g_pageidx).length>0){
                	joinStartIdStr="&joinStartId="+$('#joinStartId' + g_pageidx).attr("startId");
                }
                g_pageidx = g_pageidx + 1;
                return "load_moreFloorComment.jsp?contid=1752350&hotIds=12051137&pageidx="+g_pageidx+"&startId="+startId+joinStartIdStr;
            }
        }
    });

    $("#icommt_commt").mouseover(function(){
  		$("#icommt_commt").hide();
  		$("#commText").focus();
    });
    
    $("#commText").mousedown(function(){
		  $("#icommt_commt").hide();
    });
    
    $("#commText").blur(function(){
  		if ($("#commText").val() == ""){
  			$("#icommt_commt").show();
  		}   
    });
	
    // update num of comments
    var commPreHtml	= "评论<span>（";
    var commSurHtml	= "）</span>";
    $(".video_news_tit3 #comm_span").html(commPreHtml + "37" + commSurHtml);
});

function expandcomment(commtId) {
	$("#comment"+ commtId + " #slideDown_Commt .ansright_contans").slideDown()
	$("#comment"+ commtId + " .expand_commt").hide();
}
</script>

'''

one_div_wenti4='''
<div class="comment_que" id="comment12400982">
    <div class="aq_write clearfix">
    	<div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=957508&commentId=12400982"><img src="http://image.thepaper.cn/publish/interaction/image/0/686/267.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        
        <div class="aqwright">
        	<h3><a href="ask_user_home.jsp?userId=957508&commentId=12400982">dracula</a><span>23小时前</span>
                </h3>
            
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12400982,12400982);">笑死了</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12400982,12400982,8);" id="12400982" class="ansright_zan">8</a>
				<span>|</span>
				<a href="javascript:replyFloor(12400982,12400982);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12400982" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12400982" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12400982, 12400982)" onblur="displayReplyFloor(12400982, 12400982)"></textarea>
	       		<div id="icommt_commt12400982" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12400982, 12400982)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1770956,1,false,12400982,12400982)" class="aqw_pub">发表</button>
	       	</div>
        
        </div>
        <div class="aqwright_bdbt"></div>
    </div>

<div id="startId" startId="0" pageIndex="" style="display:none;"></div>
    </div>

<div class="comment_que" id="comment12400898">
    <div class="aq_write clearfix">
    	<div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2376439&commentId=12400898"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        
        <div class="aqwright">
        	<h3><a href="ask_user_home.jsp?userId=2376439&commentId=12400898"></a><span>23小时前</span>
                </h3>
            
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12400898,12400898);">小编，这个系统的字形日ri、曰jyue无法区分，里面的“曰”字字形不对，应当再宽一点。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12400898,12400898,2);" id="12400898" class="ansright_zan">2</a>
				<span>|</span>
				<a href="javascript:replyFloor(12400898,12400898);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12400898" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12400898" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12400898, 12400898)" onblur="displayReplyFloor(12400898, 12400898)"></textarea>
	       		<div id="icommt_commt12400898" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12400898, 12400898)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1770956,1,false,12400898,12400898)" class="aqw_pub">发表</button>
	       	</div>
        
        </div>
        <div class="aqwright_bdbt"></div>
    </div>

</div>

<div class="comment_que" id="comment12399687">
    <div class="aq_write clearfix">
    	<div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2384670&commentId=12399687"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        
        <div class="aqwright">
        	<h3><a href="ask_user_home.jsp?userId=2384670&commentId=12399687">stzar</a><span>1天前</span>
                </h3>
            
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12399687,12399687);">“词旨雅驯”兼有王义庆《世说新语》之长。”？？别逗我啊老哥，作者刘义庆啊。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12399687,12399687,1);" id="12399687" class="ansright_zan">1</a>
				<span>|</span>
				<a href="javascript:replyFloor(12399687,12399687);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12399687" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12399687" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12399687, 12399687)" onblur="displayReplyFloor(12399687, 12399687)"></textarea>
	       		<div id="icommt_commt12399687" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12399687, 12399687)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1770956,1,false,12399687,12399687)" class="aqw_pub">发表</button>
	       	</div>
        
        </div>
        <div class="aqwright_bdbt"></div>
    </div>

</div>

<div class="comment_que" id="comment12399603">
    <div class="aq_write clearfix">
    	<div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=2100301&commentId=12399603"><img src="http://image.thepaper.cn/html/image/def_head.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        
        <div class="aqwright">
        	<h3><a href="ask_user_home.jsp?userId=2100301&commentId=12399603">贵涛哥哥</a><span>1天前</span>
                </h3>
            
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12399603,12399603);">到底想要表达什么？原谅我学识太浅。</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12399603,12399603,0);" id="12399603" class="ansright_zan">0</a>
				<span>|</span>
				<a href="javascript:replyFloor(12399603,12399603);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12399603" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12399603" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12399603, 12399603)" onblur="displayReplyFloor(12399603, 12399603)"></textarea>
	       		<div id="icommt_commt12399603" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12399603, 12399603)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1770956,1,false,12399603,12399603)" class="aqw_pub">发表</button>
	       	</div>
        
        </div>
        <div class="aqwright_bdbt"></div>
    </div>

</div>

<div class="comment_que" id="comment12398684">
    <div class="aq_write clearfix">
    	<div class="aqwleft">
            <div class="ansleft_hdimg">
                <a href="ask_user_home.jsp?userId=625608&commentId=12398684"><img src="http://image.thepaper.cn/publish/interaction/image/0/415/60.jpg"><div class="hdimg_bg"><img src="../img/headerimg_bg50.png"></div></a>
            </div>
        </div>
        
        <div class="aqwright">
        	<h3><a href="ask_user_home.jsp?userId=625608&commentId=12398684">愤怒的小王八</a><span>1天前</span>
                </h3>
            
        	<div class="ansright_cont">
	       		<a href="javascript:replyFloor(12398684,12398684);">腊...腊鸡...</a>
	       	</div>
        	
			<div class="ansright_time">
				<a href="javascript:priseCommtFloor(12398684,12398684,25);" id="12398684" class="ansright_zan">25</a>
				<span>|</span>
				<a href="javascript:replyFloor(12398684,12398684);">回复</a>
			</div>
		
	       	<div class="ansright_aqans" id="comm_textarea12398684" style="display:none">
	       		<div class="point_top"></div>
	       		<textarea type="text" id="commText12398684" class="input_aqw input_aqans" onmousedown="clearReplyFloor(12398684, 12398684)" onblur="displayReplyFloor(12398684, 12398684)"></textarea>
	       		<div id="icommt_commt12398684" class="aqw_tip" style="top:7px;left:16px;" onmouseover="disappearReplyFloor(12398684, 12398684)">
	       			<img src="../img/iask_tip.png" alt="" />
	       			<span>说你什么好呢</span>
	       		</div>
	       		<button onclick="replyCommentFloor(1770956,1,false,12398684,12398684)" class="aqw_pub">发表</button>
	       	</div>
        
        </div>
        <div class="aqwright_bdbt"></div>
    </div>

</div>


'''


datasoup=BeautifulSoup(one_div_wenti4,'lxml')
# print str(datasoup.select('div.aqwright > h3 > a')[0]).split('commentId=')[1].split('"')[0]
# print datasoup.select('div.aqwright > div.floor_content > div > h3 > span')
# for jj in datasoup.select('div.aqwright > div > div '):
#     print jj
#     print '\n'

# for iii in datasoup.select('div '):
#     print iii
#     print '\n'

# for iii in datasoup.select('div.aqwright'):
#     # print iii.select('div > a')
#     # print '\n\n'
#
#     if iii.select('div > a[href^="javascript:replyFloor"]'):
#         print iii.select('div > a[href^="javascript:replyFloor"]')[0].text


# for i in  datasoup.select('div.aqwright > div.ansright_time > a[href^="javascript:priseCommtFloor"]'):
#     print i.text


# for i in datasoup.select('div.comment_que'):
#     print i.select('div.aqwleft > div > a > img')[0]
#     print '\n\n\n'

url5='http://www.thepaper.cn/newsDetail_forward_1779653'

response1=requests.get(url6)
datasoup2=BeautifulSoup(response1.text,'lxml')
# print datasoup2.select('video source')[0].get('src')
# print response1.text.decode()

print '这是分隔符----------------------------'
for i in datasoup2.select('p'):
    print i.text