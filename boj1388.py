
#같은 모양 - 행, 열인 경우에만 방문 처리를 진행.

import sys
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))
visited = [[False]*m for _ in range (n)]
dx = [1, -1]
dy = [1, -1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx, ny = -1,-1
            if  graph[x][y] == '|':
                nx = x+dx[i]
                ny = y
            if  graph[x][y]== '-':
                nx = x
                ny = y+dy[i]
            if nx <0 or ny<0 or nx>=n or ny>=m or visited[nx][ny]:
                continue
            if  graph[x][y] == graph[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny] = True
        
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:  # 방문하지 않은 노드인 경우
            bfs(i, j)
            cnt += 1
print(cnt)
