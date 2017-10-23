from bs4 import BeautifulSoup
import datetime
from urllib.request import urlopen


url = 'http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04'
with urlopen(url) as resp:
    html = resp.read()

soup = BeautifulSoup(html, 'html.parser')
table_tag = soup.find('table', {'class': 'tbl_type3 tbl_calendar'})
listed_text = []

for td_tag in table_tag.find_all('td'):
    div_tag = td_tag.find('div')
    text = div_tag.text
    if text.strip():
        listed_text.append(text)

now = datetime.datetime.now()
nowdate = now.strftime('%d')
nowtime = int(now.strftime('%H'))

today_meal = ""
lunch = ""
dinner = ""

if nowdate[0] == 0 :
    today_meal = listed_text[int(nowdate[1])-1]
else :
    today_meal = listed_text[int(nowdate)-1]

if today_meal in "[중식]" :
    lunch = today_meal[today_meal.index("[중식]"):today_meal.index("[석식]")]
    dinner = today_meal[today_meal.index("[석식]"):]

else:
    lunch = "정보없음"
    dinner = "정보없음"

print(lunch)
print(dinner)
