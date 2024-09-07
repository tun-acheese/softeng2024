# 팩토리얼 구하기: 재귀함수
def main():
# 5! = 1*2*3*4*5
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("숫자를 입력하세요: "))
print(f"{num}!의 값은 {factorial(num)}입니다.")

if __name__ == '__main__':
    main()