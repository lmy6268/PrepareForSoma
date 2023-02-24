import sys;input =sys.stdin.readline
#dfs 풀이
'''
n = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
numList = []
def dfs(x,y):
    count = 1 #1씩 누적하도록 하기 위함. (만약 2개씩 카운트 해야한다면 2로 수정하면됨.)
    if  x>=n or x<0 or y>=n or y<0 or graph[x][y] == 0 : #종료조건 (범위 초과 혹은 벽을 만나는 경우)
        return False 
    if graph[x][y]== 1 : #아직 방문하지 않은 건물인 경우
        graph[x][y] = 0 #방문처리 
        #상하좌우를 탐색한 결과값을 count 변수에 저장
        count+=sum([dfs(x+1,y),dfs(x-1,y),dfs(x,y+1),dfs(x,y-1)]) 
    #만약 종료가 안된다면 count값을 그대로 반환
    return count
    
for i in range(n):
    for j in range(n):
        if graph[i][j] !=0: #방문하지 않은 경우
            numList.append(dfs(i,j)) #dfs의 결과를 numList에 삽입
numList.sort()
print(len(numList))
for i in numList:
    print(i)
'''
#bfs 풀이
