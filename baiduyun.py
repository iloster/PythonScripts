#-*-coding utf-8 -*-
#---------------------
#   python2.7
#   author:loster
#   version:0.1
#   description:获得百度云盘中文件的信息
#
#

import re
import urllib

#关键字
qword=raw_input('input some word:')
#返回结果的条数，好像得是10的倍数,或者小于10
rn=raw_input('input the number:')
#分析百度参数得到的
url='http://www.baidu.com/s?wd=site:pan.baidu.com+'+qword+'&rn='+rn
html=urllib.urlopen(url).read().decode('utf-8')
#正则表达式
#reg=re.compile(r'<.*?\"c-abstract\".*?m>(.*?)</em>.*?:(.*?)</')
#reg=re.compile(r'data-tools.*?\"title\":"(.*?)_.*?\"url\":"(.*?)"')
reg=re.compile(r'<.*?\"c-abstract\".*?m>(.*?)</em>.*?:(.*?)</.*?data-tools.*?\"title\":"(.*?)_.*?\"url\":"(.*?)"')
results=reg.findall(html)
#print results
i=0
print "结果个数%d" % len(results)
for i in range(len(results)):
#for result in results:
    print "----------"
    print i+1
    #文件信息
    print "info:"+results[i][1]
    #文件名字
    print "name:"+results[i][2]
    #文件网址
    print "website:"+results[i][3]

