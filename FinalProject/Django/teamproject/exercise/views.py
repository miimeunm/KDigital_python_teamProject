from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .models import ImgModel, Exercise
from . import inference

# Create your views here.
def index(request) :
    return render(request, 'exercise/index.html')

def upload(request) :
    if request.method == 'POST' :
        form = UploadFileForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()     # 폼이 정상적이라면 저장
            img_url = 'media/' + str(form.cleaned_data['file'])     # 이미지 경로 생성
            # print(img_url)
            # print('뽑아낸값 : ', form.cleaned_data['file']) 
            
            rs_data = inference.inference(img_url)      # 딥 러닝 예측 모델 돌려서 반환 후 rs_data에 저장
            
            if rs_data == 1:
                form = UploadFileForm()
                return render(request, 'exercise/upload.html', {'form' : form, 'alert_message': '운동 사진 업로드 바람'})

            else:
                result = ImgModel()    # 예측 모델 이미지 저장하기 위해 모델 생성
                # 예측 된 값(rs_data)를 이미지 모델에 저장 (파일 이름, 예측 라벨링 포함된 이미지, 기구 클래스, 기구 이름, 예측 퍼센트)
                result.img_data = rs_data['img_data']
                result.ex_class = rs_data['ex_class']
                result.ex_name = rs_data['ex_name']
                result.ex_per = rs_data['ex_per']

                result.save() # 모델 저장

                return redirect(reverse('exercise:result'))

    else :
        form = UploadFileForm()
        
    return render(request, 'exercise/upload.html', {'form' : form})

def result(request) :
    # 라벨링 된 사진
    img = ImgModel.objects.last()   # 직전 모델 select 해서 불러오기
    # select한 모델에서 값 가져오기
    img_data = img.img_data
    ex_class = img.ex_class
    ex_name = img.ex_name
    ex_per = int(round(img.ex_per, 2) * 100)
    # print("라벨링 예측 값 (Predict): " , ex_class, ex_name, ex_per )
    
    # 운동 순서(클래스)에 따른 운동 부위, 기구 이름들
    # 리스트를 생성해서 DB에서 클래스 숫자를 인덱스로 받아서 검색될 수 있도록 변수 처리
    ex_part_list = ['팔', '허리', '등', '가슴', '가슴', '가슴', '엉덩이', '등', 
                    '허벅지', '허벅지', '허벅지', '어깨', '허벅지']  
    ex_name_list = ['암컬', '백 익스텐션', '케이블머신', '펙덱 플라이 머신', '체스트 프레스 머신', 
                    '어시스트 치닝 앤 디핑 머신', '힙 어브덕션', '랫 풀 다운', '레그 익스텐션', '레그 프레스',
                    '레그 컬 - 라잉', '숄더 프레스 - 머신', '스쿼트 - 스미스 머신']
    
    ex_pred_part = ex_part_list[ex_class]
    ex_pred_name = ex_name_list[ex_class]
        
    # print('이름 예측 값 (Predict): ', ex_pred_name)
    # print('부위 예측 값 (Predict): ', ex_pred_part)
        
    # 예측한 이미지 객체의 값들
    # 처리한 변수를 바탕으로 운동 데이터에서 검색
    predict_result = Exercise.objects.get(ex_name = ex_pred_name)
    pre_text = predict_result.ex_method.replace(". ", ".<br>")

    # 머신러닝 모델 학습
    mac_predict = inference.machine_inference(ex_pred_part)
    
    # 머신러닝 결과 값을 zip으로 묶어서 한번에 던지기
    
    name_predict = list(mac_predict.ex_name)
    print(name_predict)
    index_predict = list(mac_predict.index)
    zip_data = zip(name_predict, index_predict)
    
    ex_video1 = predict_result.ex_video1

    context = {
        'img_data' : img_data,
        'ex_class' : ex_class,
        'ex_name' : ex_name,
        'ex_per' : ex_per, 
        'predict_result' : predict_result,
        'zip_data' : zip_data,
        'pre_text' : pre_text,
        'ex_video1' : ex_video1,
    }
    
    return render(request, 'exercise/result.html', context)

# 추천 운동 상세 설명 페이지
def detail(request, id):
    ex_detail = Exercise.objects.get(id=id)
    ex_text = ex_detail.ex_method.replace('. ', '.<br>')
    ex_video1 = ex_detail.ex_video1

    context = {
        'ex_video1' : ex_video1,
        'ex_detail' : ex_detail,
        'ex_text' : ex_text,
    }

    return render(request, 'exercise/detail.html', context)