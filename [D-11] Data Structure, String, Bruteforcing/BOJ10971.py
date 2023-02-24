#외판원 순회 2
#https://www.acmicpc.net/problem/10971

import sys;input = sys.stdin.readline
import math ; MAX = math.inf

n = int(input())  #도시의 수
dp = [[0] * n for _ in range(1<<n)] # 방문 배열 초기화
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

#외판원 순회 진행 함수
def TSP(visit,now): #이미 방문한 도시 체크, 이번에 지날 도시번호
    visit |= (1<<now) #now번 도시 방문 추가 (비트 OR연산)

    #모든 도시를 지난 경우 (시작 지점 제외)
    if visit == (1<<n)-1:
        if arr[now][0] > 0: #비용이 0인 경우 갈 수 없는 경로를 의미
            return arr[now][0]
        return MAX

    #방문 경로에서 현재 위치까지의 최소 비용을 저장
    ret = dp[visit][now]  

    #memorization
    if ret > 0:
        return ret
    
    ret = MAX #초기화

    for i in range(n):
        #now => i번 도시를 아직 방문하지 않았고(visit&(1<<i) == 0), 갈 수 있는 경로가 있는 경우 (arr[now][i] >0)
        if visit&(1<<i) == 0 and arr[now][i] >0:
            #최소 비용 갱신
            ret = min(ret,TSP(visit,i) + arr[now][i])
    return ret

ans = TSP(0,0) #0으로 시작해서 0으로 돌아오는 순회 경로의 최소 비용
print(ans)