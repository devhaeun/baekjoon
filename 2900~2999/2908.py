# 상근이의 동생 상수는 수학을 정말 못한다.
# 상수는 숫자를 읽는데 문제가 있다.
# 이렇게 수학을 못하는 상수를 위해 상근이는 수의 크기를 비교하는 문제를 내주었다.
# 상근이는 세 자리 수 두 개를 칠판에 써주었다.
# 그 다음에 크기가 큰 수를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다.

A,B = map(int, input().split())

A = A%10*100 + (A%100-A%10) + A//100
B = B%10*100 + (B%100-B%10) + B//100

print(max(A,B))