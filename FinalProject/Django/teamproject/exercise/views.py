from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .models import ImgModel
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
            
            result = ImgModel()     # 예측 모델 이미지 저장하기 위해 모델 생성
            # 예측 된 값(rs_data)를 이미지 모델에 저장 (파일 이름, 예측 라벨링 포함된 이미지, 기구 클래스, 기구 이름, 예측 퍼센트)
            result.img_name = 'infer_' + str(form.cleaned_data['file'])
            result.img_data = rs_data['img_data']
            result.ex_class = rs_data['ex_class']
            result.ex_name = rs_data['ex_name']
            result.ex_per = rs_data['ex_per']
            
            result.save()       # 모델 저장
            
            return redirect(reverse('exercise:result'))
    else :
        form = UploadFileForm()
        
    return render(request, 'exercise/upload.html', {'form' : form})