## 원형 연결 리스트 응용예제 01
## 현재 위치부터 가까운 편의점 관리하기

# import random
#
# ## 함수 선언, 구현부
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
# def circular_linked_list(data):
#     global head, current # 글로벌 변수. 현재 위치 바로 뒤에 삽입만 하면 되기 때문에 전역 변수로 기억해둠.
#                           # 이걸 지역변수로 하면 함수가 return하면 스택메모리에서 회수되기 때문에 안 됨.
#     node = Node()
#     node.data = data
#
#     if head is None: #헤드가 없으면 초기화
#         head, current = node, node
#         current.link = node
#         return
#     current.link = node
#     current = current.link
#     node.link = head
#
# def distance(data):
#     """
#     좌표값을 입력 받아서 (0, 0)부터 거리를 구하여 반환
#     :param x: integer
#     :param y: integer
#     :return: float
#     """
#
#     calc_distance = ((data[1] ** 2) + (data[2] ** 2)) ** (1/2)
#     return calc_distance
#
# ## 전역변수 선언부
# current, head, last = None, None, None
# convenient_datalist = [(ord('A')+i, random.randint(1, 100), random.randint(1, 100)) for i in range(10)]
#
# ## 메인 함수
# if __name__ == "__main__":
#     i = 0
#     for data in convenient_datalist:
#         print(f'{chr(65+i)} 편의점, 거리: {distance(data)}')
#         i += 1


"""
-------------------------------------------------------------------
"""

## 응용예제 2
## 이중 연결 리스트 구현하기 (데크?)


# class Node():
#     def __init__(self):
#         self.data = None
#         self.rightlink = None
#         self.leftlink = None
#
# def print_nodes(start):
#     global last
#     current = start
#     if current is None:
#         return
#     print(current.data, end = ' ')
#     while current.rightlink is not None:
#         current = current.rightlink
#         last = current
#         print(current.data, end = ' ')
#     print()
#
# def print_nodes_reverse():
#     global last
#     current = last
#     if current is None:
#         return
#     print(current.data, end=' ')
#     while current.leftlink is not None:
#         current = current.leftlink
#         print(current.data, end=' ')
#     print()
#
# def double_linked_list(data):
#     global head, previous, current, last
#     node = Node()
#     node.data = data
#
#     if head is None: #헤드가 없으면 초기화
#         head, current = node, node
#         return
#     current.rightlink = node
#     previous = current
#     current = current.rightlink
#     current.leftlink = previous
#
# ## 전역 함수 선언부
# current, previous, head, last = None, None, None, None
# member_list = ['다현', '정현', '쯔위', '사나', '지효']
#
# ## 메인 함수
# if __name__ == "__main__":
#     for data in member_list:
#         double_linked_list(data)
#     print("정방향-->", end=" ")
#     print_nodes(head)
#     print("역방향-->", end=" ")
#     print_nodes_reverse()
