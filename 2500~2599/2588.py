# (세 자리 수) x (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2) 위치에 들어갈 세 자리 자연수가 주어질 때
# (3), (4), (5), (6) 위치에 들어갈 값을 구하는 프로그램을 작성하시오.

initial_num = int(input())
last_num = int(input())

blank3 = initial_num*(last_num%10)
blank4 = initial_num*(last_num//10%10)
blank5 = initial_num*(last_num//100)
blank6 = blank3 + blank4*10 + blank5*100

print(blank3)
print(blank4)
print(blank5)
print(blank6)
