import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"time elapsed: {end - start}")
        return result
    return wrapper

def factorial(number) -> int:
    """
    fac by repetition
    :param number: int number to repeat
    :return: int result
    """
    result = 1
    # while(number > 1):
    #     result = result * number
    #     number -= 1
    for i in range(number):
        result = result * (i+1)
    return result

def factorial_recursion(number) -> int:
    """
    fac by recursion
    :param number: number
    :return: int result
    """
    if number == 1:
        return 1
    else:
        return number * factorial_recursion(number - 1)
@timer
def Combination(n, r) -> int:
    """
    nCr 조합의 경우의 수를 반환하는 함수
    :param n: 선택할 수 있는 숫자
    :param r: 선택한 수
    :return: int
    """

    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)