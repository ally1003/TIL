## 클래스 또는 함수 선언부

class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
    current = node1
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

## 전역 변수부
memory = []
head, current, pre = None, None, None
import random
dataArry = [random.randint(1000,9999) for _ in range(20)]

## 메인 코드부
if __name__ == '__main__' : # C, Java, C++, c# ==> main() 함수

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] : # ['정연', ' 쯔위', '사나','지효']
        pre = node
        node = Node()
        node.data = node # 정연, 쯔위...
        pre.link = node
        memory.append(node)

    printNodes(head)