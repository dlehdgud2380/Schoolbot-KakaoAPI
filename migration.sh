#!/bin/sh
#model.py에 있는 정보를 sqlite3 데이터베이스에 반영합니다.

echo "데이터 베이스에 반영"

sudo python3 manage.py makemigrations yhbot
sudo python3 manage.py migrate yhbot
