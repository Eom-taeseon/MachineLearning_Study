from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.weather.go.kr/weather/forecast/mid-term_01.jsp"

#urlopen()으로 데이터 가져옥
res = req.urlopen(url)

#BeautifulSoup으로 분석하기
soup = BeautifulSoup(res, "html.parser")

#원하는 데이터 추출하기
title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)
