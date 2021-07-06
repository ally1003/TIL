# 기본 정렬 알고리즘

## 최솟값을 찾는 방법

def findMinIdx(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx]> ary[i]) :
            minIdx = i
    return minIdx

testAry = [55, 88, 33 ,77]
minPos = findMinIdx(testAry)
print('최솟값 -->', testAry[minPos])


def findMinIdx(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

testAry = [66, 78,90,2,4]
minPos = findMinIdx(testAry)
print('최솟값 self ==>', testAry[minPos])