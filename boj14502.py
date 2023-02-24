#0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳 
import sys;input = sys.stdin.readline
from collections import deque
from copy import deepcopy
from itertools import combinations as combi

n,m = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#입력
graph = []
blank_pos = []
virus_pos = []
answer = 0

for i in range(n):
    arr=list(map(int,input().split()))
    graph.append(arr)
    for j in range(m):
        if arr[j] == 0:
            blank_pos.append((i,j)) #빈칸 위치
        elif arr[j] ==2:
            virus_pos.append((i,j)) #바이러스 위치

#벽을 세우는 함수
def buildWalls(wallPos,virusPos,board):
    global answer
    for x,y in wallPos:
        board[x][y] =1 #벽을 세움 
    safeCnt = n*m - len(wallPos) - len(virusPos) #전염 전 안전 영역 넓이 
    for vx,vy in virusPos:
        queue = deque([(vx,vy)])
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m or board[nx][ny] !=0:
                    continue
                queue.append((nx,ny)) #큐에 추가
                board[nx][ny] = 2 #미리 마킹 (방문 표시)
                safeCnt-=1 #전염됨 
                if safeCnt <answer:
                    return -1

    res = 0
    for b in board:
        res += b.count(0)
    return res

for c in combi(blank_pos,3):
    res = buildWalls(c,virus_pos,deepcopy(graph))
    if answer<res:
        answer = res
print(answer)





