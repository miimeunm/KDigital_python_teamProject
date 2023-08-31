from django.db import models
from django_base64field.fields import Base64Field

# Create your models here.
class UploadFile(models.Model) :
    # 파일 업로드 모델
    file = models.FileField(null=True)
    
    def __str__(self):
        return f'{self.file}'
    
class ImgModel(models.Model) :
    # 예측 이미지 저장 모델
    img_name = models.CharField(max_length=50, null=True)
    
    # base64 인코딩한 객체 인식 이미지 파일
    img_data = Base64Field(max_length=900000, blank=True, null=True)
    
    # 운동 클래스 번호..(이걸로 부위 나눌수있을거가튼디..)
    ex_class = models.IntegerField()
    
    # 운동기구 이름
    ex_name = models.CharField(max_length=50)
    
    # 운동기구 예측 퍼센트
    ex_per = models.FloatField(blank=True)
    
    def __str__(self):
        return f'file_name : {self.img_name}'