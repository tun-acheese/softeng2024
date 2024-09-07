# 단위변환(온도, 길이 등): 함수, 포맷팅

def main():
    def c_to_f(c):
        return (c * 9 / 5) + 32

    def f_to_c(f):
        return (f - 32) * 5 / 9

    def main():
        print("온도 단위 변환기")
        print("1: 섭씨(°C)에서 화씨(°F)로 변환")
        print("2: 화씨(°F)에서 섭씨(°C)로 변환")

        choice = int(input("선택하세요 (1 또는 2): "))

        if choice == 1:
            c = f("섭씨 온도를 입력하세요: "))
            f = c_to_f(c)
            print(f"{c}°C는 {f}°F입니다.")
        elif choice == 2:
            f = float(input("화씨 온도를 입력하세요: "))
            c = f_to_c(f)
            print(f"{f}°F는 {c}°C입니다.")
        else:
            print("잘못된 선택입니다. 1 또는 2를 입력하세요.")


if __name__ == '__main__':
    main()