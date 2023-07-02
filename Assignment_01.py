import math
import os
from tkinter import *
from tkinter import messagebox

def displayImage() :
    global window, canvas, paper, height, width, filename

    if (canvas != None):
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')


    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))

    canvas.pack()

def reverseImage():
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]
    displayImage()

def RightImage():
    for i in range(height):
        for k in range(width):
            if(image[i][k] + 50 > 255):
                image[i][k] = 255
            else:
                image[i][k] += 50
    displayImage()

def DarkImage():
    for i in range(height):
        for k in range(width):
            if (image[i][k] - 100 < 0):
                image[i][k] = 0
            else:
                image[i][k] -= 100
    displayImage()

def whiteBlackImage_avg():
    hap = 0
    avg = 0 #참조오류때문에 사용하는 것이 좋다.
    for i in range(height):
         for k in range(width):
             hap += image[i][k]
    avg = hap / (height * width)

    for i in range(height):
        for k in range(width):
            if (image[i][k] >= avg):
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()

def whiteBlackImage_byte():
    for i in range(height):
        for k in range(width):
            if (image[i][k] >= 128):  # 128이든, 127이든 상관 없다.
                image[i][k] = 255
            else:
                image[i][k] = 0
    displayImage()


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


def whiteBlackImage_Quick_Sort():
    sort = []
    for i in range(height):
        for k in range(width):
            sort.append(image[i][k])

    result = Quick_Sort(sort)
    index = len(result) // 2

    for i in range(height):
        for k in range(width):
            if (image[i][k] >= result[index]):
                image[i][k] = 255
            else:
                image[i][k] = 0

    displayImage()

#     original_image = PhotoImage()
#     image_viewer = Label(window, image=original_image)
#     image_viewer.pack()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('512x512')
window.title('영상처리 Alpha')
btn_1 = Button(window, text="반전", command = reverseImage)
btn_1.pack()
btn_2 = Button(window, text="밝게", command = RightImage)
btn_2.pack()
btn_3 = Button(window, text="어둡게", command = DarkImage)
btn_3.pack()
btn_4 = Button(window, text="흑백(127)", command = whiteBlackImage_byte)
btn_4.pack()
btn_5 = Button(window, text="흑백(평균)", command = whiteBlackImage_avg)
btn_5.pack()
btn_6 = Button(window, text="흑백(sort)", command = whiteBlackImage_Quick_Sort)
btn_6.pack()
# btn_destroy = Button(window, text="초기화", command=initialize_image)
# btn_destroy.pack()

filename = 'Etc_Raw(squre)/assignment.raw'
# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()
displayImage() # 이걸 해야지 처음에 이미지가 출력된다.
window.mainloop()