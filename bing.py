#-*-coding:utf-8 -*-
#-----------------------------
#   python2.7
#   author:loster
#   version:0.1
#   description:下载bing壁纸到本地
#-------------------------------
import urllib
import re
import time
def getHtml(url):
    return urllib.urlopen(url).read()

def getImgUrl(html):
    reg=re.compile(r'(http://s.cn.bing.net/.*?\.jpg)')
    url=reg.findall(html)
    print url[0]
    return url[0]

def downloadImg(url,path):
    xpath=path+'\\bing.jpg'
    print xpath
    urllib.urlretrieve(url,xpath)
    
if __name__=='__main__':
    start=time.time()
    html=getHtml('http://cn.bing.com/')
    url=getImgUrl(html)
    downloadImg(url,'F:\\python')
    end=time.time()
    print 'done %.2f seconds' % (end-start)
