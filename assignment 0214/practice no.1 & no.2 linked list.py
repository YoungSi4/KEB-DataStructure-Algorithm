## 1부터 100까지의 숫자로 링크드 리스트를 만들고
## 그 리스트의 노드를 모두 출력해보세요

import random

## 링크드 리스트 노드 선언부
def print_Nodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

##  insert_Node 함수를 만들어서 추가할 수 있게 구현.
## 나중에 for로 number_Array의 값을 data에 받아서 넣어주면 된다.
## 생성시킨 후 print_Node 함수로 모두 출력한다.

## 전역변수 선언부
number_Array = [random.randint(1,100) for num in range(5)]
current, pre, head = None, None, None


