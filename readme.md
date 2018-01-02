# 카카오플러스 학교정보 자동응답봇

![](https://scontent-icn1-1.xx.fbcdn.net/v/t31.0-8/21427425_1830905700554575_1288293878148381013_o.png?oh=cb4b0e773515078a5be41fcb25bd5826&oe=5AF884D0)

영훈앱2.0 개선 및 마무리를 목표로 하여 제작한 파이썬자동응답봇입니다.


취지는 학교공지를 카카오톡으로 전달 할 수 있도록 하기 위해 제작 되었습니다.

사용하시기전 Python언어와 Django웹프레임워크에 대한 이해를 습득하시고 사용하시는 것을 추천합니다.

#### 1. Django 웹프레임워크 사용법

https://tutorial.djangogirls.org/ko/
    (Django 웹프레임워크 사용법을 한번 보고 오시는 걸 추천합니다.)

#### 2. Python

https://wikidocs.net/book/1
    (Python 언어에 대한 기본적인 이해를 요구합니다.)

#### 3. 카카오톡 자동응답

https://github.com/plusfriend/auto_reply
    (카카오톡 자동응답설정 하는 법을 숙지해주세요.)
    
    
#### 4. 사양 및 사용된 라이브러리

#### 사양
Python 3.6.3
Django Webframework
SQLlite3

#### 라이브러리
Beautiful Soup 4
Pillow


## 0\. 목차

1. 기능

2. 필수패키지 설치 및 세팅

3. 월간학사일정 및 급식정보를 불러오기 위한 세팅

4. 가정통신문 등록하기

## 1\. 기능

![](https://i.imgur.com/yFAjYrY.jpg)


## 2\. 필수 패키지 설치 및 세팅
서버 구동에 필수적으로 요구되는 라이브러리입니다. 
```
pip3 install django && pip3 install Pillow && pip3 install bs4
```
django: 봇 서버를 구동시켜주는 파이썬 웹프레임워크
Pillow: 파이썬에서 이미지 처리를 해주는 라이브러리
bs4: BeautifulSoup 웹 파싱 라이브러리
**※구동에 필수 라이브러리입니다. 미설치시 서버구동이 안됩니다.**


그 다음으로 해줘야 할 것은 ALLOWED_HOSTS에 외부에서 접근할 수 있는 ip 및 URL주소를 입력하여 admin 페이지에 접속 할 수 있도록 해줘야합니다. 
**kakaoplusfriend_schoolbot/kap_yhbot/settings.py**를 열어주시고 
ALLOWED_HOSTS라는 리스트변수를 찾아 외부에서 접속할 수 있는 주소를 입력해주세요.
```
28    ALLOWED_HOSTS = [ 서버 url, 서버 ip]
```

마지막으로 이 부분은 새로 django project로 새로 생성해서 참고용으로 이용하시는 분은 목차 3으로 바로 넘어가시면 되지만 그대로 clone해서 사용하시는 분들은 보안을 위해 꼭 확인해주셔야 하는 부분입니다.
django SECRET KEY를 새로 발급을 받아야합니다. 이건 쿠키데이터 해시 및 암호쪽에 임시적으로 사용되는 것이기 때문에 아주중요합니다. 
https://www.miniwebtool.com/django-secret-key-generator/
이쪽에서 새로 키를 발급받고 **kakaoplusfriend_schoolbot/kap_yhbot/settings.py**를 열어줍니다 .
해당 홈페이지에서 발급받은 키를 복사하여 SECRET_KEY변수에 붙여넣기 해줍니다.
```
23    SECRET_KEY = '이쪽에 붙여넣기'
```
## 3\. 월간학사일정 및 급식정보를 불러오기 위한 세팅

사용자의 학교에 맞춰서 급식정보, 학사일정, 정보를 불러오기 위해 링크를 수정할 것입니다. **kakaoplusfriend_schoolbot/yhbot/views.py**를 열어보시고

12줄부터 15번째줄에 해당하는 변수에 코드를 입력해주세요.
```
12     url_educationoffice = '해당하는 학교의 소속교육청입력' 
13     schulCode = '학교의 고유코드입력' 
14     chulCrseScCode =  '학교 분류코드입력' 
15     schulKndScCode =  '학교 종류코드입력' 
```
예: (영훈고등학교를 예로 들었습니다.)

(급식주소)
http://stu.sen.go.kr/sts_sci_md00_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04

(월간학사일정 주소)
http://stu.sen.go.kr/sts_sci_sf01_001.do?schulCode=B100000505&schulCrseScCode=4&schulKndScCode=04

**url_educationoffice**는 학교에 소속된 교육청주소를 입력해주세요.
```
stu.sen.go.kr(서울특별시 교육청)
```
**schulCode**는 학교고유코드입니다.
```
B100000505(영훈고등학교)
```
   

**schulCrseScCode**는 학교 분류입니다.
```
1 : 유치원
2 : 초등학교
3 : 중학교
4 : 고등학교(영훈고등학교는 이쪽에 해당)
```
**schulKndScCode**는 학교 종류입니다.
```
01 : 유치원
02 : 초등학교
03 : 중학교
04 : 고등학교(영훈고등학교는 이쪽에 해당)
```
schulCode(학교고유번호) 검색은 이 주소에서 검색하시면 됩니다.
https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do

※나이스 주소를 넣었을 때 어떤 학교든 정상적으로 파싱이 되게 설계하였습니다. 일부 학교는 값이 이상하게 나올 수도 있으니 맞게 수정을 해주시면 되겠습니다.

## 4\. 가정통신문 등록하기

앞서 가정통신문은 파싱을 통해 작동되는 방식이 아님을 미리 알립니다.
어드민 페이지를 통해 가정통신문 이미지 파일을 업로드하여 불러오는 방식입니다.

view.py를 열고 운영하는 서버 주소를 402번째 줄에 추가해줍니다.
```
400      def schoolinfo_imgloader(list_num):
401  
402          return '이쪽에 주소입력'+ '/upload_files' + str(School_Info.objects.get(title = schoolinfo_titleloader(list_num)).img)
```
앞서서 해당 명령어로 어드민 페이지에 접속할 계정을 만들어주세요.
```
python3 manage.py createsuperuser
```
그다음 **http://localhost(또는 자신의 서버 ip):8000/admin**으로 웹브라우저를 통해 접속합니다.

접속하면 어드민 페이지 로그인화면이 뜹니다. 생성한 계정으로 로그인 해주세요.
![](https://i.imgur.com/vhiyL6S.png)


로그인이 되면 School_Infos라는 부분이 보입니다. 저기를 눌러주세요 
![](https://i.imgur.com/ob8Eg47.png)


추가버튼을 눌러줍니다.
![](https://i.imgur.com/ChGg19I.png)

제목과 코멘트 입력을 해주시고 이미지를 첨부합니다. 그리고 저장버튼을 눌러줍니다.
**※파일명은 무조건 영어또는 숫자로 해서 업로드 해주세요.**
![](https://i.imgur.com/xhtu8gy.png)

데이터베이스에 저장된 정보를 불러오는 것을 확인 할 수 있습니다.
![](https://i.imgur.com/GyqXTAq.jpg)

응용을 한다면 comment에 google docs 설문지링크를 달아 가정통신문 신청서를 작성하게 할 수 있습니다.







