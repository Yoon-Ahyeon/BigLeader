#Image Processing

from tkinter import *
from tkinter import messagebox

import os
import math

##Function
def displayImage(): #red, blue, green을 모두 표현해야하지만, 우리는 정보가 1개밖에 없기 때문에 grayscale이 된다.
    for i in range(height):
        for k in range(width):
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (i, k))#16진수로 표시하여 rgb를 찍어주겠다. i, k 위치에 rgb를 찍겠다.

##Parameter
window, canvas, paper = None, None, None #벽, 칠판(왠만한건 가능, 선, 동그라미, 등),점을 그리기 위한 종이
filename = ""
height, width = 0, 0
image = [] #배열


##Main
window = Tk() #대소문자 가림
window.geometry('300x300') #윈도우 창 크기 조절
window.title("Image Processing_version Alpha") #제목

#canvas, paper 정의
canvas = Canvas(window, height = 256, width = 256) #그림이 256이라서 ..
paper = PhotoImage(height= 256, width= 256)
canvas.create_image((256/2, 256/2), image=paper, state='normal') #이거는 이해가 필요함 !!

window.mainloop()

#파일 가져오기
filename = 'Etc_Raw(squre)\LENA256.RAW'
fsize = os.path.getsize(filename)
height = width = int(math.sqrt(fsize))
#메모리 확보(영상 크기)
image = [[0 for _ in range(width)] for _ in range(height)] #width X height 배열을 0으로 초기화하는 코드
#파일 - 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height):
    for k in range(width):
        image[i][k] = ord(rfp.read(1)) #숫자로 가져오기 위해서 ord() 사용 (아니면 외래어 나옴)
rfp.close()

displayImage()

canvas.pack()
window.mainloop()

