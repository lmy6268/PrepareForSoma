'''
다음에 손대기로 함..
'''

from collections import deque 

visited = []


#행렬을 회전하는 함수
def spin(maps,n):
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # (n-1 ~ 0, 0)  -> (0, 0 ~ n-1) 
            rotated[i][j] = maps[n-j-1][i]
    return rotated

#퍼즐 조각을 꺼내는 로직
def getPuzzle(puzzles,n):
    puzzleList = []
    for i in puzzles:
        tmp = [[0] * n for _ in range(n)]
        for x,y in i:
            tmp[x][y] = 1

        for _ in range(3):
            tmp = [a for a in tmp if a != [0 for _ in range(len(tmp))] ] # 모든 열이 0인 행 삭제
            tmp = spin(tmp,len(max(tmp)))
            print(puzzleList,tmp)
        puzzleList.append(tmp)
    return puzzleList

def puzBfs(x,y,table,n):
    puzzleXY= [(x,y)]
    queue = deque([(x,y)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n :
                if not visited[nx][ny] and table[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] =True
                    puzzleXY.append((nx,ny))

    return puzzleXY

def solution(game_board,table):
    global visited
    n = len(table)
    visited = [[False] * n for _ in range(n)]
    puzzles = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j]==1:
                puzzles.append(puzBfs(i,j,table,n))

    print(getPuzzle(puzzles,n))

    answer = 0
    return answer


#Test
board =[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table =[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

solution(board,table)