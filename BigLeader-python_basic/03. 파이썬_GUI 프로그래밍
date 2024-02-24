#GUI Prgoramming

from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo("제목", "내용")

window = Tk() #대소문자 가림
window.geometry('300x300') #윈도우 창 크기 조절
window.title("여기가 제목") #제목
label1 = Label(window, text='나 글자다.', font=("궁서체", 20))
button1 = Button(window, text='확인', command=clickButton) #함수이름만 작성해야 된다. (괄호 사용 X)

label1.pack() #이거 무조건 써줘야한다.
button1.pack()
window.mainloop()


