#File Processing
#Text File (메모장) 제외 Binary File(고유의 SW가 필요하다. - 코드 주소 필요)
#Binary File - image file 중 Raw File

import os.path
import math

##display (이게 바로 image)
filename = "C:/Users/ahyeo/PycharmProjects/BigLeaderAIProject/Etc_Raw(squre)/LENA256.RAW"
fsize = os.path.getsize(filename)
height = width = int(math.sqrt(fsize)) #256X256이니까 루트를 통해서 가로 세로 길이를 알아내는 것
print(height, 'x', width)
#메모리 확보(영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)] #width X height 배열을 0으로 초기화하는 코드
#파일 - 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) #숫자로 가져오기 위해서 ord() 사용 (아니면 외래어 나옴)
rfp.close()

##일부분만 확인
# for i in range(100, 105, 1):
#     for k in range(100, 105, 1):
#         print("%3d " % image[i][k], end='')
#     print()
# print()

##반전 처리
for i in range(height):
    for k in range(width):
        image[i][k] = 255 - image[i][k]

for i in range(height):
    for k in range(width):
        print("%3d " % image[i][k], end='')
    print()
print()
