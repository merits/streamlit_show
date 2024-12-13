# ... 기존 코드 ...
import numpy as np
import pandas as pd
import streamlit as st  # Streamlit 모듈 추가

# 지도 위에 표시될 점 좌표 값을 위도경도에 담습니다.
base_position = [37.285438, 127.012756]
# 중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 : lat, 경도 : lon으로 지정하였습니다.
'''
map_data = pd.DataFrame(
    np.random.randn(5, 2) / [20, 20] + base_position,  # 2개의 열로 수정
    columns=['lat', 'lon']
)
'''
map_data = pd.DataFrame(
    {
        'lat': [37.285438],  # 위도
        'lon': [127.012756]  # 경도
    }
)

# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('Map of Data')  # 제목 생성 
st.map(map_data)  # 지도 생성
# ... 기존 코드 ...
