## 1부터 100까지의 숫자로 링크드 리스트를 만들고
## 그 리스트의 노드를 모두 출력해보세요

import random

## 링크드 리스트 노드 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None

## 함수 선언 & 정의부
def linked_list_generator():
    for data in [random.randint(1,100) for num in range(5)]:





## 전역변수
current, pre, head = None, None, None

