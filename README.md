# Covid_Subway_Project
언제 지하철이 붐비는 지 예측할 수 있다면, 접촉으로 쉽게 감염이 될 수 있는 코로나의 감염 위험도도 예측이 가능하지 않을까?

## Data
- API
  - OpenWether API -> 날씨, 온도, 강수여부 feature
  - Beautiful Soup -> 과거 Covid-19 확진자 정보(키인증이슈), 공휴일 여부
  - 공공데이터 포털 -> 지하철 사용자 수, 지하철 주변 버스정류장 수


## PipeLine
- MongoDB -> data 적재
- SQLite 사용 RDB형태로 저장하여 Dashboard에 이용
![image](https://user-images.githubusercontent.com/50479962/175195267-2f494770-63e8-40ce-a01f-553e13e51719.png)

## Model
- Random Forest Regressor : 지하철 이용객 수 예측 
- Prophet : 시계열 예측 - 코로나 확진자 수
