import pickle

def predict_covid(n):
    # model pickle 불러오기
    with open('model_ph.pkl','rb') as pickle_file:
        model = pickle.load(open('model_ph.pkl', 'rb'))

    # n일 예측 -> 동적으로 바꿀수 있음 좋겠다...
    future = model.make_future_dataframe(periods=n)
    forecast = model.predict(future)

    fore_num = forecast[['ds','yhat']].tail(1)['yhat']
    fore = format(int(fore_num), ',')

    return fore

