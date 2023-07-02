from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image #필로우 라이브 중 이미지만 가져온다. (png 가져오는 라이브러리)

import os
import math

##FUCTION DEFINE

### 공통 함수부 ###
def loadImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 파일을 가져오는 것 (그 중 raw 파일만을 가져온다.)
    filename = askopenfilename(parent = window,
                               filetypes=(("Color file", "*.png;*.jpg;*.bmp;*.gif"), ("All file", "*.*")))

   # 압축파일이라 raw file처럼 size를 가져올 수가 없음. - pillow의 도움을 받는다.
    pillow = Image.open(filename)
    inH = pillow.height #(300, 100, 100) 이런식으로 나온다.
    inW = pillow.width

    #컬러 메모리
    inImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]
    pillowRGB = pillow.convert('RGB') #RGB 모델 변경 - 내부적으로 r,g,b모델로 바꾸어준다.

    for i in range(inH):
        for k in range(inW):
            #r, g, b 값을 알려주는 함수 생성
            r, g, b = pillowRGB.getpixel((k, i)) #내부적으로 r, g, b가 변경되어 있기 때문에 원래대로 바꿔준다. (이건 경험으로 겪어라..)
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    equalImage()

def displayImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    if (canvas != None):
        canvas.destroy()

    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal') #중앙점 찾기

    rgbString = ""
    for i in range(outH):
        tmpString = ""
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()

def equalImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]

    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]

    displayImage()

def saveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    filename = asksaveasfile(parent=window, mode='wb', defaultextension=".png",
                             filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")))

    newOutImage = Image.new('RGB', (outW, outH)) #새로운 RGB 이미지를 만들어준다.

    #이 이미지에 각각 자리에 r, g, b 값과 숫자를 넣어준다.
    for i in range(outH):
        for k in range(outW):
            r = outImage[0][i][k]
            g = outImage[1][i][k]
            b = outImage[2][i][k]
            newOutImage.putpixel((k, i), (r, g, b)) #r, g, b를 각각 픽셀 숫자에 넣어준다.

    newOutImage.save(filename.name) # 파일 저장
    messagebox.showinfo('저장', filename.name + '   Save Success!!')

def exitImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    window.destroy()
    

### 영상처리 함수부(핵심 함수) ###

##흑백처리를 위해 grayscale로 바꿔주기
def grayscaleImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(inW)] for _ in range(inH)] for _ in range(3)]

    for i in range(inH):
        for k in range(inW):
            hap = inImage[0][i][k] + inImage[1][i][k] + inImage[2][i][k] #rgb 모든 값을 다 더해준다.
            outImage[0][i][k] = outImage[1][i][k] = outImage[2][i][k] = hap // 3

    return outImage

## 화소점 처리 - 이미지 반전
def reserveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    for i in range(inH):
        for k in range(inW):
            outImage[0][i][k] = 255 - inImage[0][i][k]
            outImage[1][i][k] = 255 - inImage[1][i][k]
            outImage[2][i][k] = 255 - inImage[2][i][k]

    displayImage()

## 화소점 처리 - 퀵 정렬을 사용하여 이미지 흑백 처리
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
    grayImage = grayscaleImage()
    sort = []

    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                sort.append(grayImage[rgb][i][k])

    result = Quick_Sort(sort)
    index = len(result) // 2

    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (grayImage[rgb][i][k] >= result[index]):
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = 0

    displayImage()

## 화소점 처리 - 이미지 감마
#def gammaImage:

## 기하학 처리 - 영상 이동
def moveImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    x_Val = askinteger("X축 값", "")
    y_Val = askinteger("Y축 값", "")

    # 외부에 접근하는 것이기 때문에 프로그램이 죽을 수 밖에 없음, 그렇기 때문에 먼저 위치를 확인을 하고, 위치가 없음 버려야한다. (if문)
    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                if (0 <= i + x_Val < outH) and (0 <= k + y_Val < outW):
                    outImage[rgb][i + x_Val][k + y_Val] = inImage[rgb][i][k]

    displayImage()


## 기하학 처리 - 영상 회전
def rotateImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    #메모리 할당은 동일하게 하기
    outH = inH
    outW = inW
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    angle = askinteger("각도", "각도를 입력하세요.")
    radian = angle * math.pi / 180.0 #삼각함수가 프로그램에서는 라디안용이기 때문에 변경해줘야 한다.

    #홀문제 해결 (백워딩)
    cx = inH //2
    cy = inW //2

    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                oldI = int(math.cos(radian) * (i - cx) + math.sin(radian) * (k - cy)) + cx #문제를 해결하기 위해 빼줬던 만큼 다시 더해준다.
                oldK = int(-math.sin(radian) * (i - cx) + math.cos(radian) * (k - cy)) + cy

                if (0 <= oldI < inH) and (0 <= oldK < inW):
                    outImage[rgb][i][k] = inImage[rgb][oldI][oldK]

    displayImage()

## 기하학 처리 - 영상 축소
def zoomOutImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("축소 배율", "몇 배 축소할 것 인가요?")

    #포워딩 기법
    outH = inH // scale
    outW = inW // scale
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    for rgb in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i//scale][k//scale] = inImage[rgb][i][k]

    displayImage()

## 기하학 처리 - 영상 확대
def zoomInImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    scale = askinteger("확대 배율", "몇 배 확대할 것 인가요?")

    #백워딩 기법
    outH = int(inH * scale)
    outW = int(inW * scale)
    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]

    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = inImage[rgb][i//scale][k//scale] #홀 잡아준다. - 어차피 반올림한 값임
    displayImage()

def gammaImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    gamma = askfloat("감마 값", "감마 값을 입력해주세요.")

    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = int(math.pow(inImage[rgb][i][k]/255, gamma) * 255)
    displayImage()

def parabolicImage():
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW

    outImage = [[[0 for _ in range(outW)] for _ in range(outH)] for _ in range(3)]
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = int(255 * math.pow((inImage[rgb][i][k] / 127) - 1, 2))
                if (outImage[rgb][i][k] > 255):
                    outImage[rgb][i][k] = 255
    displayImage()
    
##PARAMETER
inImage = outImage = [] #배열로 해줘도 아~무 상관없음!
#InImage = OutImage = None
inH, inW, OutH, OutW = 0, 0, 0, 0
window, canvas, paper = None, None, None
filename = ""

##MAIN CODE

window = Tk()
window.geometry('300x300')
window.title('Color Image Processing (GUI)')

mainMenu = Menu(window) #메뉴의 틀
window.config(menu = mainMenu) #위에 메뉴바를 생성하기

# 상위 메뉴(파일)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu) #파일 확장되는 것

fileMenu.add_command(label = "파일 열기", command = loadImage) #파일 열기 - 명령어 실행 (파일 메뉴의 하단 메뉴?)
fileMenu.add_command(label = "파일 저장", command = saveImage)
fileMenu.add_separator() #종료 전에 굵은 선? 처럼 나타난다.
fileMenu.add_command(label = "파일 종료", command = exitImage)

# 첫 번째 상위 메뉴(이미지)
imageMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label = "화소점 처리", menu = imageMenu1)

#영상처리 알고리즘
imageMenu1.add_command(label = "동일 영상", command = equalImage)
imageMenu1.add_command(label = "영상 반전", command = reserveImage)
imageMenu1.add_command(label = "영상 흑백 처리", command = white_black_Quick_Sort)
imageMenu1.add_command(label = "영상 감마 처리", command = gammaImage)
imageMenu1.add_command(label = "영상 파라볼라 처리(CAP)", command = parabolicImage)

# 두 번째 상위 메뉴(이미지)
imageMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "기하학 처리", menu = imageMenu2)

imageMenu2.add_command(label = "동일 영상", command = equalImage)
imageMenu2.add_command(label = "영상 이동", command = moveImage)
imageMenu2.add_command(label = "영상 회전", command = rotateImage)
imageMenu2.add_command(label = "영상 축소", command = zoomOutImage)
imageMenu2.add_command(label = "영상 확대", command = zoomInImage)

window.mainloop()
