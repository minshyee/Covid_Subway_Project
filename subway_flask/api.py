import requests
import json
from bs4 import BeautifulSoup

API_KEY = '5830c843e512b669280f21fa3ad0c3b6'

def get_city_data():
    """
    현재 날씨 값 불러오기
    """
    CURRENT_WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}"

    c_weather = requests.get(CURRENT_WEATHER_URL)
    current_weather = json.loads(c_weather.text)
    weather = current_weather['weather'][0]['main']
    temps = round(float(current_weather['main']['temp'] - 273.15),1)
    temp_min = round(float(current_weather['main']['temp_min'] - 273.15),1)
    temp_max=round(float(current_weather['main']['temp_max'] - 273.15),1)

    return weather, temp_min, temp_max, temps


def get_today_corona():
    """
    오늘 확진자 수
    """
    BASE_URL = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    today = soup.select('div.caseTable>div>ul>li>dl>dd.ca_value')[6].text

    return today
