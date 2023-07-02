print("Hello world!")

#IF문

num = 100
if (num>=100):
    print("It is over than 100 or same.")
elif (num >= 50):
    print("It is over than 50 or same")
else:
    print("It is lower than 50.")

#For문

hap = 0
for i in range(1, 101, 1): #1부터 100까지 1씩 증가하면서 반복하여라.
    hap += i

print(hap)

#QUIZ

i= 1
result = 0
while (i<=100): #괄호는 꼭 써라..
    result += i
    i += 1

print(result)


#Function Declare
def addNumber(n1, n2):

    #global Parameter
    total = 0

    #Main Code
    for i in range(n1, n2+1, 1):
        total += i
    return total

result_2 = addNumber(1, 10)
print(result_2)