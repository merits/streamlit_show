import streamlit as st
import pandas as pd

# 카카오 지도 API를 사용하기 위한 HTML 코드
def display_kakao_map(lat, lon):
    map_html = f"""
    <div id="map" style="width: 100%; height: 500px;"></div>
    <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=f077adabc59c0f4120c0c3bc6d5fae7b"></script>
    <script>
        var mapContainer = document.getElementById('map'); // 지도를 표시할 div 
        var mapOption = {{
            center: new kakao.maps.LatLng({lat}, {lon}), // 지도의 중심좌표
            level: 3 // 지도의 확대 레벨
        }};
        
        var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

        // 마커를 생성합니다
        var markerPosition  = new kakao.maps.LatLng({lat}, {lon}); 
        var marker = new kakao.maps.Marker({{ position: markerPosition }}); // 수정된 부분
        marker.setMap(map); // 마커를 지도에 표시합니다
    </script>
    """
    st.components.v1.html(map_html, height=600)

# 하나의 좌표만 포함하도록 수정
map_data = pd.DataFrame(
    {
        'lat': [37.285438],  # 위도
        'lon': [127.012756]  # 경도
    }
)

# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('Kakao Map')  # 제목 생성 
display_kakao_map(map_data['lat'][0], map_data['lon'][0])  # 카카오 지도 표시
