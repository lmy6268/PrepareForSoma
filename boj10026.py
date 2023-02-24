from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#type - True : 색약 O , False : 색약 X


def bfs(data, x, y, type):
    global visited
    queue = deque([(x, y)])
    visited[x][y] = True #방문처리
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny]:
                continue
            if not type:
                if data[x][y] == data[nx][ny]: #같은 문자일 경우
                    visited[nx][ny] = True
                    queue.append((nx,ny)) #다음 문자 확인
            else: #색약이 있는 경우
                if (data[x][y] ==["R","G"] and data[nx][ny] in ["R","G"]) or (data[x][y]=="B" and data[nx][ny]=="B"):
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return True


answer = []
for _ in range(2):
    visited = [[False] * n for _ in range(n)]
    area = 0
    t = False if _ == 0 else True  # 타입
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and bfs(deepcopy(graph),i, j, t):
                area += 1
    answer.append(area)
print(*answer)

#많이 빠른 풀이
# import sys;input = sys.stdin.readline

# drc = [(0,1),(1,0),(0,-1),(-1,0)]
# N = int(input())
# graph = [input().rstrip() for _ in range(N)]
# def solution(diff_colors):
#     visited = [[0]*N for _ in range(N)]
#     cnt = 0 #구역의 수
#     for r in range(N):
#         for c in range(N):
#             if visited[r][c]: #이미 방문한 경우
#                 continue 
#             cnt+=1
#             visited[r][c] =1
#             now = graph[r][c]
#             stack = [(r,c)] #스택에 위치값을 저장 
#             while stack:
#                 x,y = stack.pop()
#                 for dr,dc in drc:
#                     nr,nc = x+dr,y+dc
#                     if not ( 0<=nr <N and 0<=nc<N) or visited[nr][nc] or graph[nr][nc] in diff_colors[now]:
#                         continue
#                     visited[nr][nc] = 1
#                     stack.append((nr,nc))
#     return cnt
# diff_colors1 = {"R": set(("G", "B")), "G": set(("R", "B")), "B": set(("R", "G"))}
# diff_colors2 = {"R": set(("B")), "G": set(("B")), "B": set(("R", "G"))}

# print(solution(diff_colors1), solution(diff_colors2))