## 음이 아닌 정수로 구성되어 있는 배열 an_array에서
##짝수만 추출한 배열과 홀수만 추출한 배열을 만들어보세요

## 전역변수 선언
odd_array = []
even_array = []
an_array = [1, 2, 3, 4, 5, 6]

def extract(datas):
    for data in datas:
        if data % 2 == 0:
            even_array.append(data)
        else:
            odd_array.append(data)

if __name__ == "__main__":
    extract(an_array) ## 파이썬에서 mutable은 call by ref로 상호작용 한다.

    print(f"원래 리스트: {an_array}")
    print(f"홀수 리스트: {odd_array}")
    print(f"짝수 리스트: {even_array}")
