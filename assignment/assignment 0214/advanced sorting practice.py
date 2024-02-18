## 고급 정렬 응용문제 01
## 선택 정렬과 퀵 정렬의 성능 비교하기

# import random
# import time
#
# def selection_sort(datalist):
#     selection_list = datalist[:]
#
#     for i in range(len(selection_list)):
#         for j in range(i+1, len((selection_list))):
#             if selection_list[i] > selection_list[j]:
#                 selection_list[i], selection_list[j] = selection_list[j], selection_list[i]
#
#     return selection_list
#
# def quick_sort(datalist):
#     # print(f"정렬 전 {datalist}")
#     if len(datalist) <= 1:
#         return datalist
#     start = 0
#     end = len(datalist) - 1
#
#     high, low = end, start
#     pivot = datalist[(high + low)//2]
#     while low <= high:
#         while datalist[low] < pivot:
#             low += 1
#         while datalist[high] > pivot:
#             high -= 1
#         if low <= high:
#             datalist[low], datalist[high] = datalist[high], datalist[low]
#             low, high = low + 1, high - 1
#
#     mid = low
#     # print(f"정렬 후 {datalist}")
#     return quick_sort(datalist[start:mid]) + quick_sort((datalist[mid:end+1]))
#
#
# ## 전역 변수 생성
# n = int(input("## 데이터의 수: "))
# list_for_exp = [random.randint(1,10000) for _ in range(n)]
# # print(list_for_exp)
#
# selection_start_time = time.time()
# selection = selection_sort(list_for_exp)
# selection_end_time = time.time() - selection_start_time
# print(f"선택 정렬 결과 --> {selection}")
# print(f"선택 정렬 시간 --> {selection_end_time}")
#
# quick_start_time = time.time()
# quick = quick_sort(list_for_exp)
# quick_end_time = time.time() - quick_start_time
# print(f"  퀵 정렬 결과 --> {quick}")
# print(f"  퀵 정렬 시간 --> {quick_end_time}")