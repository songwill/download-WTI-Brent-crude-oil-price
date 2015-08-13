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

def getdayprice(url):
     html=gethtml(url)
     soup=BeautifulSoup(html)
     t=soup.find_all("td",text=re.compile(r'.*?201.-..-...*?')) #‘布伦特’作为关键词不好用正则匹配，故选用日期
     l=[]
     for i in t:
         td=i.parent.find_all('td')
         tdlist=[5,1,2,3,4]
         p=[]
         for s in tdlist:
             p.append(td[s].text) 
         l.append(p)
         print p[0]
     daylist=l
     return daylist

pricelist=[]
for n in range(76):
     url='http://www.l-zzz.com/shiyou/sy_list.jsp?nID=45&pageNum=%d' %n  
     pricelist += getdayprice(url)



#print pricelist
import csv ,codecs     #不导入codecs输出的csv文件中文会显示乱码
csvfile = open('E:/mygit/dec-data/brent.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
s1=['日期','价格','比昨日','比上周','比上月']
writer.writerow(s1)
#for item in pricelist:
#    writer.writerow(item)
writer.writerows(pricelist)
csvfile.close()



