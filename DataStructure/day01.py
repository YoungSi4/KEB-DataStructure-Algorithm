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

import random

counter = 0
def judge(rand, choose):
    if(rand == choose):
        print(f"맞췄습니다! 정답은 {generated_Numeber}입니다! {counter}회 시도했습니다!")
        return False
    elif(rand > choose):
        print(f"{choose}는 생성된 숫자보다 작습니다.")
        return True
    else:
        print(f"{choose}는 생성된 숫자보다 큽니다")
        return True

if __name__ == "__main__":
    generated_Numeber = random.randint(1,100)
    is_Correct = True
    while(is_Correct):
        guess_num = int(input("생성된 숫자를 맞춰보세요: "))
        counter += 1
        is_Correct = judge(generated_Numeber, guess_num)