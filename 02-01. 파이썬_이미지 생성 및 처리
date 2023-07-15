import random as rand

##2D array

##Function

##display (이게 바로 image)
def Display():
    for i in range(ROW):
        for k in range(COL):
            print("%3d " % image[i][k], end='')
        print()
    print()

##Parameter
ROW, COL = 5, 5
image = None

##Memory Malloc
image = [] #위에 함수에서 정의할거니까 None으로 설정한다.
tmpAry = []

#image를 2D array로 만드는 방법
for i in range(ROW):
     for k in range(COL):
        tmpAry.append(0)
     image.append(tmpAry)
     tmpAry = [] #초기화

#file - Memory Loading
for i in range(ROW):
    for k in range(COL):
        pixel = rand.randint(0, 255)
        image[i][k] = pixel

Display()

## Image processing !!!

## (1) 영상을 50 밝게 처리하자. (숫자 더하기)
for i in range(ROW):
    for k in range(COL):
        # 먼저 확인을 안하면, 오버플로우가 발생하지 않아도 프로그램이 죽을 수도 있다.
        if(image[i][k] + 50 > 255):
             image[i][k] = 255
         else:
             image[i][k] += 50
Display()

## (2) 영상을 100 어둡게 처리하자. (숫자 빼기)
for i in range(ROW):
    for k in range(COL):
         if(image[i][k] - 100 < 0):
             image[i][k] = 0
         else:
             image[i][k] -= 100

Display()

## (3) 완전 흑백 처리

# 중앙값을 통해 완전 흑백 처리 가능 (큰 의미는 없다) - 이상한 값이 나올 수 있기 때문에 안전상으로 수행하기
hap = 0
avg = 0 #참조오류때문에 사용하는 것이 좋다.
for i in range(ROW):
    for k in range(COL):
        hap += image[i][k]
avg = hap / (ROW*COL)
for i in range(ROW):
    for k in range(COL):
        if(image[i][k] >= avg):
            image[i][k] = 255
        else:
            image[i][k] = 0

Display()

# 128을 기준으로 반 나누어서 흑백 처리하기
for i in range(ROW):
    for k in range(COL):
        if(image[i][k] >= 128): #128이든, 127이든 상관 없다.
            image[i][k] = 255
        else:
            image[i][k] = 0

Display()

## (4) 반전 처리
for i in range(ROW):
    for k in range(COL):
        image[i][k] = 255-image[i][k]

Display()
