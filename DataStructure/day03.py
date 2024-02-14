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


# 교수님과 함께 만들어보기
# 임의의 그래프를 만들어서 순회하기

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

visited = [0] * len(graph) # list comprehension 으로 바꿔도 됨
dfs(graph, 0, visited)