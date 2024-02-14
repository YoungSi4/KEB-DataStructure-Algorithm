# 키 순서대로 출력

## 클래스와 함수 선언 부분 ##
# class Node() :
# 	def __init__ (self) :
# 		self.data = None
# 		self.link = None
#
# def print_Nodes(start) :
# 	current = start
# 	if current == None :
# 		return
# 	print(current.data, end = ' ')
# 	while current.link != None:
# 		current = current.link
# 		print(current.data, end = ' ')
# 	print()
#
# def make_Simple_Linked_List(name_Phone) :
# 	global head, current, pre
# 	print_Nodes(head)
#
# 	node = Node()
# 	node.data = name_Phone
# 	if head == None :			# 첫 번째 노드일 때
# 		head = node
# 		return
#
# 	if head.data[1] > name_Phone[1] :	# 첫 번째 노드보다 작을 때
# 		node.link = head
# 		head = node
# 		return
#
# 	# 중간 노드로 삽입하는 경우
# 	current = head
# 	while current.link != None :
# 		pre = current
# 		current = current.link
# 		if current.data[1] > name_Phone[1]: # 부등호만 바꾸면 오름차순 내림차순 전환 가능
# 			pre.link = node
# 			node.link = current
# 			return
#
# 	# 삽입하는 노드가 가장 큰 경우
# 	current.link = node
#
# ## 전역 변수 선언 부분 ##
# head, current, pre = None, None, None
# data_Array = [["지민", "180"],
#               ["정국", "177"],
#               ["뷔", "183"],
#               ["슈가", "175"],
#               ["진", "179"]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#
# 	for data in data_Array :
# 		make_Simple_Linked_List(data)
#
# 	print_Nodes(head)


# # 4-7 참고해서 원형 연결 리스트 삭제 기능 만들기
# # 머리가 안 돌아가
#
# class Node:
#     def __init__(self):
#         self.data = None
#         self.link = None
#
# def insert_node():
#     pass
#
# def delete_node():
#     pass
#
# def find_node():
#     pass
#
# def print_node(start_point):
#     current = start_point
#     if current.link == head:
#         return
#
# current, last, head = 0, 0, 0
# data_Array = [] # 임시
#
# if __name__ == "__main__": # 원형 리스트 생성.
#     node = Node()
#     node.data = data_Array[0]
#     head = node
#     node.link = head
#
#     for data in data_Array[1:]:
#         pre = node
#         node = Node()
#         node.data = data
#         pre.link = node
#         node.link = head

# # 원형 연결 리스트 응용 5 - 8 혼자 해결하기 문제
# import random
#
# class Node() :
# 	def __init__ (self) :
# 		self.data = None
# 		self.link = None
#
# def print_Nodes(start):
# 	current = start
# 	if current.link is head:
# 		return
# 	print(current.data, end=' ')
# 	while current.link != start:
# 		current = current.link
# 		print(current.data, end=' ')
# 	print()
#
# def delete_Node(delete_Data) :
# 	global head, current, pre
#
# 	if head.data == delete_Data :		# 첫 번째 노드 삭제
# 		current = head
# 		head = head.link
# 		last = head
# 		while last.link != current:		# 마지막 노드를 찾으면 반복 종료
# 			last = last.link		# last를 다음 노드로 변경
# 		last.link = head			# 마지막 노드의 링크에 head가 가리키는 노드 지정
# 		del(current)
# 		return
#
# 	current = head	                        	# 첫 번째 외 노드 삭제
# 	while current.link != head :    # None이 없기 때문에 head가 기준
# 		pre = current
# 		current = current.link
# 		if current.data == delete_Data :  	# 중간 노드를 찾았을 때
# 			pre.link = current.link
# 			del(current)
# 			return
#
# def process_toggle(datas):
# 	plus_count, minus_count, zero_count = 0, 0, 0
# 	# odd_count, even_count, reminder = 0, 0, 0
#
# 	for data in datas:
# 		if data > 0:
# 			plus_count += 1
# 		else:
# 			minus_count += 1
# 	print(f'양수-->{plus_count}  음수-->{minus_count}  0-->{zero_count}')
#
# 	# 이전 문제 코드
# 	# if even_count > odd_count:
# 	# 	reminder = 0
# 	# else:
# 	# 	reminder = 1
# 	#
# 	# current = head
# 	# while True:
# 	# 	if current.data % 2 == reminder:
# 	# 		current.data *= -1
# 	# 	if current.link == head:
# 	# 		break
# 	# 	current = current.link
#
# 	current = head
# 	while True:
# 		current.data = current.data * -1
# 		if current.link == head:
# 			break
# 		current = current.link
#
# ## 전역 변수 선언 부분 ##
# head, current, last = None, None, None
# data_Array = [random.randint(-100, 100) for number in range(7)]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#     node = Node()		# 첫 번째 노드
#     node.data = data_Array[0]
#     head = node
#     node.link = head
#
#
#     for data in data_Array[1:] :	# 두 번째 이후 노드
#         pre = node
#         node = Node()
#         node.data = data
#         pre.link = node
#         node.link = head
#
#     print_Nodes(head)
#     process_toggle(data_Array)
#     print_Nodes(head)



# # 스택
#
# def is_StackFull():
# 	global SIZE, stack, top
# 	if (top >= SIZE-1):
# 		return True
# 	else :
# 		return False
#
# def push(data) :
# 	global SIZE, stack, top
# 	# if is_StackFull():
# 	if top >= SIZE - 1:
# 		print("스택이 꽉 찼습니다.")
# 		return
# 	top += 1
# 	stack[top] = data
#
# def pop():
# 	if top == -1:
# 		print("스택이 비었습니다")
# 		return None
# 	data = stack[top]
# 	stack[top] = None
# 	top -= 1
# 	return data
#
# def peek(data):
#     if top == -1:
#         print("스택이 비었습니다")
#         return None
#     return stack[top]
#
# SIZE = 5
# stack = ["커피", "녹차", "꿀물", "콜라", None]
# top = 3
#
# print(stack)
# push("환타")
# print(stack)
# push("게토레이")


# # 스택 응용 - 괄호 짝 맞추기
#
# ## 함수 선언 부분 ##
# def is_Stack_Full():
#     global size, stack, top
#     if top >= size-1:
#         return True
#     else :
#         return False
#
# def is_Stack_Empty():
#     global size, stack, top
#     return size[top]
#
# def push(data) :
#     global size, stack, top
#     if is_Stack_Full():
#         print("스택이 꽉 찼습니다.")
#         return
#     top += 1
#     stack[top] = data
#
# def pop() :
#     global size, stack, top
#     if is_Stack_Empty():
#         print("스택이 비었습니다.")
#         return None
#     data = stack[top]
#     stack[top] = None
#     top -= 1
#     return data
#
# def peek() :
#     global size, stack, top
#     if is_Stack_Empty():
#         print("스택이 비었습니다.")
#         return None
#     return stack[top]
#
# def check_Bracket(expr: str) -> bool:
#     """
#     check bracket pair in expression
#     :param expr: str
#     :return: bool
#     """
#
#     stack = list()
#     table = {')': '(', '}': '{', ']': '[', '>': '<'} # dict 자료형으로 키 밸류로 매칭
#
#     for charictor in expr:
#         if charictor in table.values(): # ( { [ < 만 스택에 넣는다
#             # push(charictor)
#             stack.append(charictor)
#         elif charictor in table.keys():
#             if not stack or table[charictor] != stack.pop():
#                 return False
#     return len(stack) == 0 # 스택의 길이가 0이면 True
#
# ## 전역 변수 선언 부분 ##
#
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__" :
#     expression = input("input expression")
#     print(check_Bracket(expression))

# 이진 트리 구현해보기 - 8-2 코드 가져와서 실습

# class TreeNode() :
#     def __init__ (self) :
#         self.left = None
#         self.data = None
#         self.right = None
#
# node1 = TreeNode()
# node1.data = '화사'
#
# node2 = TreeNode()
# node2.data = '솔라'
# node1.left = node2
#
# node3 = TreeNode()
# node3.data = '문별'
# node1.right = node3
#
# node4 = TreeNode()
# node4.data = '휘인'
# node2.left = node4
#
# node5 = TreeNode()
# node5.data = '쯔위'
# node2.right = node5
#
# node6 = TreeNode()
# node6.data = '선미'
# node3.left = node6
#
# node8 = TreeNode()
# node8.data = '다현'
# node4.right = node8
#
# node12 = TreeNode()
# node12.data = '사나'
# node6.right = node12
#
# def preorder(node) :
#     if node == None:
#         return
#     print(node.data, end='->')
#     preorder(node.left)
#     preorder(node.right)
#
# def inorder(node):
#     if node == None :
#         return
#     inorder(node.left)
#     print(node.data, end='->')
#     inorder(node.right)
#
# def postorder(node):
#     if node == None :
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.data, end='->')
#
# print('전위 순회 : ', end = '')
# preorder(node1)
# print('끝')
#
# print('중위 순회 : ', end = '')
# inorder(node1)
# print('끝')
#
# print('후위 순회 : ', end = '')
# postorder(node1)
# print('끝')



# 이진 탐색 트리 구현 - 8-4 번 코드 활용

## 함수 선언 부분 ##
class TreeNode:
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

## 전역 변수 선언 부분 ##
root = None
name_Array = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분 ##
node = TreeNode()
node.data = name_Array[0]
root = node

for name in name_Array[1:] :

    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left is None :
                current.left = node
                break
            current = current.left
        else :
            if current.right is None :
                current.right = node
                break
            current = current.right

findName = input("찾고 싶은 아이돌 입력: ")

current = root
while True :
    if findName == current.data:
        print(findName, '을(를) 찾음.')
        break
    elif findName < current.data :
        if current.left is None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left
    else :
        if current.right is None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right
