import sys;input = sys.stdin.readline
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
diff = 10**10

check = [False]*N
def dfs(depth,next):
    global diff,check
    
    '''
    [백트래킹] 
    제한 조건에 도달할 때 값을 체크한다 -> 이 문제에서는 팀 배정이 완료된 경우

    '''
    # 반반으로 팀이 구성된 이때 능력치 합을 구한다.
    if depth == N//2: 
        start = 0 
        link = 0        
        #인원 수 만큼 루프
        for i in range(N):
            #인원 수 만큼 루프
            for j in range(i,N):
                #스타트링크 팀에 배정된 경우 
                if (check[i],check[j]) == (True,True):
                    start += (matrix[i][j]+matrix[j][i])
                #링크 팀에 배정된 경우
                elif (check[i],check[j]) == (False,False):
                    link += (matrix[i][j]+matrix[j][i])
        diff = min(abs(start-link),diff)
        return 

    for i in range(next,N):
        if not check[i]:
            check[i] = True #스타트링크팀에 배정
            dfs(depth+1,i+1)  #DFS 실행
            check[i] = False #링크팀에 배정
    return
dfs(0,0)
print(diff)