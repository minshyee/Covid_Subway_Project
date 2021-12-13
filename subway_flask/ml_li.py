import pickle
import pandas as pd
import os

# 탑승객 예측 모델

def predict_subway(avgTa, minTa, maxTa, sumRn, day_info, bus_cnt):

    FILENAME = 'pipe.pkl'
    MODEL_PATH = os.path.abspath(os.path.join(os.getcwd(), FILENAME))

    #pickle파일 읽어오기
    with open(MODEL_PATH,'rb'):
        pipe = pickle.load(open('pipe.pkl', 'rb'))

    # 입력 df로 넣어주기
    df = pd.DataFrame(data=[[avgTa, minTa, maxTa, sumRn, day_info, bus_cnt]],
                      columns=['avgTa', 'minTa', 'maxTa', 'sumRn', 'day_info', 'bus_cnt']
                      )

    pred_num = int(pipe.predict(df)[0])
    if pred_num > 30000:
        stat = '혼잡한'
    elif pred_num > 10000:
        stat = '상대적으로 수월한'
    else:
        stat = '한산한'
    pred = format(pred_num, ',')
    return pred, df, stat

