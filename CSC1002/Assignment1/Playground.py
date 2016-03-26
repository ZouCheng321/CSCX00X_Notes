# -*-coding:utf-8-*-
import urllib

import cookielib
import urllib2

account=raw_input('account:')#输入知乎的用户名
password=raw_input('password:')#输入密码
filename = 'cookie.txt'  #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)  #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'account':account,
    'password':password
})
loginUrl = 'http://www.zhihu.com'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)#保存cookie到cookie.txt
Url = 'http://www.zhihu.com/people/bboczeng/followers'#利用cookie请求访问另一个网址
result = opener.open(Url)#请求访问该url
print result.read()