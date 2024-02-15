## 선형 리스트 응용예제 1번
## 카톡 친구 자동 삽입하기

## 추가할 친구 이름, 카톡 횟수를 입력 받고 연락 횟수 내림차순으로 정렬
## 동일한 연락 횟수라면 새로운 친구를 앞 순위로 지정한다.

## 함수 선언 및 정의

# def find_insert_Place(chat_time):
#     """
#     튜플 형태의 자료를 받아서 기존 리스트에 삽입하는 함수
#     :param chat_time: tuple, len: 2, (str, int)
#     :return: 없음
#     """
#     global friend_list
#
#     for i in range(len(friend_list) - 1):
#         if chat_time[1] >= friend_list[i][1]:
#             friend_list.insert(i, chat_time)
#
# ## 전역변수 선언
# friend_list = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
#
#
# ## 메인 함수
# if __name__ == "__main__":
#     name = input("추가할 친구--> ")
#     times = int(input("카톡 횟수--> "))
#     new_data = (name, times)
#     find_insert_Place(new_data)
#     print(friend_list)


"""
-----------------------------------------------------------
"""


## 선형 리스트 응용예제 2번
## 2차원 배열 활용하기

## 함수 선언 부분 ##
# def print_Poly(tx_px):
#     poly_Str = "P(x) = "
#
#     for i in range(len(tx_px)):
#         term = tx_px[i][0]  # 항 차수
#         coef = tx_px[i][1]  # 계수
#
#         if (coef >= 0):
#             poly_Str += "+"
#         poly_Str += str(coef) + "x^" + str(term) + " "
#
#     return poly_Str
#
#
# def calculation_Poly(xVal, tx_px):
#     retValue = 0
#
#     for i in range(len(tx_px)):
#         term = tx_px[i][0]  # 항 차수
#         coef = tx_px[i][1]  # 계수
#         retValue += coef * (xVal ** term)
#
#     return retValue
#
#
# ## 전역 변수 선언 부분 ##
# # tx = [300, 20, 0]
# # px = [7, -4, 5]
# # 이걸 이중 배열로 바꾸고 이전과 동일한 결과가 나오도록 코드를 바꾸자.
# txpx = [[300, 7], [20, -4], [0, 5]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     pStr = print_Poly(txpx)
#     print(pStr)
#
#     xValue = int(input("X 값--> "))
#
#     pxValue = calculation_Poly(xValue, txpx)
#     print(pxValue)


"""
-----------------------------------------------------------
"""

# 책 교제 문제

## 음이 아닌 정수로 구성되어 있는 배열 an_array에서
##짝수만 추출한 배열과 홀수만 추출한 배열을 만들어보세요

## 전역변수 선언
# odd_array = []
# even_array = []
# an_array = [1, 2, 3, 4, 5, 6]
#
# def extract(datas):
#     for data in datas:
#         if data % 2 == 0:
#             even_array.append(data)
#         else:
#             odd_array.append(data)
#
# if __name__ == "__main__":
#     extract(an_array) ## 파이썬에서 mutable은 call by ref로 상호작용 한다.
#
#     print(f"원래 리스트: {an_array}")
#     print(f"홀수 리스트: {odd_array}")
#     print(f"짝수 리스트: {even_array}")
