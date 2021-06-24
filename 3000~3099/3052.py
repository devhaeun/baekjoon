# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지이다.

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

arr = []
new_arr = []

for i in range(10):
    number = int(input())
    arr.append(number%42)

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(len(new_arr))
