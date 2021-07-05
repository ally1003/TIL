katok = ['다현', '정연', '쯔위', ' 사나', '지효']

def delete_data(poition) :
    kLen = len(katok)
    katok[poition] = None

    for i in range(poition+1, kLen, 1) :
        katok[i-1] = katok[1]
        katok[i] = None

    del(katok[kLen-1])

delete_data(1)
print(katok)
delete_data(3)
print(katok)