import numpy as np
import pandas as pd 

#지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
base_position =  [37.285438, 127.012756]
#중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])
# map data 생성 : 위치와 경도 

print(map_data)
