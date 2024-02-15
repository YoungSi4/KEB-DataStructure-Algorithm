











"""
    stack 연습문제 1번.
    괄호의 짝이 맞는지 확인하는 프로그램을 확장해
    중괄호 {} 의 짝도 확인할 수 있도록`
"""


## 함수 선언 & 정의부

## push와 pop은 append와 pop을 이용하겠음.


# def check_Bracket(phrase) -> bool:
#     """
#     스택을 활용해 괄호 짝을 검사하는 함수
#     :param phrase: string
#     :return: bool
#     """
#
#     # 지역변수 선언
#     stack = list() # 여는 괄호를 받아서 저장, 닫는 괄호를 만나면 pop으로 꺼내면서 지우고 대조
#     datatable = {')': '(', '}': '{', ']': '[', '>': '<'}
#
#     for word in phrase:
#         if word in datatable.values():
#             stack.append(word)
#         elif word in datatable.keys():
#             if not stack or datatable[word] != stack.pop():
#                 return False
#     return len(stack) == 0
#
# ## 메인 함수
# if __name__ == "__main__":
#     expresion = input("괄호 검사 (){}[]<>: ")
#     print(check_Bracket(expresion))



