import random as rand

#array

#parameter
arr = []
#Function

#Main Code

#array initial
for i in range(10):
    arr.append(0) #배열의 초기화는 append() 함수 쓰기

##배열에 값 대입, 2부터 짝수 대입##

#i는 배열의 첨자로만 사용하는 것을 권장
for i in range(len(arr)):
    #arr[i] = (i+1) * 2
    #arr[i] = num
    #num += 2

    arr[i] = rand.randint(0, 1000)

print(arr)

#배열 합계
total = 0
for i in range(len(arr)):
    total += arr[i]
print(total)

#홀수 배열만 함계
odd_total = 0
for i in range(len(arr)):
    if(arr[i] %2 == 1):
        odd_total += arr[i]
    else:
        continue

print(odd_total)