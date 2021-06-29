# 알파벳 대소문자로 된 단어가 주어지면,
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = list(input())
alphabet = []

for i in range(26):
    if chr(65+i) in word or chr(97+i) in word:
        temp = word.count(chr(97+i))
        TEMP = word.count(chr(65+i))
        alphabet.append(temp+TEMP)
    else:
        alphabet.append(0)
    
if alphabet.count(max(alphabet))>1:
    print('?')
else:
    print(chr(65+alphabet.index(max(alphabet))))
