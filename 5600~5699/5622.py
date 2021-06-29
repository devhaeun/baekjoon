# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면,
# 숫자를 하나 누른 다음에 금속 핀이 있는 곳까지 시계방향으로 돌려야 한다.
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고,
# 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하며,
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
# 할머니가 외운 단어가 주어졌을 때,
# 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

memory = list(input())

alphabet = []
for i in range(26):
    alphabet.append(chr(65+i))

time = 0
for i in memory:
    number = alphabet.index(i)
    if number<3:
        # 숫자 2 = 3초
        time += 3
    elif number<6:
        # 숫자 3 = 4초
        time += 4
    elif number<9:
        # 숫자 4 = 5초
        time += 5
    elif number<12:
        # 숫자 5 = 6초
        time += 6
    elif number<15:
        # 숫자 6 = 7초
        time += 7
    elif number<19:
        # 숫자 7 = 8초
        time += 8
    elif number<22:
        # 숫자 8 = 9초
        time += 9
    else:
        # 숫자 9 = 10초
        time += 10

print(time)
