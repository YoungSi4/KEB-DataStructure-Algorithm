## 재귀 응용예제 01
## 진수 변환하기

## 함수 선언 부분 ##
# def notation(base, n):
#     if n < base :
#         print(number_char[n], end =' ')
#     else :
#         notation(base, n // base)
#         print(number_char[n % base], end =' ')
#
# ## 전역 변수 선언 부분 ##
# number_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# number_char += ['A', 'B', 'C', 'D', 'E', 'F']
#
# ## 메인 코드 부분 ##
# number = int(input('10진수 입력 -->'))
# print('\n 2진수 : ', end = ' ')
# notation(2, number)
# print('\n 8진수 : ', end = ' ')
# notation(8, number)
# print('\n16진수 : ', end = ' ')
# notation(16, number)


"""
---------------------------------------------------------
"""


## 응용예제 02
## 시에르핀스키 삼각형 그리기

from tkinter import *
def drawTriangle(x, y, size) :
    if size >= 30 :
        drawTriangle(x, y, size/2)				# 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2, y, size / 2)			# 오른쪽 아래 작은 삼각형
        drawTriangle(x + size / 4, int(y-size*(3**0.5)/4), size / 2)	# 위쪽 작은 삼각형
    else :
        canvas.create_polygon (x, y, x + size, y, x + size / 2, y - size*(3 ** 0.5) / 2, fill = 'red', outline = "red")


## 전역 변수
wSize = 1000
radius = 400

## 메인 코드
if __name__ == "__main__":
    window = Tk()
    window.title("삼각형 프렉탈")
    canvas = Canvas(window, height = wSize, width = wSize)

    drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

    canvas.pack()
    window.mainloop()
