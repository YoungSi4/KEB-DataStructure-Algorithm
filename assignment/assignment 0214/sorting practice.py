## 정렬 응용문제 01
## 성적별로 조 편성하기

# def insert_sort(datalist)->list:
#     """
#     삽입정렬을 통해 받은 매개변수를 오름차순으로 정렬해주는 함수
#     :param datalist: list[][]
#     :return: list[][]
#     """
#     for end in range(1, len(datalist)):
#       for current in range(end, 0, -1):
#           if datalist[current-1][1] > datalist[current][1]:
#               datalist[current-1], datalist[current] = datalist[current], datalist[current-1]
#     return datalist
#
# def pairing(datalist):
#     """
#     datalist를 받아서 조 편셩을 출력해주는 함수
#     :param datalist: list[][]
#     :return: 없음
#     """
#     print("## 성적별 조 편성표 ##")
#     for pair in range(len(datalist)//2):
#         print(f'{datalist[pair][0]} : {datalist[len(datalist)-pair-1][0]}')
#     if len(datalist) % 2 != 0:
#         print(f'{datalist[len(datalist)//2+1][0]}은(는) 혼자입니다.')
#
# ## 전역 변수
# students_array = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 79], ['영웅', 67], ['민호', 92], ['영배', 59]]
#
# ## 메인 함수
# if __name__ == "__main__":
#     print(f"정렬 전--> {students_array}")
#     print(f'정렬 후--> {insert_sort(students_array)}')
#     pairing(students_array)

"""
------------------------------------------------------------------------------------
"""


## 응용예제 02
## 2차원 배열의 중앙값 찾기

## 정렬 알고리즘은 위에서 사용한 삽입 정렬을 수정하여 이용하겠음

# def make_flat(datalist)-> list:
#     """
#     2차원 리스트를 1차원으로 평평하게 펴주는 함수
#     :param datalist: list[][]
#     :return: list[]
#     """
#
#     linear_array = []
#
#     for row in range(len(datalist)):
#         for col in range(len(datalist[row])):
#             linear_array.append(datalist[row][col])
#     return linear_array
#
# def insert_sort(datalist)->list:
#     """
#     삽입정렬을 통해 받은 매개변수를 오름차순으로 정렬해주는 함수
#     :param datalist: list[]
#     :return: list[]
#     """
#     for end in range(1, len(datalist)):
#       for current in range(end, 0, -1):
#           if datalist[current-1] > datalist[current]:
#               datalist[current-1], datalist[current] = datalist[current], datalist[current-1]
#     return datalist
#
# ## 전역변수 설정
# square_array = [[55, 33, 250, 44], [88, 1, 76, 23], [199, 222, 38, 47], [155, 145, 20, 99]]
#
# ## 메인 함수
# if __name__ == "__main__":
#     print(f'1차원 변경 전, 정렬 전--> {square_array}')
#     linear_list = make_flat(square_array)
#     print(f"1차원 변경 후, 정렬 전--> {linear_list}")
#     insert_sort(linear_list)
#     print(f"1차원 변경 후, 정렬 후--> {linear_list}")
#
#     print(f'중앙값--> {linear_list[len(linear_list)//2]}')
