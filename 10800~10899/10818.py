# N개의 정수가 주어진다.
# 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
arr = list(map(int, input().split()))

print("%d %d"%(min(arr), max(arr)))