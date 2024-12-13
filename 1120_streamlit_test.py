import streamlit as st
import folium
import pandas as pd

# 하나의 좌표만 포함하도록 수정
map_data = pd.DataFrame(
    {
        'lat': [37.7749],  # 위도
        'lon': [-122.4194]  # 경도
    }
)

# Folium을 사용하여 지도 생성
def create_map(lat, lon):
    # Folium 지도 생성
    m = folium.Map(location=[lat, lon], zoom_start=13)
    # 마커 추가
    folium.Marker([lat, lon], popup='Marker').add_to(m)
    return m

# Streamlit 앱에서 지도 표시
st.subheader('Folium Map')  # 제목 생성 
map_object = create_map(map_data['lat'][0], map_data['lon'][0])  # Folium 지도 생성
# Folium 지도를 HTML로 변환하여 Streamlit에 표시
st.write(map_object._repr_html_(), unsafe_allow_html=True)
