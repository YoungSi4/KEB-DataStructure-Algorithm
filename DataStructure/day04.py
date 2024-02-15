## 재귀 - 회문 10-11코드

## 함수 선언 부분 ##
def palindrome(p_Str) :
    if len(p_Str) <= 1 : # 길이를 체크. 한 글자면 무조건 펠린드롬
        return True

    if p_Str[0] != p_Str[-1] : # 맨 앞과 맨 뒤를 체크. 둘이 다르면 False 리턴.
        return False

    return palindrome(p_Str[1:len(p_Str) - 1]) # 원래 문자열을 슬라이싱해서 재귀함수에 넣어버림
    # ex) 봄봄 > if 2개 지나감 > 슬라이싱 > 빈 리스트 전달 > 맨처음 if에 걸려서 Ture 반환.


## 전역 변수 선언 부분 ##
str_Array = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번주 주번이 너야", "살금 살금"]

## 메인 코드 부분 ##
for test_Str in str_Array :
    print(test_Str, end ='--> ')
    test_Str = test_Str.lower().replace(' ', '') ## 전부 소문자 처리하는 함수 + replace 함수로 띄어쓰기 붙임
    if palindrome(test_Str) :
        print('O')
    else :
        print('X')