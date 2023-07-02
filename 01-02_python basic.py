##Function
def addFunc(n1, n2):
    print(n1, '+', n2, '=', n1+n2)

def subFunc(n1, n2):
    print(n1, '-', n2, '=', n1-n2)

def mulFunc(n1, n2):
    print(n1, '*', n2, '=', n1*n2)

def divFunc(n1, n2):
    print(n1, '//', n2, '=', n1//n2)

def powFunc(n1, n2):
    print(n1, '**', n2, '=', n1 ** n2)

def restFunc(n1, n2):
    print(n1, '%', n2, '=', n1 % n2)

##Parameter
#num1, num2 = 0, 0 (안써도 잘만 된다. - 안정성 보장을 위해 사용하는걸지도?)

## Main
num1 = int(input("정수를 입력하세요."))
num2 = int(input("정수를 입력하세요."))

addFunc(num1, num2)
subFunc(num1, num2)
mulFunc(num1, num2)
divFunc(num1, num2)
powFunc(num1, num2)
restFunc(num1, num2)

