#Step 1. 필요한 모듈과 라이브러리를 로딩합니다.
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd    
import os
import math
from selenium.webdriver.common.by import By

#Step 2. 사용자에게 검색어 키워드를 입력 받습니다.

print("=" *80)
print(" 쿠팡 사이트의 식품 카테고리 Best Seller 상품 정보 추출하기 ")
print("=" *80)

cnt = int(input('1.크롤링 할 건수는 몇건입니까?: '))
page_cnt = math.ceil(cnt/60)

f_dir = input("2.파일을 저장할 폴더명만 쓰세요(기본경로:c:\\py_temp\\):")
if f_dir == '' :
    f_dir="c:\\py_temp\\"

print("\n")

#Step 3.저장될 파일 경로와 이름을 지정합니다
sec_name = '식품'
query_txt = '쿠팡'

n = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (n.tm_year, n.tm_mon, n.tm_mday, n.tm_hour, n.tm_min, n.tm_sec)

os.makedirs(f_dir+s+'-'+query_txt+'-'+sec_name) #중첩된 디렉토리를 한 번에 생성한다. 
os.chdir(f_dir+s+'-'+query_txt+'-'+sec_name) #현재 작업 디렉토리를 변경한다. 

ff_dir=f_dir+s+'-'+query_txt+'-'+sec_name
ff_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.txt'
fc_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.csv'
fx_name=f_dir+s+'-'+query_txt+'-'+sec_name+'\\'+s+'-'+query_txt+'-'+sec_name+'.xls'

# print(ff_name, fc_name, fx_name)

# 제품 이미지 저장용 폴더 생성
img_dir = ff_dir+"\\images"
os.makedirs(img_dir) #이미지 저장 폴더 
os.chdir(img_dir) #작업 디렉토리 변경
    
s_time = time.time( )

#Step 4. 웹사이트 접속 후 해당 메뉴로 이동합니다.
driver = webdriver.Chrome()
query_url='https://www.coupang.com/np/categories/194276'
driver.get(query_url)
driver.maximize_window()
time.sleep(3)

# Access Denied 메시지가 나오면 아래코드로 쿠키를 삭제한다
driver.delete_all_cookies()
time.sleep(2)

# # 분야별 더보기 버튼을 눌러 페이지를 엽니다
# driver.find_element_by_xpath("""//*[@id="header"]/div""").click( )
# time.sleep(2)
# driver.find_element_by_xpath("""//*[@id="gnbAnalytics"]/ul[1]/li[4]/a""").click( )

#Step 5. 내용을 수집합니다
print("\n")
print("===== 곧 수집된 결과를 출력합니다 ^^ ===== ")
print("\n")

ranking2=[]        #제품의 판매순위 저장
title2=[]          #제품 정보 저장
p_price2=[]        #현재 판매가 저장
discount2 = []     #할인율 저장
sat_count2=[]      #상품평 수 저장

img_src2=[]   # 이미지 URL 저장변수
file_no = 0   # 이미지 파일 저장할 때 번호
count = 1     # 총 게시물 건수 카운트 변수

def scroll_down(driver):
    #처음부터 scrollHeightR까지 드래그를 내리겠다.
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)

scroll_down(driver)   #현재화면의 가장 아래로 스크롤다운합니다

for x in range(1,page_cnt + 1) :
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    item_result = soup.find('ul','baby-product-list').find_all('li')

    for li in item_result :
        if cnt < count : #제품건수를 넘었을 때 반복문을 멈춘다. 
            break

        # 제품 이미지 다운로드 하기
        import urllib.request
        import urllib

        try :
            photo = li.find('dt','image').find('img')['src']
        except AttributeError :
            continue

        file_no += 1
        full_photo = 'https:' + photo
        urllib.request.urlretrieve(full_photo,str(file_no)+'.jpg') # 이미지 파일 이름
        time.sleep(0.5)

        #제품 내용 추출하기
        if not os.path.exists(ff_dir):
            os.makedirs(ff_dir)
        f = open(ff_name, 'a', encoding='UTF-8')
        f.write("-----------------------------------------------------"+"\n")
        print("-" *70)

        ranking = count
        print("1.판매순위:",ranking)
        f.write('1.판매순위:'+ str(ranking) + "\n")

        try :
            t = li.find('div','name').get_text().replace("\n","")
        except :
            title = '제품소개가 없습니다'
            print(title.replace("\n",""))
            f.write('2.제품소개:'+ title + "\n")
        else :
            title = t.replace("\n","").strip()
            print("2.제품소개:", title.replace("\n","").strip())                  
            f.write('2.제품소개:'+ title + "\n")

        try :
            p_price = li.find('strong','price-value').get_text().replace("\n","")
        except :
            p_price = '0'
            print("3.판매가격:", p_price.replace("\n",""))
            f.write('3.판매가격:'+ p_price + "\n")
        else :
            print("3.판매가격:", p_price.replace("\n",""))
            f.write('3.판매가격:'+ p_price + "\n")

        try :
            discount = li.find('span','discount-percentage').get_text().replace("\n","")
        except  :
            discount = '0'
            print("4:할인률:", discount)
            f.write('4.할인율:'+ discount + "\n")
        else :
            print("4:할인률:", discount)
            f.write('4.할인율:'+ discount + "\n")

        try :
            sat_count_1 = li.find('span','rating-total-count').get_text()
            sat_count_2 = sat_count_1.replace("(","").replace(")","")
        except  :
            sat_count_2='0'
            print('5.상품평 수: ',sat_count_2)
            f.write('5.상품평 수:'+ sat_count_2 + "\n")
        else :
            print('5.상품평 수:',sat_count_2)
            f.write('5.상품평 수:'+ sat_count_2 + "\n")

        #이미지 엑셀에 추가하기
        # try :
            
        # except  :
        #     title = '이미지가 없습니다'
        # else :
            


        print("-" *70)

        f.close( )             
        time.sleep(0.5)

        ranking2.append(ranking)
        title2.append(title.replace("\n",""))

        p_price2.append(p_price.replace("\n",""))
        discount2.append(discount)

        try :   
            sat_count2.append(sat_count_2)
        except IndexError :
            sat_count2.append(0)

        count += 1
    x += 1      
    # try :
    #     driver.find_element(By.LINK_TEXT ,'%s' %b).click() 
    # except :
    #     driver.find_element(By.LINK_TEXT,'다음 페이지로').click() 
    try :
        driver.find_element(By.LINK_TEXT ,'%s' %x).click() 
    except :
        break
          
#step 6. csv , xls 형태로 저장하기              
co_best_seller = pd.DataFrame()
co_best_seller['판매순위']=ranking2
co_best_seller['제품소개']=pd.Series(title2)
co_best_seller['제품판매가']=pd.Series(p_price2)
co_best_seller['할인율']=pd.Series(discount2)
co_best_seller['상품평수']=pd.Series(sat_count2)

# csv 형태로 저장하기
co_best_seller.to_csv(fc_name,encoding="utf-8-sig",index=False)

# 엑셀 형태로 저장하기
co_best_seller.to_excel(fx_name ,index=False , engine='openpyxl')

e_time = time.time( )
t_time = e_time - s_time

count -= 1
print("\n")
print("=" *80)
print("1.요청된 총 %s 건의 리뷰 중에서 실제 크롤링 된 리뷰수는 %s 건입니다" %(cnt,count))
print("2.총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("3.파일 저장 완료: txt 파일명 : %s " %ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " %fc_name)
print("5.파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)

driver.close()