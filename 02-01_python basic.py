#영상처리 - 색상 이미지

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *

import os
import math

##FUCTION DEFINE

### 공통 함수부 ###
def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 파일을 가져오는 것 (그 중 raw 파일만을 가져온다.)
    filename = askopenfilename(parent = window,
                               filetypes=(("raw file", "*.raw"), ("모든 파일", "*.*")))

    #파일 읽어서 가져오기
    fsize = os.path.getsize(filename)
    inH = inW = int(math.sqrt(fsize))
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # 파일 - 메모리 로딩
    rfp = open(filename, 'rb')
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = ord(rfp.read(1))
    rfp.close()
    equalImage()

def displayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    if (canvas != None):
        canvas.destroy()

    window.geometry(str(inH) + 'x' + str(inW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal') #중앙점 찾기

    #for i in range(outH):
    #    for k in range(outW):
    #        r = g = b = outImage[i][k]
    #        paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    rgbString = ""
    for i in range(outH):
        tmpString = "" #한 줄(512개)를 만든다.
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} ' #한줄의 rgb 출력 = 512개 / 마지막 한 칸을 띄워야지 줄바꿈 생성 가능
    paper.put(rgbString)

    canvas.pack()

def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    # 메모리 확보 (Input Image와 OutputImage의 파일 크기가 달라질 수 있기 때문에 동일하게 설정하는 것은 안좋음. - 예시: 확대, 축소)
    # 중요 ! 출력 이미지 크기 결정하기
    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]  # 배열 초기화는 확실히 해주는 것이 좋음

    ##영상처리 알고리즘 구현 !!! (알고리즘 구현시에는 이 부분만 변경해주면 되는 것이다. - 하나의 플랫폼으로 생각하기)
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
    #################################################################################################

    displayImage()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    saveFp = asksaveasfile(parent = window, mode = 'wb', defaultextension='*.raw'
                           , filetypes=(('raw file', '*.rqw'), ('모든 파일', '*.*')))

    #파일 저장법
    import struct
    for i in range(outH):
        for k in range(outW):
            saveFp.write((struct.pack('B', outImage[i][k])))
    saveFp.close()
    messagebox.showinfo('저장', saveFp.name + '   Save Success!!')

#def ExitImage():

### 영상처리 함수부(핵심 함수) ###

## 이미지 반전 함수
def reverseImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255 - inImage[i][k]

    displayImage()

### 이미지 밝기 조절 함수
def addImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    value = askinteger("밝게/어둡게", "밝기 조절 값", minvalue = -255, maxvalue = 255)

    for i in range(inH):
        for k in range(inW):
            if(value + inImage[i][k] <0):
                outImage[i][k] = 0
            elif (value + inImage[i][k] > 255):
                outImage[i][k] = 255
            else:
                outImage[i][k] = value + inImage[i][k]

    displayImage()

## 이미지 흑백 처리 함수 (중앙 바이트값)
def white_black_byte():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] < 128):
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255

    displayImage()

## 이미지 흑백 처리 함수 (평균값)
def white_black_avg():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    hap = 0

    for i in range(inH):
        for k in range(inW):
            hap += inImage[i][k]
            avg = hap / (inH * inW)

    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] < avg):
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255

    displayImage()

## 이미지 흑백 처리 함수 (퀵정렬)

def Quick_Sort(arr):

    # 원소가 하나도 없을 때
    if len(arr) <= 1:
        return

    start = 0

    pivot = arr[start]
    left_arr = []
    right_arr = []
    piv_arr = []

    for i in arr:
        if i < pivot:
            left_arr.append(i)
        elif i > pivot:
            right_arr.append(i)
        else:
            piv_arr.append(i)

    Quick_Sort(left_arr)
    Quick_Sort(right_arr)

    arr[:] = left_arr + piv_arr + right_arr

    return arr

def white_black_Quick_Sort():
    sort = []
    for i in range(inH):
        for k in range(inW):
            sort.append(inImage[i][k])

    result = Quick_Sort(sort)
    index = len(result) // 2

    for i in range(inH):
        for k in range(inW):
            if (inImage[i][k] >= result[index]):
                outImage[i][k] = 255
            else:
                outImage[i][k] = 0

    displayImage()

def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    x_Val = askinteger("X축 값", "")
    y_Val = askinteger("Y축 값", "")

    # 외부에 접근하는 것이기 때문에 프로그램이 죽을 수 밖에 없음, 그렇기 때문에 먼저 위치를 확인을 하고, 위치가 없음 버려야한다. (if문)
    for i in range(inH):
        for k in range(inW):
            if (0<=i+x_Val<outH) and (0<=k+y_Val<outW):
                outImage[i+x_Val][k+y_Val] = inImage[i][k]

    displayImage()

#인덱싱 !!! 중요 (포워딩 -> 효율측면에서 굳이 덮어쓰는 것이 필요없다.. -이 부분은 효율을 위해 백워딩을 하자!)
def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("축소 배율", "몇 배 축소할 것 인가요?")

    #포워딩 기법
    outH = inH // scale
    outW = inW // scale
    outImage = [[0 for _ in range(outW)] for _ in range(outH)] #outImage 크기를 정하기 위해서 축소 배율을 먼저 입력 받는다.

    for i in range(inH):
        for k in range(inW):
            outImage[i//scale][k//scale] = inImage[i][k]

    displayImage()

#백워딩 기법 다시 이해하기
def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("확대 배율", "몇 배 확대할 것 인가요?")

    #백워딩 기법
    outH = int(inH * scale)
    outW = int(inW * scale)
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    # for i in range(inH):
    #     for k in range(inW):
    #         outImage[i * scale][k * scale] = inImage[i][k]

    for i in range(outH):
        for k in range(inH):
            outImage[i][k] = inImage[i//scale][k//scale] #홀 잡아준다.

    displayImage()

#회전
def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    #메모리 할당은 동일하게 하기
    outH = inH
    outW = inW
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]

    angle = askinteger("각도", "각도를 입력하세요.")
    radian = angle * math.pi / 180.0 #삼각함수가 프로그램에서는 라디안용이기 때문에 변경해줘야 한다.

    #홀문제 해결 (백워딩)
    cx = inH //2
    cy = inW //2

    for i in range(outH):
        for k in range(outW):
            oldI = int(math.cos(radian) * (i - cx) + math.sin(radian) * (k - cy)) + cx #문제를 해결하기 위해 빼줬던 만큼 다시 더해준다.
            oldK = int(-math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy)) + cy

            if (0 <= oldI < inH) and (0 <= oldK < inW):
                outImage[i][k] = inImage[oldI][oldK]

    displayImage()

##PARAMETER
InImage = OutImage = [] #배열로 해줘도 아~무 상관없음!
#InImage = OutImage = None
inH, inW, OutH, OutW = 0, 0, 0, 0
window, canvas, paper = None, None, None
filename = ""

##MAIN CODE

window = Tk()
window.geometry('300x300')
window.title('GrayScale Image Processing (Beta_1)')

mainMenu = Menu(window) #메뉴의 틀
window.config(menu = mainMenu) #위에 메뉴바를 생성하기

# 상위 메뉴(파일)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu) #파일 확장되는 것

fileMenu.add_command(label = "파일 열기", command = loadImage) #파일 열기 - 명령어 실행 (파일 메뉴의 하단 메뉴?)
fileMenu.add_command(label = "파일 저장", command = saveImage)
fileMenu.add_separator() #종료 전에 굵은 선? 처럼 나타난다.
fileMenu.add_command(label = "파일 종료", command = None)

# 첫 번째 상위 메뉴(이미지)
imageMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label = "영상처리", menu = imageMenu1)

#영상처리 알고리즘
imageMenu1.add_command(label = "동일 영상", command = equalImage)
imageMenu1.add_command(label = "영상 반전", command = reverseImage)
imageMenu1.add_command(label = "영상 밝게/어둡게", command = addImage)

# 두 번째 상위 메뉴(이미지)
imageMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "흑백처리", menu = imageMenu2)

imageMenu2.add_command(label = "동일 영상", command = equalImage)
imageMenu2.add_command(label = "바이트값 조절", command = white_black_byte)
imageMenu2.add_command(label = "평균값 조절", command = white_black_avg)
imageMenu2.add_command(label = "중앙값 조절", command = white_black_Quick_Sort)

# 두 번째 상위 메뉴(기하학 처리)
imageMenu3 = Menu(mainMenu)
mainMenu.add_cascade(label = "기하학처리", menu = imageMenu3)

#영상처리 알고리즘
imageMenu3.add_command(label = "동일 영상", command = equalImage)
imageMenu3.add_command(label = "이동", command = moveImage)
imageMenu3.add_command(label = "축소", command = zoomOutImage)
imageMenu3.add_command(label = "확대", command = zoomInImage)
imageMenu3.add_command(label = "회전", command = rotateImage)

window.mainloop()