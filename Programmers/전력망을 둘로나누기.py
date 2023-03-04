from collections import deque

def solution(n,wires):
    graph = [[] for _ in range(n+1)] #인접리스트
    diff = n #최대값으로 설정

    #1. 들어온 입력을 그래프 형태로 표현
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    #2. 계속해서 네트워크를 둘로 나누어가며, 최소의 차이를 보이는 경우를 리턴한다
    def bfs(start):
        
        visited = [False] * (n+1)
        queue = deque([start]) #큐에 시작점 삽입
        visited[start] =True #방문처리

        cnt = 1 #계산 결과 누적

        while queue:
            data = queue.popleft()
            for i in graph[data]:
                #방문하지 않은 경우에만 진행
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    cnt+=1
        return cnt

    #3. 연결부를 for문으로 돌면서 제거, 복구를 반복
    for a,b in wires:

        #연결 제거
        graph[a].remove(b)
        graph[b].remove(a)

        #서브 그래프 각각(a 네트워크, b네트워크)에 대해 bfs 진행
        #각각의 결과값의 차이와 현재 최솟값을 비교 하여 값 업데이트진행
        diff = min(abs(bfs(b)-bfs(a)),diff)

        #연결복구
        graph[a].append(b)
        graph[b].append(a)

    return diff


#TC
n = 9; wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))