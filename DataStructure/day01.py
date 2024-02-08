def factorial(number) -> int:
    result = 1
    while(number > 1):
        result = result * number
        number -= 1
    # for i in range(number):
    #     result = result * i
    return result

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

if __name__ == "__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n} Combination {r} is {Combination(n, r)}")

