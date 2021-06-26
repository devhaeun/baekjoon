# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다.
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 예를 들어, d(75) = 75+7+5 - 87이다.

# 양의 정수 n이 주어졌을 때,
# 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...
# 과 같은 무한 수열을 만들 수 있다.

# n을 d(n)의 생성자라고 한다.
# 생성자가 한 개보다 많은 경우도 있다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 100보다 작은 셀프 넘버는 총 13개가 있다.
# 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def d(n):
    thousand = n//1000
    hundred = n//100 - n//1000*10
    ten = n//10 - n//100*10
    one = n%10

    summ = n + thousand + hundred + ten + one
    return summ

a=[]
for i in range(1,10000):
    a.append(i)

number = 0

for i in range(1,10000):
    number = d(i)
    if number in a:
        a.remove(number)

for i in a:
    print(i)
