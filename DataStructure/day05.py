## 문제 변경 - 압정미로

# ## 함수 선언 부분 ##
# def growRich() :
#     memo = [[0 for _ in range(COL)] for _ in range(ROW)]
#     memo[0][0] = goldMaze[0][0]
#
#     rowSum = memo[0][0]
#     for i in range(1, ROW) :
#         rowSum += goldMaze[0][i]
#         memo[0][i] = rowSum
#
#     colSum = memo[0][0]
#     for i in range(1, COL) :
#         colSum += goldMaze[i][0]
#         memo[i][0] = colSum
#
#     for row in range(1, ROW) :
#         for col in range(1, COL):
#             if (memo[row][col-1] < memo[row-1][col]):
#                 memo[row][col] = memo[row][col-1] + goldMaze[row][col]
#             else:
#                 memo[row][col] = memo[row-1][col] + goldMaze[row][col]
#
#     return memo[ROW-1][COL-1]
#
# ## 전역 변수 선언 부분 ##
# ROW, COL = 5, 5
# goldMaze = [[1, 4, 4, 2, 2],
#           [1, 3, 3, 0, 5],
#           [1, 2, 4, 3, 0],
#           [3, 3, 0, 4, 2],
#           [1, 3, 4, 5, 3]]
#
# ## 메인 코드 부분 ##
# macolGold = growRich()
# print('황금 미로에서 밟은 압정 개수 -->', macolGold)

## 응용예제 2 피보나치 수열

# def fibonacci_recursion(num)-> int:
#     global count_recursion
#     count_recursion += 1
#
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#
#     return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)
#
# def fibonacci_memo(num, memo) -> int:
#     global count_memo
#     count_memo += 1
#
#     if memo[num] is not None:
#         return memo[num]
#
#     if num < 2:
#         result = num
#     else:
#         result = fibonacci_memo(num-1, memo) + fibonacci_memo(num-2, memo)
#     memo[num] = result
#     return result
#
# ## 전역 변수
# count_recursion = 0
# count_memo = 0
#
# if __name__ == "__main__":
#     num = int(input("몇 번째 피보나치? -> "))
#
#     memoization = [0, 1] + [None] * num
#
#     print(f'메모 방식 --> 답: {fibonacci_memo(num, memoization)}, 반복수: {count_memo}')
#     print(f'재귀 방식 --> 답: {fibonacci_recursion(num)}, 반복수: {count_recursion}')

## 너비 우선 탐색

# from collections import deque
#
# def dfs(g, i, visited):
#     visited[i] = 1
#     print(chr(ord('A')+i), end=' ')
#     for j in range(len(g)):
#         if g[i][j] == 1 and not visited[j]:
#             dfs(g, j, visited)
#
#
# def bfs(g, i, visited):
#     queue = deque([i]) # 큐 초기화 / 데크 객체이긴한데, 큐처럼 사용
#     visited[i] = 1 # i번 방에 1로 초기화 (방문기록)
#
#     while queue:
#         i = queue.popleft() # 완전히 popout 되면 종료된다
#         print(chr(ord('A') + i), end=' ')
#         for j in range(len(g)):
#             if g[i][j] == 1 and not visited[j]:
#                 queue.append(j)
#                 visited[j] = 1
#
# graph = [
#     [0, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0, 0],
#     [0, 1, 1, 0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 1, 0]
# ]
#
# visited_dfs = [0 for _ in range(len(graph))]
# visited_bfs = [0 for _ in range(len(graph))]
# dfs(graph, 0, visited_dfs)
# print()
# bfs(graph, 0, visited_bfs)

## 백준 18352번 특정 거리의 도시 찾기 https://www.acmicpc.net/problem/18352

## bfs를 쓸지 dfs를 쓸지 고민해봐야 한다.
## 이 문제에선 bfs가 더 유리하다
## bfs를 사용하기 위해서 데크를 가져온다

from collections import deque

n, m, k, x = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    g[start].append(end)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next in g[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)