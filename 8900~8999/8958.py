# "OOXXOXXOOO"와 같은 OX 퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 ㅗ딘다.

T = int(input())

for i in range(T):
    score = 0
    total = 0
    quiz = list(input())

    for j in range(len(quiz)):
        if quiz[j] == 'O':
            score = 1
            if j == 0:
                total += score
                score = 0
            else:
                for _ in range(j-1,-1,-1):
                    if quiz[_] == 'O':
                        score += 1
                    else:
                        break
                total += score
                score = 0

    print(total)
