from collections import deque


def solution(maps):
    n = len(maps) #세로 길이
    m = len(maps[0]) #가로 길이
    answer = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # bfs 진행
    queue = deque([(0, 0)])  # 시작 x,y 좌표를 큐에 추가
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and  maps[nx][ny]==1:
                queue.append((nx,ny))
                maps[nx][ny] += maps[x][y]
    if maps[n-1][m-1] != 1:
        answer = maps[n-1][m-1]
    
    return answer

# dataset = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
dataset =[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(dataset))