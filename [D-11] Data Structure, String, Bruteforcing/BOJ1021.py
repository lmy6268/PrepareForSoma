#회전하는 큐


import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
l = deque([i for i in range(1, n+1)]) #1~N까지의 원소를 가진 덱
tarIdx = list(map(int, input().split())) #뽑아낼 원소 목록
cnt = 0 #최종으로 출력할 최솟값의 합
for i in tarIdx: #원소 목록에서 값을 하나씩 뽑아냄
    L = l.copy() #덱을 복사 -> 왼쪽으로 이동시키는 경우
    R = l.copy() #덱을 복사 -> 오른쪽으로 이동시키는 경우
    Lcnt = 0 #-> 왼쪽으로 이동시킬 때의 연산 횟수
    Rcnt = 0 #-> 오른쪽으로 이동시킬 때의 연산 횟수
    while (True):
        if L[0] == i:
            break
        #원하는 값을 발견하지 못한 경우
        Lcnt += 1
        L.append(L.popleft())
    while (True):
        if R[0] == i:
            break
        #원하는 값을 발견하지 못한 경우
        Rcnt += 1
        R.appendleft(R.pop())
    if Lcnt >= Rcnt:
        R.popleft()
        l = R
        cnt += Rcnt
    else:
        L.popleft()
        l= L
        cnt+= Lcnt
print(cnt)
    