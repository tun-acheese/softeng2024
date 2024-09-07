# • 1-100까지 짝수의 합 구하기: 반복문, 조건문, 지능형 리스트, 수학함수

def main():

total_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number

print(f"1부터 100까지의 짝수의 합은 {total_sum}입니다.")

#지능형 리스트
total_sum = sum(number for number in range(1, 101) if number % 2 == 0)

print(f"1부터 100까지의 짝수의 합은 {total_sum}입니다.")



if __name__ == '__main__':
    main()