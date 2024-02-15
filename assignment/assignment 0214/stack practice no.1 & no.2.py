## 스택 응용문제 01
## 헨젤과 그레텔의 집으로 돌아가기

# import random
#
# ## 전역변수
# stones = ['주황', '초록', '파랑', '보라', '노랑', '빨강', '노랑']
# stack = []
#
# ## 메인 함수
# if __name__ == "__main__":
#     random.shuffle(stones)
#
#     print("과자집에 가는 길: ", end='')
#     for stone in stones:
#         stack.append(stone)
#         print(f"{stone}-->", end='')
#     print('과자집')
#
#     print("우리집에 오는 길: ", end='')
#     for i in range(len(stones)):
#         print(f'{stones.pop()}-->', end='')
#     print('우리집')


"""
_______________________________________________________________
"""


## 응용예제 2
## 파일 내용을 완전히 거꾸로 출력하기

# stack = []
#
# if __name__ == "__main__" :
#
# 	with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp :
# 		line_array = rfp.readlines()
#
# 	print("---------- 원본 ----------")
# 	for line in line_array :
# 		stack.append(line)
# 		print(line, end = ' ')
# 	print()
#
# 	print("------ 거꾸로 처리된 결과 ------")
# 	while True :
# 		line = stack.pop()
# 		if line == None :
# 			break
#
# 		mini_stack = [None for _ in range(len(line))]
# 		mini_top = -1
#
# 		for charact in line :
# 			mini_top += 1
# 			mini_stack[mini_top] = charact
#
# 		while True :
# 			if mini_top == -1 :
# 				break
# 			charact = mini_stack[mini_top]
# 			mini_top -= 1
# 			print(charact, end =' ')


"""
-------------------------------------------------------------
"""


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



