# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개,
# N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별을 출력하시오.

N = int(input())

for i in range(N):
    for j in range(N-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*',end='')
    print()
