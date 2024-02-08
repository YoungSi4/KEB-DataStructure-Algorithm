"""
조합 구하기
"""

# import Probability
# import time
#
# if __name__ == "__main__":
#     n = int(input("Input n : "))
#     r = int(input("Input r : "))
#     print(f"{n} Combination {r} is {Probability.Combination(n, r)}")

"""
업다운 숫자 맞추기 게임 : O(log N)
"""

# import random
#
# counter = 0
# def judge(rand, choose):
#     if(rand == choose):
#         print(f"맞췄습니다! 정답은 {generated_Numeber}입니다! {counter}회 시도했습니다!")
#         return False
#     elif(rand > choose):
#         print(f"{choose}는 생성된 숫자보다 작습니다.")
#         return True
#     else:
#         print(f"{choose}는 생성된 숫자보다 큽니다")
#         return True
#
# if __name__ == "__main__":
#     generated_Numeber = random.randint(1,100)
#     is_Correct = True
#     while(is_Correct):
#         guess_num = int(input("생성된 숫자를 맞춰보세요: "))
#         counter += 1
#         is_Correct = judge(generated_Numeber, guess_num)



"""
2차 다항식 계산하기
"""

def print_Poly(f_x) -> str : #언더스코어 표기법
    term = len(f_x) - 1
    poly_expression = "F(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수

        if coefficient >= 0:
            poly_expression += "+"
        poly_expression += f'{coefficient}x^{term} '
        term -= 1

    return poly_expression


def calculation_Poly(x_Value, f_x):
    return_Value = 0
    term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        return_Value += coefficient * pow(x_Value, term)
        term -= 1

    return return_Value


## 전역 변수 선언 부분 ##
fx = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_Poly(fx))
    print(calculation_Poly(int(input("input x -> ")), fx))