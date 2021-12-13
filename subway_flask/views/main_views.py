from flask import Blueprint, render_template, request, jsonify
from subway_flask.api import get_city_data, get_today_corona
from subway_flask.search_info import transfer_type, find_bus
from subway_flask.ml_li import predict_subway
from subway_flask.ml_ph import predict_covid
from subway_flask.db_info import MONGO_URI, DATABASE_NAME, COLLECTION_NAME
from pymongo import MongoClient
from datetime import datetime
import pickle
import os


main_bp = Blueprint('main',__name__)

# 매일 변하는 데이터 불러오기
weather, minTa, maxTa, nowTa = get_city_data()
todayPeople = get_today_corona()

# home
@main_bp.route('/')
def home():
    return render_template('index.html')

# 입력 페이지
@main_bp.route('/input', methods=['POST', 'GET'])
def input():
    # Get method
    if request.method == 'GET':
        return render_template('input.html', weather=weather, maxTa=maxTa, minTa=minTa, nowTa=nowTa, todayPeople=todayPeople), 200

# 결과페이지
@main_bp.route('/predict', methods=['POST'])
def predict():

    # year = datetime.today().year
    # month = str(datetime.today().month).zfill(2)
    # day = str(datetime.today().day + 1).zfill(2)

    if request.method == 'POST':
        # 변수 받기
        p_date = request.form['p_date']
        p_subline = request.form['p_subline']
        p_station = request.form['p_station']
        p_min = request.form['p_min']
        p_avg = request.form['p_avg']
        p_max = request.form['p_max']
        p_rain, p_holiday = transfer_type(request.form.get('p_rain'), request.form.get('p_holiday'))
        # 입력된 역 기준으로 데이터 베이스에서 버스정류장 번호 찾기
        try:
            p_bus = find_bus(p_station, str(p_subline))
        except:
            render_template('input.html', weather=weather, maxTa=maxTa, minTa=minTa, nowTa=nowTa, todayPeople=todayPeople), 200
        # 예측해야하는 행 수 계산
        n = (int(p_date[-2:]) - 12)

        # 모델
        predictSub, new, stat = predict_subway(p_avg, p_min, p_max, p_rain, p_holiday, p_bus)
        predictCo = predict_covid(n)

        # 결과값 합쳐 db 반영
        new['predict_sub'] = predictSub
        new['predict_co'] = predictCo
        data = new.loc[0].to_dict()
        client = MongoClient(MONGO_URI)
        db = client[DATABASE_NAME][COLLECTION_NAME].insert_one(data)

    # 12일 이후 경과 시간 + 1

    return render_template('outcome.html',
                           predictCorona=predictCo,
                           weather=weather, maxTa=maxTa, minTa=minTa, nowTa=nowTa, todayPeople=todayPeople,
                           station=p_station, line =p_subline, predictSubway=predictSub,
                           year=p_date[:4], month=p_date[5:7], day=p_date[-2:],
                           status = stat)


# json_file로 API 받아오기
@main_bp.route('/data')
def get_data():
    data = { 'weather' : weather, 'minTa': minTa, 'maxTa' : maxTa, 'nowTa' : nowTa}
    return jsonify(data)

