#TC
rect = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1;characterY = 3 ; itemX = 7;itemY = 8; exp = 17 


from collections import deque
#해결방안
def solution(rect,chaX,chaY,itX,itY):
    MX = 0
    MY = 0
    
    #1. 좌표를 2배로 -> 프로그램이 정상적으로 꺾임을 인식할 수 있도록
    rect = [list(map(lambda x:x*2,i)) for i in rect]
    for x,y,x2,y2  in rect:
        MX = max(x2,MX)
        MY = max(y2,MY)

    #2. 길을 그릴 지도 리스트 그리기
    graph = [[0] * (MX+2) for _ in range(MY+2)]

    #3. 1로 먼저 안쪽 다 칠하기
    for x,y,x2,y2 in rect:
        for i in range(y,y2+1):
            for j in range(x,x2+1):
                graph[i][j] = 1

    #4. 테두리 제외하여 직사각형 내부 모두 0으로 채우기
    for x,y,x2,y2 in rect:
        for i in range(y+1,y2):
            for j in range(x+1,x2):
                graph[i][j] = 0
    
    #5. 도착하면 갯수 저장
    start = (chaX*2,chaY*2)
    end = (itX*2,itY*2)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque([start])

    while queue:
        x,y = queue.popleft()
        if (x,y) == end:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if graph[ny][nx] == 1:
                graph[ny][nx]+=graph[y][x]
                queue.append((nx,ny))

    return graph[y][x]//2


print(solution(rect,characterX,characterY,itemX,itemY))