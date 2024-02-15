"""
    stack 연습문제 1번.
    괄호의 짝이 맞는지 확인하는 프로그램을 확장해
    중괄호 {} 의 짝도 확인할 수 있도록`
"""


## 함수 선언 & 정의부

# push와 pop은 append와 pop을 이용하겠음.

def check_Bracket(phrase) -> bool:
    """
    스택을 활용해 괄호 짝을 검사하는 함수
    :param phrase: string
    :return: bool
    """

    # 지역변수 선언
    stack = list()
    datatable = {'(': ')', '{': '}', '[': ']', '<': '>'}

    for word in phrase:
        if word in datatable.keys():
            stack.append(word)
        elif word in datatable.values():
            if



## 메인 함수
if __name__ == "__main__":
    expresion = input("괄호 검사 (){}[]<>: ")
    print(check_Bracket(expresion))



"""
    stack 연습문제 2번.
    O(1) 의 상수 시간으로 푸시, 팝, 스택의 가장 큰 요소를
    탐색할 수 있는 최대 스택을 설계해보세요
"""

