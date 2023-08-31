import torch
import base64
import io
import joblib
import pandas as pd
from PIL import Image

# 딥 러닝 모델(Yolov5 객체 인식 모델)
def inference(img) :
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/best.pt', force_reload=True)    # 학습한 모델 불러오기
    img = Image.open(img)
    
    result = model(img, size = 640)     # 불러온 모델에 업로드 된 이미지 넣기
    rs = result.pandas().xyxy[0].to_numpy()     # 결과 값을 가져오기 편하도록 numpy형태로 저장
    # print('퍼센트값 :' , rs[0][4])
    
    if len(rs) != 0 :
        ex_per = rs[0][4]       # 예측 퍼센트
        ex_class = rs[0][5]     # 클래스 index
        ex_name = rs[0][6]      # 기구 이름(영문)
         
        result.ims
        result.render()
        
        # 예측되어 라벨링 된 이미지를 BASE64 코드로 변환해서 이미지 모델에 저장
        for img in result.ims :
            buffered = io.BytesIO()
            img_base64 = Image.fromarray(img)
            img_base64.save(buffered, format='JPEG')
            encode_img = base64.b64encode(buffered.getvalue()).decode('utf-8')
            
        data = {
            'img_data' : encode_img,
            'ex_class' : ex_class,
            'ex_name' : ex_name,
            'ex_per' : ex_per,
        }
        
        return data
    
    else :
        return 1