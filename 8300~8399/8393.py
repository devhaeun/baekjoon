# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# n 입력
n = int(input())

# 1부터 n까지 합
count = 0
for i in range(n):
    count+=i+1

print(count)
