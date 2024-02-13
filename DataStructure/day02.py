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


# 4-7 참고해서 원형 연결 리스트 삭제 기능 만들기
# 머리가 안 돌아가

# 원형 연결 리스트 응용 5 - 8 혼자 해결하기 문제
import random

class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def print_Nodes(start):
	current = start
	if current.link is head:
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def delete_Node(delete_Data) :
	global head, current, pre

	if head.data == delete_Data :		# 첫 번째 노드 삭제
		current = head
		head = head.link
		last = head
		while last.link != current:		# 마지막 노드를 찾으면 반복 종료
			last = last.link		# last를 다음 노드로 변경
		last.link = head			# 마지막 노드의 링크에 head가 가리키는 노드 지정
		del(current)
		return

	current = head	                        	# 첫 번째 외 노드 삭제
	while current.link != head :    # None이 없기 때문에 head가 기준
		pre = current
		current = current.link
		if current.data == delete_Data :  	# 중간 노드를 찾았을 때
			pre.link = current.link
			del(current)
			return

def process_toggle(datas):
	plus_count, minus_count, zero_count = 0, 0, 0
	# odd_count, even_count, reminder = 0, 0, 0

	for data in datas:
		if data > 0:
			plus_count += 1
		else:
			minus_count += 1
	print(f'양수-->{plus_count}  음수-->{minus_count}  0-->{zero_count}')

	# 이전 문제 코드
	# if even_count > odd_count:
	# 	reminder = 0
	# else:
	# 	reminder = 1
	#
	# current = head
	# while True:
	# 	if current.data % 2 == reminder:
	# 		current.data *= -1
	# 	if current.link == head:
	# 		break
	# 	current = current.link

	current = head
	while True:
		current.data = current.data * -1
		if current.link == head:
			break
		current = current.link

## 전역 변수 선언 부분 ##
head, current, last = None, None, None
data_Array = [random.randint(-100, 100) for number in range(7)]

## 메인 코드 부분 ##
if __name__ == "__main__" :
    node = Node()		# 첫 번째 노드
    node.data = data_Array[0]
    head = node
    node.link = head


    for data in data_Array[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    print_Nodes(head)
    process_toggle(data_Array)
    print_Nodes(head)
