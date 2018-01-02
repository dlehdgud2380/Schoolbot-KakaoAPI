카카오플러스 학교정보 자동응답봇
==============================
![](https://scontent-icn1-1.xx.fbcdn.net/v/t31.0-8/21427425_1830905700554575_1288293878148381013_o.png?oh=cb4b0e773515078a5be41fcb25bd5826&oe=5AF884D0)

영훈앱2.0 개선 및 마무리를 목표로 하여 제작한 파이썬자동응답봇입니다.
개발환경은 Python3.6.3이며 사용한 웹프레임워크는 Django입니다. 데이터베이스는 SQLlite3를 사용했습니다. 파싱에는 Beautiful Soup 라이브러리가 사용되었습니다.

취지는 학교공지관련 전산을 카카오톡으로 더 쉽게 더 편하게 알려주기 위해 만들게 되었습니다. 

사용하시기전 Python언어와 Django웹프레임워크에 어느정도 이해하시는 것을 추천합니다.

1. Django 웹프레임워크 사용법
https://tutorial.djangogirls.org/ko/
(Django 웹프레임워크 사용법을 한번 보고 오시는 걸 추천합니다.)

2. Python 
https://wikidocs.net/book/1 
(Python 언어에 대한 기본적인 이해를 요구합니다.)

3. 카카오톡 자동응답
https://github.com/plusfriend/auto_reply 
(카카오톡 자동응답설정 하는 법을 숙지해주세요.)

## 0. 목차
1. 기능
2. 월간학사일정 및 급식정보 불러오기
3. 가정통신문 등록하기

## 1. 기능
* **가정통신문 기능**
![](https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/21768059_1837013486610463_8242130654175268927_n.jpg?oh=aa7bae5b0a8487b7026ed84cfbfc3748&oe=5AFCF937)
![](https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/21687943_1837013496610462_3751951653458047538_n.jpg?oh=3fc04515816b18439a4c413d1d6ca32a&oe=5AFD79D4)



* **중식 및 석식 조회**
![](https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/21078499_1826277991017346_9051141542305306283_n.jpg?oh=c6c8217f5c1bdeb1079c0b71f2fcdbf9&oe=5AB1AC22)



* **오늘 및 이번 달 학사일정 조회**
![](https://scontent-icn1-1.xx.fbcdn.net/v/t1.0-9/21557479_1831367327175079_4829560746013230479_n.jpg?oh=de997663fcdf8c2d1c62fcb68ec79904&oe=5AB48B1B)

## 2. 월간학사일정 및 급식정보 불러오기
① 사용자의 학교에 맞춰서 급식정보, 학사일정, 정보를 불러오기 위해 링크를 수정할 것입니다.               **kakaoplusfriend_schoolbot/yhbot/views.py**를 열어보시고
**def meal_parser():** 라는 함수와 **def schoolschedule_parser():** 라는 함수를 찾아주세요.

② **url변수**에 서비스 하시려는 해당 학교 나이스 홈페이지 주소를 넣어주시면 됩니다.

예: (영훈고등학교를 예로 들었습니다.)
(급식주소) 
http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04
(월간학사일정 주소) 
http://stu.sen.go.kr/sts_sci_sf01_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04


**schulCode**는 학교고유코드입니다.

    B100000505(영훈고등학교)
    
**schulCrseScCode**는 학교 분류입니다

    1 : 병설유치원
    2 : 초등학교
    3 : 중학교
    4 : 고등학교

**schulKndScCode**는 학교 종류입니다

    01 : 유치원
    02 : 초등학교
    03 : 중학교
    04 : 고등학교

고유번호 검색은 이 주소에서 가능합니다.
https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do

※나이스 주소를 넣었을 때 어떤 학교든 정상적으로 파싱이 되게 설계하였습니다. 일부 학교는 값이 이상하게 나올 수도 있으니 맞게 수정을 해주시면 되겠습니다. 

③ 마지막으로 메인 디렉토리(/kakaoplusfriend_schoolbot)로 나와 터미널에 ./runserver.sh(리눅스 및 OSX 기준)를 입력해주시고 django서버를 실행합니다. 

## 3. 가정통신문 등록하기
앞서 가정통신문은 파싱을 통해 작동되는 방식이 아님을 미리 알립니다.
어드민 페이지를 통해 가정통신문 이미지 파일을 업로드하여 불러오는 고전적인 방식입니다. 

① http://localhost(또는 자신의 서버 ip):8000/admin으로 접속합니다.
② 