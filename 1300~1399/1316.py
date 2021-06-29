# 그룹 단어란 단어에 존재하는 모든 문자에 대해서,
# 각 문자가 연속해서 나타나는 경우만을 말한다.

# 단어 N개를 입력으로 받아
# 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

N = int(input())

count = 0
for i in range(N):
    store = []
    word = input()
    temp = 1

    for j in range(len(word)):
        if word[j] not in store:
            store.append(word[j])
        elif word[j] in store and word[j-1] == word[j]:
            continue
        else:
            store.remove(word[j])
            temp = 0
            break

    if temp != 0:
        count+=1

print(count)
