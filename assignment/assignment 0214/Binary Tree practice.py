## 이진 트리 응용예제 01
## 편의점에서 판매된 물건 목록 출력하기

# import random
#
# class tree_node():
#     def __init__(self):
#         self.data = None
#         self.leftlink = None
#         self.rightlink = None
#
# def bst(sales):
#     global root
#     node = tree_node()
#     node.data = sell_array[0]
#     root = node
#
#     for sale in sales[1:]:
#         node = tree_node()
#         node.data = sale
#
#         current = root
#         while True:
#             if sale == current.data:
#                 break
#             if sale < current.data:
#                 if current.leftlink is None:
#                     current.leftlink = node
#                     break
#                 current = current.leftlink
#             else:
#                 if current.rightlink is None:
#                     current.rightlink = node
#                     break
#                 current = current.rightlink
#
#     print("BST 구성 완료")
#
# def search(node) :
#     if node is None :
#         return
#     print(node.data, end = ' ')
#     search(node.leftlink)
#     search(node.rightlink)
#
# ## 전역변수 선언부
# root = None
# data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라' , '삼각김밥']
# sell_array = [random.choice(data_array) for _ in range(20)]
#
#
#
# if __name__ == "__main__":
#     print(f'오늘 판매된 물건 (중복 O)--> {sell_array}')
#     bst(sell_array)
#     print("오늘 판매된 물건 종류 (증복 X)-->", end=' ')
#     search(root)


"""
---------------------------------------------------------------------------------------------------
"""


## 응용예제 02
## 폴더 및 하위 폴더에 중복된 파일 이름 찾기
## 위의 문제와 동일한 방식을 적용

# import os
#
# class tree_node():
#     def __init__(self):
#         self.data = None
#         self.leftlink = None
#         self.rightlink = None
#
# def bst(file_name):
#     global root
#     node = tree_node()
#     node.data = file_name[0]
#     root = node
#
#     for sale in file_name[1:]:
#         node = tree_node()
#         node.data = sale
#
#         current = root
#         while True:
#             if sale == current.data:
#                 break
#             if sale < current.data:
#                 if current.leftlink is None:
#                     current.leftlink = node
#                     break
#                 current = current.leftlink
#             else:
#                 if current.rightlink is None:
#                     current.rightlink = node
#                     break
#                 current = current.rightlink
#
# def search(node) :
#     if node is None :
#         return
#     print(node.data, end = ' ')
#     search(node.leftlink)
#     search(node.rightlink)
#
# ## 전역 변수 선언 부분
# root = None
# file_name_array = []
#
# ## 메인 함수
# if __name__ == "__main__":
#     folder_name = 'C:/Program Files/Common Files/'
#     for directory_name, sub_directory_list, file_names in os.walk(folder_name) :
#         for fname in file_names :
#             file_name_array.append(fname)
#
#     bst(file_name_array)
#     print(folder_name, '및 그 하위 디렉터리의 중복된 파일 목록 -->')
#     search(root)