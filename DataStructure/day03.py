# 그래프 주석 이름

## 함수 선언 부분 ##
class Graph() :
    def __init__ (self, size) :
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end = ' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end = ' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end= '  ')
        print()
    print()


## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
mb, sl, hw, tw, sm, hs = 0, 1, 2, 3, 4, 5


## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[mb][sl] = 1; G1.graph[mb][hw] = 1
G1.graph[sl][mb] = 1; G1.graph[sl][tw] = 1
G1.graph[hw][mb] = 1; G1.graph[hw][tw] = 1
G1.graph[tw][sl] = 1; G1.graph[tw][hw] = 1; G1.graph[tw][sm] = 1; G1.graph[tw][hs] = 1
G1.graph[sm][tw] = 1; G1.graph[sm][hs] = 1
G1.graph[hs][tw] = 1; G1.graph[hs][sm] = 1

print('## G1 무방향 그래프 ##')
printGraph(G1)
