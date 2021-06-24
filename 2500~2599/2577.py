# 세 개의 자연수 A,B,C가 주어질 때 AxBxC 를 계산한 결과에
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

A = int(input())
B = int(input())
C = int(input())
ans = str(A*B*C)
ans = list(map(int, ans))

for i in range(0,10):
    count = ans.count(i)
    print(count)
