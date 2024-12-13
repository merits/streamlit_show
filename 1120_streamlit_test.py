import streamlit as st
import pandas as pd

# OpenStreetMap을 사용하여 지도를 표시하는 HTML 코드
def display_openstreetmap(lat, lon):
    map_html = f"""
    <div id="map" style="width: 100%; height: 500px;"></div>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        var map = L.map('map').setView([{lat}, {lon}], 13); // 지도의 중심좌표 및 확대 레벨 설정

        // OpenStreetMap 타일 레이어 추가
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {{
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }}).addTo(map);

        // 마커를 생성합니다
        var marker = L.marker([{lat}, {lon}]).addTo(map); // 마커 추가
    </script>
    """
    st.components.v1.html(map_html, height=600)

# 하나의 좌표만 포함하도록 수정
map_data = pd.DataFrame(
    {
        'lat': [37.7749],  # 위도
        'lon': [-122.4194]  # 경도
    }
)

# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('OpenStreetMap')  # 제목 생성 
display_openstreetmap(map_data['lat'][0], map_data['lon'][0])  # OpenStreetMap 표시
