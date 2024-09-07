# 소수 구하기: 함수, 반복문

def main():

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')


if __name__ == '__main__':
    main()