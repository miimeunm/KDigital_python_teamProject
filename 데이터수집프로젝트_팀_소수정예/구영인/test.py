from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests, time, os

data = pd.read_csv('bestSeller_yes24_구영인.csv', encoding='CP949')
data


# def bestSeller(year, month) :
#     root_url = 'https://www.yes24.com'
    
#     add_year = 'https://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09&year='
#     add_month = '&month='
    
#     set_url = add_year + year + add_month + month
#     # 월간 베스트 url에서 연도(year)와 달(month)가 바뀌도록 url 세팅
    
#     book_list = []
    
#     url = requests.post(set_url)
#     bs = BeautifulSoup(url.text, 'html.parser')
#     books = bs.select('td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)')
#     # 첫 화면에서 request로 html화면을 파싱해서 각 책들의 제목의 내용을 저장
    
#     for book in books :
        
#         # 책들의 제목 요소 중에서 href 링크만 따와서 root_url과 합쳐서 각 책들의 상세페이지 url 생성
#         book_url = root_url + book.attrs['href']
#         book_data = requests.post(book_url)
#         book_bs = BeautifulSoup(book_data.text, 'html.parser')
        
#         # 각 항목(column)별 데이터 뽑아내기
#         # isbn, title, category, writer, point, price, date (isbn, 제목, 장르, 저자, 평점, 가격, 발행일)
#         select_isbn = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(3) > th'
#         if book_bs.select(select_isbn)[0].text != 'ISBN13' :
#             isbn13 = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(4) > td'
#         else :
#             isbn13 = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(3) > td' 
#         isbn = book_bs.select(isbn13)[0].text    

#         select_title = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > div > h2'
#         title = book_bs.select(select_title)[0].text 

#         select_category = '#infoset_goodsCate > div.infoSetCont_wrap > dl:nth-child(1) > dd > ul > li:nth-child(1) > a:nth-child(4)'
#         category = book_bs.select(select_category)[0].text

#         select_writer = '#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_auth > a'
#         writer = book_bs.select(select_writer)[0].text

#         select_point = '#spanGdRating > a > em'
#         point = book_bs.select(select_point)[0].text

#         select_price = book_bs.find_all('span', {'class' : 'nor_price'})
#         price = select_price[0].text

#         select_date = '#infoset_specific > div.infoSetCont_wrap > div > table > tbody > tr:nth-child(1) > td'
#         date = book_bs.select(select_date)[0].text
    
#         # 각 항목들 한 리스트에 담아서 리스트로 저장
#         book_list.append([isbn, title, category, writer, point, price, date])
    
#     # 컬럼명 지정
#     list = ['ISBN', '책 제목', '도서 장르', '저자', '평점', '판매가격', '발행일']
    
#     # pandas에 DataFrame를 사용해서 표를 생성
#     # index_df는 표에서 index를 설정해서 첫 행은 띄어지도록 표시하기 위한 DataFrame
#     # book_list는 데이터
#     index_df = pd.DataFrame(columns=list)
#     index_df.loc[0] = ['', '', '', '', '', '', '']
#     index_df.index = [str(year) + '년' + str(month) + '월']
    
#     book_list = pd.DataFrame(np.array(book_list), columns=list)
#     book_list.index = range(1, len(book_list)+1)
#     book_list = pd.concat([index_df, book_list])

#     return book_list

# list = bestSeller(str(2022), str(7))


# # month_val = 6
# # for month in range(1, 13) :
    
# #     if month < 7 :
# #         year = 2022
# #         month = month_val + month
    
# #     else :
# #         year = 2023
# #         month = month - month_val
    
# #     book_list= bestSeller(str(year), str(month))

# #     if not os.path.exists('bestSeller.csv') :
# #         book_list.to_csv('bestSeller.csv', encoding='CP949', mode = 'w')
# #     else :
# #         book_list.to_csv('bestSeller.csv', encoding='CP949', mode = 'a', header=False)
    
# #     print('YEAR : ' , year)
# #     print('MONTH : ', month)
# #     print('저장완료')
    