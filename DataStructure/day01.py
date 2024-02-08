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
2차 다항식 계산하기 - 다양한 지수에 대응
"""

def print_Poly(t_x, f_x) -> str : #언더스코어 표기법
    poly_expression = "F(x) = "

    for i in range(len(fx)):
        term = t_x[i]
        coefficient = f_x[i]  # 계수

        if coefficient == 0:
            continue
        if coefficient > 0 and i != 0:
            poly_expression += "+"

        poly_expression += f'{coefficient}x^{term} '

    return poly_expression


def calculation_Poly(x_Value, t_x, f_x):
    return_Value = 0

    for i in range(len(fx)):
        coefficient = f_x[i]  # 계수
        return_Value += coefficient * pow(x_Value, t_x[i])

    return return_Value


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
fx = [7, -4, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_Poly(tx, fx))
    print(calculation_Poly(int(input("input x -> ")), tx, fx))

