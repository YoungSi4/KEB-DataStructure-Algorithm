## 큐 응용예제 1
## 유명 맛집의 대기줄 구현하기

# def is_queue_full() :
#     global SIZE, queue, front, rear
#     if (rear == SIZE-1) :
#         return True
#     else :
#         return False
#
# def is_queue_empty() :
#     global SIZE, queue, front, rear
#     if (front == rear) :
#         return True
#     else :
#         return False
#
# def enQueue(data) :
#     global SIZE, queue, front, rear
#     if (is_queue_full()) :
#         print("큐가 꽉 찼습니다.")
#         return
#     rear += 1
#     queue[rear] = data
#
# def deQueue() :
#     global SIZE, queue, front, rear
#     if (is_queue_empty()) :
#         print("큐가 비었습니다.")
#         return None
#     front += 1
#     data = queue[front]
#     queue[front] = None
#
#     for i in range(front + 1, rear + 1): 	# 모든 사람을 한칸씩 앞으로 당긴다.
#         queue[i - 1] = queue[i]
#         queue[i] = None
#     front = -1
#     rear -= 1
#
#     return data
#
# def peek() :
#     global SIZE, queue, front, rear
#     if (is_queue_empty()) :
#         print("큐가 비었습니다.")
#         return None
#     return queue[front+1]
#
# ## 전역 변수 선언 부분 ##
# SIZE = 5
# queue = [ None for _ in range(SIZE) ]
# front = rear = -1
# member_list = ['정국', '뷔', '지민', '진', '슈가']
#
# if __name__ == "__main__":
#
#     for person in member_list:
#         enQueue(person)
#     print(queue)
#
#     for i in range(SIZE):
#         print(f'{deQueue()} 님이 식당에 들어감')
#         print(f'대기 줄 상태: {queue}')
#
#     print("식당 영업 종료!")


"""
-------------------------------------------------------------
"""


## 큐 응용예제 02
## 콜센터의 응답 대기 시간 계산하기

def is_queue_full() :
    global SIZE, queue, front, rear
    if ((rear+1)%SIZE == front) :
        return True
    else :
        return False

def is_queue_empty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (is_queue_full()) :
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None

    return data

def peek() :
    global SIZE, queue, front, rear
    if (is_queue_empty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

def calc_time() :
    global SIZE, queue, front, rear
    timeSum = 0
    for i in range((front+1)% SIZE, (rear+1)%SIZE) :
        timeSum += queue[i][1]
    return timeSum


## 전역 변수 선언 부분 ##
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
    waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

    for call in waitCall :
        print("귀하의 대기 예상시간은 ", calc_time(), "분입니다.")
        print("현재 대기 콜 --> ", queue)
        enQueue(call)
        print()

    print("최종 대기 콜 --> ", queue)
    print("프로그램 종료!")
