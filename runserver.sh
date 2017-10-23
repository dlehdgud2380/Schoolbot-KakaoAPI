#!/bin/sh
#리눅스에서 Djago서버를 실행합니다.

echo "리눅스에서 장고서버를 실행합니다"

sudo python3 manage.py runserver 0.0.0.0:8000
