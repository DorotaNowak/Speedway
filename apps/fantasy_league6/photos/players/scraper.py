from bs4 import BeautifulSoup
import requests
import urllib.request
list_of_teams=[
   'wlokniarz-czestochowa/',
   'stal-gorzow/',
   'gkm-grudziadz/',
   'fogo-unia-leszno/',
   'motor-lublin/',
   'ks-torun/',
   'sparta-wroclaw/',
   'falubaz-zielona-gora/'
]
for team in list_of_teams:
   htmlSource=requests.get('https://speedwayekstraliga.pl/druzyny/'+team).text
   soup=BeautifulSoup(htmlSource)
   players=soup.find_all("div", {"class": "page-team__rider"})
   name='p'
   import os
   for p in players:
      name=p.find("div", {"class": "page-team__rider__name"}).text.replace(" ", "").splitlines()
      surname=p.find("div", {"class": "page-team__rider__surname"}).text.replace(" ", "").splitlines()
      link_to_img=p.find("div", {"class": "page-team__rider__avatar"}).find("div", {"class": "media-loader"}).find("img")['data-src']
      urllib.request.urlretrieve(link_to_img, name[1]+'_'+surname[1]+'.jpg')
