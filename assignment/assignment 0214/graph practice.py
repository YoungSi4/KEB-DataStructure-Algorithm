## 그래프 응용문제 01
## 허니버터칩이 가장 많이 남은 편의점 찾기

class Graph():
    def __init__(self, size, graph):
        self.size = size
        self.graph = graph

## 전역변수
size = 5
store_stock = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
G1 = Graph(size, graph)

## 메인 함수
if __name__ == "__main__":
    print("## 편의점 그래프 ##")

    print('    ')
    for i in range(len(store_stock)):
        print(f'{store_stock[i][0]}', end='  ')

    for row in range(len(store_stock)):
        print(f'{store_stock[row][0]}', end='    ')
        for col in range(len(store_stock)):
            pass



