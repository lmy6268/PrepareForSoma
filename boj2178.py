import sys;input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i] ; ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1: #방문하지 않은 노드인 경우
                graph[nx][ny] += graph[x][y]
                queue.append((nx,ny))
bfs(0,0)
print(graph[n-1][m-1])