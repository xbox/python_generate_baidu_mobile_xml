'''
Created on 2012-11-23

@author: Administrator
'''
from xml.dom.minidom import Document
import xlrd
doc = Document()
url = doc.createElement("url")
doc.appendChild(url)
loc = doc.createCDATASection("http://baidu.com")
url.appendChild(loc)

print doc.toprettyxml(indent=" ")