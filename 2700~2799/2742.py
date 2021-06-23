# 자연수 N이 주어졌을 때,
# N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# N 입력
N = int(input())

# N부터 1까지 출력
for i in range(N, 0, -1):
    print(i)
