## 단순 연결 리스트 응용예제 1번
## 사용자가 이름과 이메일을 입력하면 이메일 순서대로 단순 연결 리스트를 생성하는 프로그램을 작성
## 이름에서 enter를 입력하면 종료한다.

# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
# def print_nodes(start):
#     current = start # 지역변수 current. 링크를 처음부터 끝까지 순회하며 출력하기 위함
#     if current is None:
#         return
#     print(current.data, end = ' ')
#     while current.link is not None:
#         current = current.link
#         print(current.data, end = ' ')
#     print()
#
# def linked_list(data):
#     global head, current # 글로벌 변수. 현재 위치 바로 뒤에 삽입만 하면 되기 때문에 전역 변수로 기억해둠.
#                           # 이걸 지역변수로 하면 함수가 return하면 스택메모리에서 회수되기 때문에 안 됨.
#     node = Node()
#     node.data = data
#
#     if head is None: #헤드가 없으면 초기화
#         head, current = node, node
#         return
#     current.link = node
#     current = current.link
#
# ## 전역 함수 선언부
# current, head = None, None
#
# ## 메인 함수
# if __name__ == "__main__":
#     while True:
#         name = input("이름--> ")
#         if name == '':
#             break
#         mail = input("이메일--> ")
#
#         idenfication_data = [name, mail]
#         linked_list(idenfication_data)
#         print_nodes(head)

"""
-----------------------------------------------------------
"""

# ## 단순 연결 리스트 응용예제 2번
# ## 로또 추첨하기

# # 모듈 import
# import random
#
# ## 함수 선언
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
# def print_nodes(start):
#     current = start
#     if current is None:
#         return
#     print(current.data, end = ' ')
#     while current.link is not None:
#         current = current.link
#         print(current.data, end = ' ')
#     print()
#
# def linked_list(data):
#     global head, current
#     node = Node()
#     node.data = data
#
#     if head is None: #헤드가 없으면 초기화
#         head, current = node, node
#         return
#     current.link = node
#     current = current.link
#
# ## 전역변수 선언
# head, current = None, None
#
# ## 메인 함수
# if __name__ == "__main__":
#     lotto_numbers = [random.randint(1, 45) for _ in range(6)]
#     for lotto_number in lotto_numbers:
#         linked_list(lotto_number)
#     print_nodes(head)


"""
-----------------------------------------------------------
"""

# 이 아래는 pdf가 아니라 교재의 마지막 문제들

## 1부터 100까지의 숫자로 링크드 리스트를 만들고
## 그 리스트의 노드를 모두 출력해보세요

# import random
#
# ## 링크드 리스트 노드 선언부
# def print_Nodes(start):
#     current = start
#     if current.link == None:
#         return
#     print(current.data, end=' ')
#     while current.link != start:
#         current = current.link
#         print(current.data, end=' ')
#     print()
#
# ##  insert_Node 함수를 만들어서 추가할 수 있게 구현.
# ## 나중에 for로 number_Array의 값을 data에 받아서 넣어주면 된다.
# ## 생성시킨 후 print_Node 함수로 모두 출력한다.
# ## 나중에 한 번 복습하고 만들자...
#
# ## 전역변수 선언부
# number_Array = [random.randint(1,100) for num in range(5)]
# current, pre, head = None, None, None



## 하나는 사이클이 있고 하나는 없는 두 개의 링크드 리스트 생성
## 두 리스트에 모두 사이클을 찾는 detect_cycle 메서드가 있어야 한다. 각 리스트에서 해당 함수를 호출하세요