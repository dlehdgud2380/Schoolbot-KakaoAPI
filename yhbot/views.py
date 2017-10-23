from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from yhbot.models import School_Info
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json, datetime
import re



def keyboard(request):#자동응답 버튼입니다
    
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['급식정보', '가정통신문 보기', '학사일정', '공지사항']

    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    selected_keyboard = received_json_data["content"]
    today_date = datetime.date.today().strftime("%m월 %d일")
    month_date = datetime.date.today().strftime("%m월")
    
#급식정보 파트(중식, 석식 파트 불러옵니다.)
    if "급식정보" in selected_keyboard:

       return JsonResponse({
               'message': {
                   'text': today_date + "의 " + selected_keyboard + "\n" + meal_parser()
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })
#가정통신문 파트(최대 6개까지 불러올 수 있습니다.)
    elif "가정통신문 보기" in selected_keyboard: 

        return JsonResponse({
               'message': {
                   'text': "가정통신문 메뉴를 고르세요\n최상위의 가정통신문이 최신의 가정통신문입니다."
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': [str(schoolinfo_titleloader(1)), str(schoolinfo_titleloader(2)), str(schoolinfo_titleloader(3)), str(schoolinfo_titleloader(4)), str(schoolinfo_titleloader(5)), str(schoolinfo_titleloader(6))]
            }

        })

    elif str(schoolinfo_titleloader(1)) in selected_keyboard:
        
        return JsonResponse({ #sql_lite에 저장된 가정통신문 게시글을 가져와 불러옵니다. 
               'message': {
                   'text': schoolinfo_loader(1),
                   'photo': {
                       'url': schoolinfo_imgloader(1),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(1)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif str(schoolinfo_titleloader(2)) in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': schoolinfo_loader(2),
                   'photo': {
                       'url': schoolinfo_imgloader(2),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(2)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif str(schoolinfo_titleloader(3)) in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': schoolinfo_loader(3),
                   'photo': {
                       'url': schoolinfo_imgloader(3),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(3)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif str(schoolinfo_titleloader(4)) in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': schoolinfo_loader(4),
                   'photo': {
                       'url': schoolinfo_imgloader(4),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(4)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif str(schoolinfo_titleloader(5)) in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': schoolinfo_loader(5),
                   'photo': {
                       'url': schoolinfo_imgloader(5),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(5)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif str(schoolinfo_titleloader(6)) in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': schoolinfo_loader(6),
                   'photo': {
                       'url': schoolinfo_imgloader(6),
                       'width': 640,
                       'height': 900
                   },

                   'message_button': {
                       'label': "가정통신문 자세히보기",
                       'url': schoolinfo_imgloader(6)
                   }
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })

    elif "정보없음" in selected_keyboard:
            
        return JsonResponse({
               'message': {
                   'text': "가정통신문 정보가 없습니다."
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }
 
        })
        
#공지사항 파트
    elif "공지사항" in selected_keyboard:
        
        return JsonResponse({
               'message': {
                   'text': today_date + "의 " + selected_keyboard + "\n" + "공지사항 테스트"
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }

        })

    elif "학사일정" in selected_keyboard: 

        return JsonResponse({
               'message': {
                   'text': "학사일정 메뉴를 고르세요"
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['오늘', '이번 달']
            }

        })

    elif "오늘" in selected_keyboard: 

        return JsonResponse({
               'message': {
                   'text': today_date + "의 학사일정입니다. \n\n" + schoolschedule_today()
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }

        })

    elif "이번 달" in selected_keyboard: 

        return JsonResponse({
               'message': {
                   'text': month_date + "의 학사일정입니다. \n" + schoolschedule_1month()
               },

               'keyboard': {
                   'type': 'buttons',
                   'buttons': ['급식정보', '가정통신문 보기', '학사일정', '공지사항']
            }

        })


               
        


#나이스에서 학교 급식을 정보를 크롤링 해옵니다.
def meal_parser(): 

    url = 'http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04' #나이스에 있는 급식 파트 부분을 불러옵니다. 해당 학교의 고유 schulCode, schulCrseScCode, schulKndScCode가 필요합니다.
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

    if "[중식]" in today_meal :
        lunch = today_meal[today_meal.index("[중식]"):today_meal.index("[석식]")]
        dinner = today_meal[today_meal.index("[석식]"):]

    else:
        lunch = "정보없음"
        dinner = "정보없음"

    data = "\n#중식정보\n\n"+ lunch + "\n\n----------------------------\n\n#석식정보\n\n" + dinner

    return (data)


#학교홈페이지에서 학교 일정을 정보를 크롤링 해옵니다.
def schoolschedule_parser():

    url = 'http://www.younghoon.hs.kr/76439/subMenu.do' #학교 가정통신문 주소를 입력 해주세요.
    with urlopen(url) as resp:
        html = resp.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    table_tag = soup.find('table')

    info = []

    for td_tag in table_tag.find_all('td'):
        text = td_tag.text.replace("\n\n", "") 
    
        if text.strip():
            info.append(text)
    
    return(info)

# schoolschedule_parser() 함수의 리턴값을 가져와 오늘의 급식정보만 정규식을 통해 가공합니다.
def schoolschedule_today():
    
    now = datetime.datetime.now()
    nowdate = int(now.strftime('%d'))-1

    parsed_data = schoolschedule_parser()
    today_schedule = parsed_data[nowdate]

    try:
       p = re.compile('[[^ \u3131-\u3163\uac00-\ud7a3]+') #한글자음 모음 정규식입니다.

       listed_info = p.findall(today_schedule)
       listed_info[0] = "*"+listed_info[0]
       day_info = "\n*".join(listed_info)

       return(day_info)
    
    except IndexError:
    
       return("정보없음")

# schoolschedule_parser() 함수의 리턴값을 가져와 1달간의 급식정보를 가져옵니다.  
def schoolschedule_1month():
    
    try:
       info = schoolschedule_parser()

       return("\n".join(info))

    except IndexError:
    
       return("정보없음")

# 가정통신문 타이틀만 불러옴
def schoolinfo_titleloader(list_num):
    load_schoolinfo = School_Info.objects.all()

    try:
        return load_schoolinfo[int(load_schoolinfo.count()-list_num)]
    
    except (IndexError, TypeError, AssertionError): 
    
        return ("정보없음")

# 가정통신문 업로드 날짜와 코멘트를 가져옴
def schoolinfo_loader(list_num):

    return "업로드 날짜: "+ str(School_Info.objects.get(title = schoolinfo_titleloader(list_num)).published_date)[0:19] + "\n-------------\n" + School_Info.objects.get(title = schoolinfo_titleloader(list_num)).comment

# 가정통신문 사진을 불러옴
def schoolinfo_imgloader(list_num):

    return "http://nepnep.iptime.org:8000/upload_files/" + str(School_Info.objects.get(title = schoolinfo_titleloader(list_num)).img)
    