# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())

for i in range(C):
    summ = 0
    count = 0

    info = list(map(int, input().split()))
    N = info[0]

    for j in range(1,len(info)):
        summ += info[j]
    avg = summ/N

    for j in range(1,len(info)):
        if info[j]>avg:
            count += 1

    print('%.3f%%'%(count/N*100))