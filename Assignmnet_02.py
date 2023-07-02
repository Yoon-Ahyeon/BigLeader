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

def degree_90():
    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]

            paper.put('#%02x%02x%02x' % (r, g, b), (len(image)-1-i, k))
    canvas.pack()

def degree_180():
    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (len(image) - 1 - k, len(image) - 1 - i))
    canvas.pack()
def degree_270():
    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (i, len(image) - 1 - k))
    canvas.pack()

def left_right():
    for i in range(height):
        for k in range(width):
            r = g = b = image[i][width-1-k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    canvas.pack()

def top_bottom() :
    for i in range(height):
        for k in range(width):
            r = g = b = image[height-1-i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k,i))
    canvas.pack()

## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []


## 메인
window = Tk()
window.geometry('512x512')
window.title('영상처리 Alpha')
btn_1 = Button(window, text="90도 회전", command = degree_90)
btn_1.pack()
btn_2 = Button(window, text="180도 회전", command = degree_180)
btn_2.pack()
btn_3 = Button(window, text="270도 회전", command = degree_270)
btn_3.pack()
btn_4 = Button(window, text="좌우반전", command = left_right)
btn_4.pack()
btn_5 = Button(window, text="상하반전", command = top_bottom)
btn_5.pack()

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