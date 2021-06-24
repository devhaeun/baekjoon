# 세준이는 기말고사를 망쳤다.
# 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
# 이 값을 M이라고 한다.
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

# 세준이의 성적을 위의 방법대로 새로 계산했을 때,
# 새로운 평균을 구하는 프로그램을 작성하시오.

N = int(input())

score = list(map(int, input().split()))
M = max(score)

for i in range(len(score)):
    score[i] = score[i]/M*100

print(sum(score)/len(score))
