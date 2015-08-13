#Author:songwill
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
from bs4 import BeautifulSoup


#获取html文档
def gethtml(url):
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    html=response.read()
    return html

url='http://www.l-zzz.com/shiyou/sy_list.jsp?nID=45&pageNum=1'
html=gethtml(url)
soup=BeautifulSoup(html)
t=soup.find_all("td",text=re.compile(r'.*?201.-..-...*?'))
l=[]
for i in t:
    td=i.parent.find_all('td')
    tdlist=[5,1,2,3,4]
    p=[]
    for s in tdlist:
        p.append(td[s].text) 
    l.append(p)
print l


#m= re.search(ur"[\u4e00-\u9fa5]+",a.decode('utf8'))
