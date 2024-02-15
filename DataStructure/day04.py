# ## 재귀 - 회문 10-11코드
#
# ## 함수 선언 부분 ##
# def palindrome(p_Str) :
#     if len(p_Str) <= 1 : # 길이를 체크. 한 글자면 무조건 펠린드롬
#         return True
#
#     if p_Str[0] != p_Str[-1] : # 맨 앞과 맨 뒤를 체크. 둘이 다르면 False 리턴.
#         return False
#
#     return palindrome(p_Str[1:len(p_Str) - 1]) # 원래 문자열을 슬라이싱해서 재귀함수에 넣어버림
#     # ex) 봄봄 > if 2개 지나감 > 슬라이싱 > 빈 리스트 전달 > 맨처음 if에 걸려서 Ture 반환.
#
#
# ## 전역 변수 선언 부분 ##
# str_Array = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번주 주번이 너야", "살금 살금"]
#
# ## 메인 코드 부분 ##
# for test_Str in str_Array :
#     print(test_Str, end ='--> ')
#     test_Str = test_Str.lower().replace(' ', '') ## 전부 소문자 처리하는 함수 + replace 함수로 띄어쓰기 붙임
#     if palindrome(test_Str) :
#         print('O')
#     else :
#         print('X')



"""
---------------------------------------------------------------------------------------------------
"""



# # GUI를 쓰는 피보나치
#
# import tkinter as tk
#
# memo = [0, 1] + [None] * (98)
#
# def fibonachi_memoization(number: int, memo: list) -> int :
#     """
#     피보나치 수를 반환하는 함수
#     :param number: integer number
#     :return: integer number
#     """
#     if memo[number] is not None: # 이미 계산한 내용이면 바로 리턴하자.
#         return memo[number]
#
#     # if number < 2:
#     #     result = number
#     # else:
#     result = fibonachi_memoization(number - 1, memo) + fibonachi_memoization(number - 2, memo)
#     memo[number] = result
#     return result
#
# def process_fibonacci():
#     number = en_input_number.get() # get 함수는 입력 받은 걸 문자열로 리턴해줌
#     lbl_display_fibonacci_result.config(text=f"f{number}! = {fibonachi_memoization(number)}") # config 구성.
#
# if __name__ == "__main__":
#     # Create window object
#     w = tk.Tk()
#     w.geometry("200x150")
#
#     # Create widget
#     lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memoization')
#     en_input_number = tk.Entry(w)
#     btn_click = tk.Button(w, text='Click', command=process_fibonacci) # bind function
#
#     # Layout
#     lbl_display_fibonacci_result.pack()
#     en_input_number.pack(fill='x')
#     btn_click.pack(fill="x")
#
#
#     # maintain window
#     en_input_number.focus() # focus: 입력 콘솔을 바로 생성된 창으로 옮겨주는 함수
#     w.mainloop()
#
# if __name__ == "__main__":
#     n = int(input("how much fibo? : "))
#     print(fibonachi_memoization(n, memo))



"""
---------------------------------------------------------------------------------------------------
"""



## 원 프렉탈 코드 - 10-13 가져옴

from tkinter import *

## 함수 선언 부분 ##
def drawCircle(x, y, r) :
	global count
	count += 1
	canvas.create_oval(x-r, y-r, x+r, y+r)
	canvas.create_text(x, y-r, text=str(count), font=('', 30))
	if r >= radius/2 :
		drawCircle(x-r//2, y, r//2)
		drawCircle(x+r//2, y, r//2)

## 전역 변수 선언 부분 ##
count = 0
wSize = 1000
radius = 400

## 메인 코드 부분 ##
window = Tk()
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()



"""
---------------------------------------------------------------------------------------------------
"""



