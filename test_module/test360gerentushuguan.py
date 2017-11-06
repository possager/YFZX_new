#_*_coding:utf-8_*_

import re

test1='http://www.xjbtssbtszhdj.com/announce.frontList.in?pageNum='


def change(match):
    str_target= match.group(1)
    str_original=match.group(0)
    data=str_original.replace(str_target,'123')
    return data
print re.sub(r'http\:\/\/www\.xjbtssbtszhdj\.com\/announce\.(.*?)\.in\?pa',change,test1)