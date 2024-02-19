## 그래프 응용문제 01
## 허니버터칩이 가장 많이 남은 편의점 찾기

# class Graph():
#     def __init__(self, size, graph):
#         self.size = size
#         self.graph = graph
#
# def dfs(graph):
#     visited, stack = [], []
#     current = 0
#     visited.append(current)
#     stack.append(current)
#
#     while len(stack) != 0:
#         next = None
#         for vertex in range(5):
#             if graph[current][vertex] == 1:
#                 if vertex in visited:
#                     pass
#                 else:
#                     next = vertex
#                     break
#
#         if next is not None:
#             stock(current)
#             current = next
#             stack.append(current)
#             visited.append(current)
#         else:
#             current = stack.pop()
#
# def stock(vertex):
#     global most_stock
#
#     if store_stock[vertex][1] > store_stock[most_stock][1]:
#         most_stock = vertex
#
# ## 전역변수
# most_stock = 0
# size = 5
# store_stock = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
# GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
# graph = [
#     [0, 1, 1, 0, 0],
#     [1, 0, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [0, 1, 1, 0, 1],
#     [0, 0, 0, 1, 0],
# ]
# G1 = Graph(size, graph)
#
# ## 메인 함수
# if __name__ == "__main__":
#     print("## 편의점 그래프 ##")
#
#     print('     ', end=' ')
#     for i in range(len(store_stock)):
#         print(f'{store_stock[i][0]}', end='  ')
#     print()
#
#     for row in range(len(store_stock)):
#         print(f'{store_stock[row][0]}', end='    ')
#         for col in range(len(store_stock)):
#             print("  ", end=' ')
#             print(f"{G1.graph[row][col]}", end=" ")
#         print()
#
#     dfs(G1.graph)
#     print(f"최대 보유 편의점, 개수 --> {store_stock[most_stock][0]}, {store_stock[most_stock][1]}")


"""
------------------------------------------------------------------------------------------
"""


## 응용예제 02
## 가장 효율적인 해저 케이블망 구성하기

class Graph():
    def __init__(self, size):
        self.graph = [[0 for _ in range(6)] for _ in range(6)]
        self.size = size

def printGraph(g) :
    print(' ', end = ' ')
    for v in range(g.size) :
        print(names[v], end = ' ')
    print()
    for row in range(g.size) :
        print(names[row], end = ' ')
        for col in range(g.size) :
            print(f'{g.graph[row][col]:2d}', end = ' ')
        print()
    print()

def quick_sort(datalist):
    # print(f"정렬 전 {datalist}")
    if len(datalist) <= 1:
        return datalist
    start = 0
    end = len(datalist) - 1

    high, low = end, start
    pivot = datalist[(high + low)//2][0]
    while low <= high:
        while datalist[low][0] < pivot:
            low += 1
        while datalist[high][0] > pivot:
            high -= 1
        if low <= high:
            datalist[low], datalist[high] = datalist[high], datalist[low]
            low, high = low + 1, high - 1

    mid = low
    # print(f"정렬 후 {datalist}")
    return quick_sort(datalist[start:mid]) + quick_sort((datalist[mid:end+1]))

def dfs(graph, find_vertex):
    visited, stack = [], []

    current = 0
    visited.append(current)
    stack.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(graph_size):
            if graph[current][vertex] != 0:
                if vertex in visited:
                    pass
                else:
                    next = vertex
                    break

        if next is not None:
            current = next
            stack.append(current)
            visited.append(current)
        else:
            current = stack.pop()

    if find_vertex in visited:
        return True
    else:
        return False

def minimum_edge(datalist):
    global G1
    index = 0
    while len(datalist) > graph_size - 1:
        start = datalist[index][1]
        end = datalist[index][2]
        save_value = datalist[index][0]

        G1.graph[start][end] = 0
        G1.graph[end][start] = 0

        start_flag = dfs(G1.graph, start)
        end_flag = dfs(G1.graph, end)

        if start_flag and end_flag:
            del(datalist[index])
        else:
            G1.graph[start][end] = save_value
            G1.graph[end][start] = save_value
            index += 1

    return G1.graph

## 전역변수
graph_size = 6
G1 = Graph(graph_size)
names = ['Se', 'NY', 'LD', 'BJ', 'BK', 'PR']
Se, NY, LD, BJ, BK, PR = 0, 1, 2, 3, 4, 5
G1.graph = [
    [0, 80, 0, 10, 0 ,0],
    [80, 0, 0, 40, 70 ,0],
    [0, 0, 0, 0, 30 ,60],
    [10, 40, 0, 0, 50 ,0],
    [0, 70, 30, 50, 0 ,20],
    [0, 0, 60, 0, 20 ,0],
]

## 메인 함수
if __name__ == "__main__":

    print("## 해저 케이블 연결을 위한 전체 연결도")
    edge_array = []
    for i in range(graph_size):
        for k in range(graph_size):
            if G1.graph[i][k] != 0:
                edge_array.append([G1.graph[i][k], i, k])
    printGraph(G1)

    new_array = []
    edge_array = quick_sort(edge_array)
    for i in range(0, len(edge_array), 2):
        new_array.append(edge_array[i])

    # print(new_array)

    new_array = minimum_edge(new_array)
    print("## 가장 효율적인 해저 케이블 연결도 ##")
    printGraph(G1)