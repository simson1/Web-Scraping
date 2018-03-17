import sys
import pandas as pd  
import requests
import PyQt5
from PyQt5.QtCore import QUrl
from bs4 import BeautifulSoup
import bs4 as bs
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication
import urllib.request
class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
url = 'https://www.codechef.com/rankings/SEPT17?filterBy=Institution%3DG%20H%20Patel%20College%20of%20Engineering%20and%20Technology&order=asc&sortBy=rank'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
v=[]
g=soup.find("tbody")
tr=g.find_all('div',class_='user-name')
for k in tr:
    v.append(k.text)
w=[]
g=soup.find("tbody")
tr=g.find_all('td',class_="num")
for i in tr:
    b=[i.text.strip() for i in tr]
w.extend(b)
print(w)
r=[]
for j in range(1,len(w),12):
    print(w[j])
    r.append(w[j])
q=[]
for i in range(0,len(w),12):
    q.append(w[i])

df = pd.DataFrame(v,q,r,columns=['v', 'q', 'r']) 
/*
f=[]
for i in range(len(v)):
    f.append((v[i],q[i],r[i]))
print(f) you can check the ranklist*/
df = pd.DataFrame(f,columns=['username','rank','points']) 
df.to_csv('ranklist', index=False, encoding='utf-8') 
//you can also make csv file
