# 위와 같은 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게
# 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자.
# (행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다고 가정한다.
# 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시
# 입력으로 주어지지 않는다.)

import math

# 테스트 케이스 개수
T = int(input())

for i in range(T):
    # 출발점 (x1,y1), 도착점 (x2,y2)
    x1,y1,x2,y2 = map(int, input().split())
    # 행성계의 개수 n
    n = int(input())
    # 행성계의 중점과 반지름 (cx,cy,r)
    cx=[]
    cy=[]
    r=[]
    for j in range(n):
        tempx, tempy, tempr = 0, 0, 0
        tempx, tempy, tempr = map(int, input().split())
        cx.append(tempx)
        cy.append(tempy)
        r.append(tempr)

    # 출발점/도착점을 포함하는 행성계의 수
    number = 0

    for j in range(n):
        start = math.sqrt((cx[j]-x1)**2+(cy[j]-y1)**2)
        end = math.sqrt((cx[j]-x2)**2+(cy[j]-y2)**2)
        if start < r[j] or end<r[j]:
            if start < r[j] and end<r[j]:
                continue
            else:
                number += 1

    print(number)