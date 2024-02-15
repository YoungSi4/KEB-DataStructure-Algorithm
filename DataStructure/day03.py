# # 그래프 주석 이름 - 코드 9-2 가져옴
#
# ## 함수 선언 부분 ##
# class Graph():
#     def __init__ (self, size):
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]
#
# def print_Graph(g):
#     print('  ', end = '  ')
#     for v in range(g.SIZE):
#         print(name_Array[v], end =' ')
#     print()
#     for row in range(g.SIZE):
#         print(name_Array[row], end ='  ')
#         for col in range(g.SIZE):
#             print(g.graph[row][col], end= '   ')
#         print()
#     print()
#
#
# G1 = None
# stack = []
# visitedAry = []		# 방문한 정점
# name_Array = ['A', 'B', 'C', 'D']
#
# ## 메인 코드 부분 ##
# G1 = Graph(4)
# G1.graph[0][2] = 1; G1.graph[0][3] = 1
# G1.graph[1][2] = 1
# G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
# G1.graph[3][0] = 1; G1.graph[3][2] = 1
#
# # 라벨 코드 잃어버렸어
# print('## G1 무방향 그래프 ##')
# for row in range(4) :
#     for col in range(4) :
#         print(G1.graph[row][col], end = ' ')
#     print()
#
# current = 0		# 시작 정점 A
# stack.append(current)
# visitedAry.append(current)
#
# while len(stack) != 0: # 스택이 빌 때까지 반복 == 탐색 종료
#     next = None
#     for vertex in range(G1.SIZE):
#         if G1.graph[current][vertex] == 1: # 연결 되어 있는지 여부 확인
#             if vertex in visitedAry:  	   # 방문한 적이 있는 정점이면 탈락
#                 pass
#             else: 			   # 방문한 적이 없으면 다음 정점으로 지정
#                 next = vertex
#                 break
#
#     if next is not None:			  	# 다음에 방문할 정점이 있는 경우
#         current = next                  # 해당 정점으로 이동
#         stack.append(current)
#         visitedAry.append(current)
#     else:            	  	  	  	  # 다음에 방문할 정점이 없는 경우
#         current = stack.pop()
#
#
# print('방문 순서 -->', end='')
# for i in visitedAry:
#     print(chr(ord('A')+i), end='   ') # 아스키코드로 변환해서 바꾸고 출력.


## 교수님과 함께 만들어보기
## 임의의 그래프를 만들어서 순회하기

# def dfs(g, i, visited):
#     visited[i] = 1
#     print(chr(ord('A') + i), end=' ')
#     for j in range(len(g)):
#         if g[i][j] == 1 and not visited[j]:
#             dfs(g, j, visited)
#
#
# graph = [
#     [0, 1, 1, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0],
#     [1, 0, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]
#
# visited = [0] * len(graph) # list comprehension 으로 바꿔도 됨
# dfs(graph, 0, visited)




# ## 클래스 및 함수 선언 부분 ##
# class Graph() :
#     def __init__ (self, size) :
#         self.SIZE = size
#         self.graph = [[0 for _ in range(size)] for _ in range(size)]
#
# def printGraph(g) :
#     print(' ', end = ' ')
#     for v in range(g.SIZE) :
#         print(nameAry[v], end = ' ')
#     print()
#     for row in range(g.SIZE) :
#         print(nameAry[row], end = ' ')
#         for col in range(g.SIZE) :
#             print(f'{g.graph[row][col]:2d}', end = ' ')
#         print()
#     print()
#
# def findVtx(g, find_vtx) :
#     stack = []
#     visited_Ary = []	# 방문한 노드
#
#     current = 0	# 시작 정점
#     stack.append(current)
#     visited_Ary.append(current)
#
#     while len(stack) != 0:
#         next = None
#         for vertex in range(gSize):
#             if g.graph[current][vertex] != 0:
#                 if vertex in visited_Ary:	# 방문한 적이 있는 정점이면 탈락
#                     pass
#                 else:			# 방문한 적이 없으면 다음 정점으로 지정
#                     next = vertex
#                     break
#
#         if next is not None :				# 다음에 방문할 정점이 있는 경우
#             current = next
#             stack.append(current)
#             visited_Ary.append(current)
#         else:					# 다음에 방문할 정점이 없는 경우
#             current = stack.pop()
#
#     if findVtx in visited_Ary:
#         return True
#     else:
#         return False
#
#
# ## 전역 변수 선언 부분 ##
# G1 = None
# nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산' ]
# 춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5
#
#
# ## 메인 코드 부분 ##
# gSize = 6
# G1 = Graph(gSize)
# G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
# G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
# G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
# G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
# G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
# G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25
#
# print('## 자전거 도로 건설을 위한 전체 연결도 ##')
# printGraph(G1)
#
# # 가중치 간선 목록
# edgeAry = []
# for i in range(gSize) :
#     for k in range(gSize) :
#         if G1.graph[i][k] != 0 :
#             edgeAry.append([G1.graph[i][k], i, k])
#
# print(edgeAry)
#
# # from operator import itemgetter
# # edgeAry = sorted(edgeAry, key = itemgetter(0), reverse = True) # side effect 발생
# edgeAry.sort(key=lambda data: data[0], reverse=True) #라이브러리 호출 + side effect 없이 처리
#
# print(edgeAry)
#
# newAry = []
# for i in range(0,len(edgeAry), 2) :
#     newAry.append(edgeAry[i])
#
# index = 0
# while (len(newAry) > gSize-1) :	# 간선의 개수가 '정점 개수-1'일 때까지 반복
#     start = newAry[index][1]
#     end = newAry[index][2]
#     saveCost = newAry[index][0]
#
#     G1.graph[start][end] = 0
#     G1.graph[end][start] = 0
#
#     startYN = findVtx(G1, start)
#     endYN = findVtx(G1, end)
#
#     if startYN and endYN :
#         del (newAry[index])
#     else :
#         G1.graph[start][end] = saveCost
#         G1.graph[end][start] = saveCost
#         index += 1 ## 복구 후에 검사를 하면 안 되기 때문에 넘어가기 위해 +1 해주기
#
# print('## 최소 비용의 자전거 도로 연결도 ##')
# printGraph(G1)
#
# # sum = 0
# # for r in range(G1.SIZE):
# #     for c in range(G1.SIZE):
# #        sum = sum + G1.graph[r][c]
# # print(sum/2)
#
# print(sum(sum(row) for row in G1.graph) / 2)
#
# ## 코드가 오류로 꼬여서 뭐 어케된 건지 모르겠다



## 재귀 함수 - 코드가 짧아지고 수학적인 가독성이 좋아진다.
## 반복문으로 구현할 수 있다. 오버헤드가 적지만 경우에 따라 코드가 복잡해진다.
#
# def decimal_to_octal(number: int) -> str: ## 출력 용이를 위함
#     """
#     decimal to octal func
#     :param number: integer (base dec)
#     :return: string (base octal)
#     """
#     if number < 8:
#         return str(number)
#     else:
#         return decimal_to_octal(number//8) + str(number%8) # 몫을 전달, 나머지 구해오기 + 나머지
#
# n = int(input("decimal: "))
# print(decimal_to_octal(n))



## 피보나치 수열 - 재귀함수

def fibonachi_recursion(number: int) -> int :
    """
    피보나치 수를 반환하는 함수
    :param number: integer number
    :return: integer number
    """
    if number == 0 :
        return 0
    elif number == 1 :
        return 1
    else :
        return fibonachi_recursion(number - 1) + fibonachi_recursion(number - 2)

# n = int(input("Input integer number: ")) ## 나오긴 하는데 점점 느려진다.
#
# for i in range(0, n) :
#     print(fibonachi_recursion(i), end=' ')

## 반복문으로 재구성. 겁나게 빠르다.
# def fibonachi_loop(n: int)-> int:
#     """
#     반복문을 이용하여 피보나치 수를 구하는 함수 (단 2 이상의 값만 입력받는다)
#     :param n: integer (2 <= n)
#     :return: integer
#     """
#     sum_fibo, reminder1, reminder2 = 0, 0, 1
#     for i in range(n-1):
#         sum_fibo = reminder1 + reminder2
#         print(f'{i+2}번')
#         print(sum_fibo)
#         reminder1 = reminder2
#         reminder2 = sum_fibo
#
# # 교수님 코드 - 변수가 하나 줄었다. 패킹 언패킹으로 매우 짧게 줄였다.

def fibo_repetition_prof(number):
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
    return a



# 피보나치 수열 - 메모이제이션 추가: 압도적으로 일반 재귀보다 빠르다.

# memo = [None for _ in range(100)] # 계산결과를 빠르게 정적할당
# memo[0] , memo[1] = 0, 1

# memo = [0 if i==0 else 1 if i==1 else None for i in range(100)] ## 이렇게 한 줄 할 수 있긴한데 비효율적인듯?

memo = [0, 1] + [None] * (98) # 좀 더 갈끔한 방법.

def fibonachi_memoization(number: int, memo: list) -> int :
    """
    피보나치 수를 반환하는 함수
    :param number: integer number
    :return: integer number
    """
    if memo[number] is not None: # 이미 계산한 내용이면 바로 리턴하자.
        return memo[number]

    # if number < 2:
    #     result = number
    # else:
    result = fibonachi_memoization(number - 1, memo) + fibonachi_memoization(number - 2, memo)
    memo[number] = result
    return result

# for i in range(0, n) :
#     print(fibonachi_memoization(i), end=' ')

## 메인함수 선언부
# if __name__ == "__main__":
n = int(input("how much fibo? : "))
    # print("0"); print("0")
    # print("1"); print("1")
    # fibonachi_loop(num)
    # print()
    # print("----------")
    # print(fibo_repetition_prof(num))

for i in range(0, n):
    print(i)
    print(fibonachi_memoization(i, memo))
print("===========================")
for i in range(0, n):
    print(i)
    print(fibonachi_recursion(i))

print("===========================")
for i in range(0, n):
    print(i)
    print(fibo_repetition_prof(i))
