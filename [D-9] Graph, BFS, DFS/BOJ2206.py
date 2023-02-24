#벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
import sys;input = sys.stdin.readline
from collections import deque 
n,m = map(int,input().split())
visited = [[False]*m for _ in range(n)]
graph = [list(map(int,list(input().rstrip()))) for _ in range (n)]
#좌우상하를 위한 벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    breakCnt =0
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        visited[x][y]= True
        for i in range(4):
            nx = x+dx[i]; ny=y+dy[i]
            if nx >= 0 and nx<m and ny>=0 and ny<n and visited[nx][ny] == False:
                


    