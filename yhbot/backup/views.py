from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from yhbot.models import Meal
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json, datetime


# Create your views here.

def keyboard(request):
    
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['중식', '석식']

    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    meal_name = received_json_data["content"]
    today_date = datetime.date.today().strftime("%m월 %d일")
    
    return JsonResponse({
            'message': {
                'text': today_date + "의 " + meal_name + "\n" + get_menu(meal_name)
            },

            'keyboard': {
                'type': 'buttons',
                'buttons': ['중식', '석식']
            }

        })


def parser(request): 

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

    Menu(meal = '중식', menu = lunch).save()


def get_menu(meal_name):
    
    if meal_name == '중식' : 
        lunch_menu = Meal.objects.get(meal = '중식').menu
        
        return lunch_menu

    elif meal_name == '석식' :
        dinner_menu = Meal.objects.get(meal = '석식').menu

        return dinner_menu
