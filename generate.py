# -*- coding: UTF-8 -*-
from xml.dom.minidom import Document
import xlrd
#Pchtml = "http://sina2.com.cn"
#MobileUrl="http://html5.sina2.com.cn"
f = open("E:\output.xml", "w")
def make_mobile_xml(Pchtml,MobileUrl):
    #Pchtml = "http://sina2.com.cn"
    #MobileUrl="http://html5.sina2.com.cn"
    #Create minidom document
    doc = Document()
    #Create the <urlset> element
    #urlset = doc.createElement("urlset")
    #doc.appendChild(urlset)
    #Create the <url> element
    url = doc.createElement("url")
    doc.appendChild(url)
    #Create <loc> element
    paragraph1 = doc.createElement("loc")
    url.appendChild(paragraph1)
    locurl = doc.createTextNode(Pchtml)
    #locurl = doc.createCDATASection(Pchtml)
    paragraph1.appendChild(locurl)
    #Create data element
    data = doc.createElement("data")
    url.appendChild(data)
    #Create display element
    display = doc.createElement("display")
    data.appendChild(display)
    #Create html5_url element
    html5_url = doc.createElement("html5_url")
    display.appendChild(html5_url)
    #Create mobile url
    mobile_url = doc.createTextNode(MobileUrl)
    #mobile_url = doc.createCDATASection(MobileUrl)
    html5_url.appendChild(mobile_url)
    #print
    f.write(doc.toprettyxml(indent="  ",encoding="UTF-8"))

data = xlrd.open_workbook('E:\hotels-pc-m-details.xls')
table = data.sheets()[1]
nrows = table.nrows
table2 = data.sheets()[2]
f = open("E:\output.xml", "w")
for i in range(nrows):
    Pchtml1 = str(table.row_values(i))
    MobileUrl1 = str(table2.row_values(i))
#    Pchtml = eval(str(table.row_values(i)))
#    MobileUrl = eval(str(table2.row_values(i)))
    Pchtml = str(eval(Pchtml1[1:-1]))
    MobileUrl = str(eval(MobileUrl1[1:-1]))
    make_mobile_xml(Pchtml,MobileUrl)
print "hey man!all over"
f.close()