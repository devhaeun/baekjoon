# N이 주어졌을 때, fibonacci(N)을 호출했을 때,
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 피보나치 수를 구하는 C++ 함수
# int fibonacci(int n) {
#   if (n==0) {
#       printf("0");
#       return 0;
#   } else if (n==1) {
#       printf("1");
#       return 1;
#   } else {
#       return fibonacci(n-1) + fibonacci(n-2);
#   }
# }

# 테스트 케이스 개수
T = int(input())

zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n], one[n])

for i in range(T):
    N = int(input())
    fibo(N)