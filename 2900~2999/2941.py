# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다.
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for i in croatia:
    alpha = alpha.replace(i, '*')

print(len(alpha))
