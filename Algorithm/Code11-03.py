## 함수 선언부
def selectionSort(ary) :
    n = len(ary) #4개
    for i in range(0, n-1) : #사이클 (큰 반복 3회)
        minIdx = i
        for k in range(i+1, n) :
            if(ary[minIdx] > ary[k]) :
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return  ary

## 전역 변수부
import random
dataAry = [random.randint(50, 190) for _ in range(8)]

##  메인 코드부
print(('정렬전-->', dataAry))
dataAry = selectionSort(dataAry)
print('정렬후-->', dataAry)

# 정렬에 있어서 외우면 좋은 코드!