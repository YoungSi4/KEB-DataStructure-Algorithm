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

# ## 원 프렉탈 코드 - 10-13 가져옴
#
# from tkinter import *
#
# ## 함수 선언 부분 ##
# def drawCircle(x, y, r) :
# 	global count
# 	count += 1
# 	canvas.create_oval(x-r, y-r, x+r, y+r)
# 	canvas.create_text(x, y-r, text=str(count), font=('', 30))
# 	if r >= radius/2 :
# 		drawCircle(x-r//2, y, r//2)
# 		drawCircle(x+r//2, y, r//2)
#
# ## 전역 변수 선언 부분 ##
# count = 0
# wSize = 1000
# radius = 400
#
# ## 메인 코드 부분 ##
# window = Tk()
# canvas = Canvas(window, height=wSize, width=wSize, bg='white')
#
# drawCircle(wSize//2, wSize//2, radius)
#
# canvas.pack()
# window.mainloop()


"""
---------------------------------------------------------------------------------------------------
"""


## 정렬 - 선택 정렬

## 함수 선언 부분
# def selection_Sort(ary):
#     n = len(ary)
#
#     for i in range(0, n - 1):
#         min_Idx = i
#         for k in range(i + 1, n):
#             if (ary[min_Idx] > ary[k]):
#                 min_Idx = k
#         ary[i], ary[min_Idx] = ary[min_Idx], ary[i]
#     return ary
#
#
# ## 전역 변수 선언 부분
# data_Ary = [188, 162, 168, 120, 50, 150, 177, 105]
#
# ## 메인 코드 부분
# print('정렬 전 -->', data_Ary)
# data_Ary = selection_Sort(data_Ary)
# print('정렬 후 -->', data_Ary)


## 정렬 - 삽입 정렬 - 코드 11-05
## self - 수정해서 랜덤숫자 생서으 내림차수 정렬 코드 작성

# import random
#
# ## 함수 선언 부분 ##
# def find_Insert_Idx(ary, data):
#     find_Idx = -1			# 초깃값은 없는 위치로
#     for i in range(0, len(ary)) :
#         if ary[i] < data:
#             find_Idx = i
#             break
#     if find_Idx == -1:			# 큰 값을 못찾음 == 제일 마지막 위치
#         return len(ary)
#     else :
#         return find_Idx
#
# ## 전역 변수 선언 부분 ##
# # before = [188, 162, 168, 120, 50, 150, 177, 105] # 원본
# before = [random.randint(0,200) for _ in range(10)] # 추가 문제
# after = []
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', before)
# for i in range(len(before)):
#     data = before[i]
#     insPos = find_Insert_Idx(after, data)
#     after.insert(insPos, data)
# print('정렬 후 -->', after)


## 삽입정렬의 조금 더 공간적으로 효율적인 구조.

# ## 함수 선언 부분 ##
# def insertion_Sort(ary) :
#     n = len(ary)
#     for end in range(1, n) :
#         for cur in range(end, 0, -1) :
#             if ( ary[cur-1] > ary[cur] ) :
#                 ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
#     return ary
#
# ## 전역 변 수 선언 부분 ##
# data_Array = [188, 162, 168, 120, 50, 150, 177, 105]
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', data_Array)
# data_Array = insertion_Sort(data_Array)
# print('정렬 후 -->', data_Array)


## os.walk()를 활용한 파일 출력 정렬 - 코드 11-

# import os
#
# ## 함수 선언 부분 ##
# def makeFileList(folderName) :
# 	fnameAry = []
# 	for dirName, subDirList, fnames in os.walk(folderName):
# 		for fname in fnames:
# 			fnameAry.append(fname)
# 	return fnameAry
#
# def insertionSort(ary) :
# 	n = len(ary)
# 	for end in range(1, n) :
# 		for cur in range(end, 0, -1) :
# 			if (ary[cur-1] < ary[cur]) :
# 				ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
# 	return ary
#
# ## 전역 변수 선언 부분 ##
# fileAry = []
#
# ## 메인 코드 부분 ##
# fileAry = makeFileList('C:/Program Files/Common Files')
# fileAry = insertionSort(fileAry)
# print('파일명 역순 정렬 -->', fileAry)


# ## 버블 정렬
#
# ## 함수 선언 부분 ##
# def bubble_Sort(ary) :
#     n = len(ary)
#     for end in range(n-1, 0, -1) :
#         change_YN = False
#         print('#사이클-->', ary)
#         for cur in range(0, end) :
#             if (ary[cur] > ary[cur+1]) :
#                 ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
#                 change_YN = True
#         if not change_YN : # 앞에서 변화가 없었다면 더이상 탐색하지 않고 탈출
#             break
#     return ary
#
# ## 전역 변수 선언 부분 ##
# dataAry = [50, 105, 120, 188, 150, 162, 168, 177]
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', dataAry)
# dataAry = bubble_Sort(dataAry)
# print('정렬 후 -->', dataAry)



## 퀵 정렬 - 12-03 코드


count = 0
## 함수 선언 부분 ##
# def quickSort(ary):
#     n = len(ary)
#     global count
#
#     if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
#         return ary
#
#     pivot = ary[n // 2]  # 기준값을 중간값으로 지정
#     leftAry, rightAry = [], []
#
#     for num in ary:
#         if num < pivot:
#             leftAry.append(num)
#         elif num > pivot:
#             rightAry.append(num)
#     count += 1
#
#     print(f'{count}번째: 왼쪽-> {leftAry} 피벗-> {[pivot]} 오른쪽-> {rightAry}')
#     return quickSort(leftAry) + [pivot] + quickSort(rightAry)
#
#
# ## 전역 변수 선언 부분 ##
# dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
#
# ## 메인 코드 부분 ##
# print('정렬 전 -->', dataAry)
# dataAry = quickSort(dataAry)
# print('정렬 후 -->', dataAry)

## 12 - 09 고양이

# from tkinter import *
#
# ## 함수 선언 부분 ##
# def qSort(arr, start, end) : # 퀵정렬 함수
#     if end <= start :
#         return
#
#     low = start
#     high = end
#
#     pivot = arr[(low + high) // 2]  # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리한다.
#     while low <= high :
#         while arr[low] < pivot :
#             low += 1
#         while arr[high] > pivot :
#             high -= 1
#         if low <= high :
#             arr[low], arr[high] = arr[high], arr[low]
#             low, high = low + 1, high - 1
#
#     mid = low
#
#     qSort(arr, start, mid-1)
#     qSort(arr, mid, end)
#
# def quickSort(ary) :
#     qSort(ary, 0, len(ary)-1)
#
# ## 메인 코드 부분 ##
# window = Tk()
# window.geometry("600x600")
# photo = PhotoImage(file = 'pet02.gif')
#
# photoAry=[]
# h = photo.height()
# w = photo.width()
# for i in range(h) :
#     for k in range(w) :
#         r, g, b = photo.get(i,k)
#         value = (r + g + b) // 3
#         photoAry.append(value)
#
# dataAry = photoAry[:]
# quickSort(dataAry)
# midValue = dataAry[h*w // 2]
#
# for i in range(len(photoAry)) :
#     if photoAry[i] <= midValue :
#         photoAry[i] = 0
#     else :
#         photoAry[i] = 255
#
# pos = 0
# for i in range(h) :
#     for k in range(w) :
#         r = g = b = photoAry[pos]
#         pos += 1
#         photo.put("#%02x%02x%02x" % (r, g, b), (i, k))
#
# paper = Label(window, image=photo)
# paper.pack(expand=1, anchor = CENTER)
# window.mainloop()
