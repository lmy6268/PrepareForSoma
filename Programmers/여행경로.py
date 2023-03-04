# ticket = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"],["JFK", "HND"]]
ticket =[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

'''
완벽한 데이터를 줬다면 풀렸을 해답
----
from collections import deque

def solution(tickets):
    graph = {}
    #1. 항공권 방향에 대한 그래프를 생성
    for tic in tickets:
        st,en = tic
        if st in graph:
            graph[st].append(en)
        else:
            graph[st] = [en]
    #2. 알파벳순으로 빠지므로 pop을 위해 내림차순으로 정렬 
    for tic in graph:
        graph[tic].sort(reverse=True)

    #3. 루트 계산하기
    stPoint ="ICN"
    route = [stPoint]
    queue = deque([stPoint])
    while queue:
        city = queue.popleft()
        #만약 그래프가 비어있지 않고, 현재도시에서 출발하는 항공권이 남아있는 경우
        if graph and city in graph: 
            nxCity = graph[city].pop() #다음 도시
            if not graph[city]: #만약 더이상 사용할 수 있는 항공권이 없는 경우
                del graph[city] #항공권 삭제
            route.append(nxCity) #루트에 저장
            queue.append(nxCity) #큐에 삽입
            
    return route
'''
from collections import deque

# route = []
# visited = []


# def dfs(airport,n,tickets,cnt):
#     global check,route,visited
#     if cnt == len(tickets):
#         check = True        
#     route.append(airport)

#     for i in range(n):
#         #만약 방문하지 않은 공항이고, 시작점이라면
#         if not visited[i] and tickets[i][0] == airport:
            
#             visited[i] = True
#             cnt+=1

#             dfs(tickets[i][1],n,tickets,cnt)

#             #만약 항공권을 다 사용하지 않았다면?
#             if not check:
#                 route.pop() #현재 경로를 제외하고
#                 visited[i] = False #방문기록을 제거

def bfs(airport,tickets):
    n = len(tickets)
    cnt = 0
    tickets.sort(key = lambda x:(x[0], x[1]))
    visited = [False] *n
    route = []
    queue = deque([airport])
    check = False
    while queue:
        start = queue.popleft()
        route.append(start)
        
        
        for i in range(n):
            #티켓을 사용하지 않았고, 출발지가 지금 선택된 출발지와 같은 경우
            if not visited[i] and tickets[i][0] == start:
                visited[i] = True
                cnt+=1
                queue.append(tickets[i][1])

                if cnt == len(tickets)-1:
                    check = True
        
            if not check and route:
                route.pop()
                visited[i] = False
               

    return route


    

def solution(tickets):
    return bfs("ICN",tickets)
    # global visited
    # n = len(tickets)
    # visited = [False] *n
    # tickets.sort(key = lambda x:(x[0], x[1]))
    # dfs("ICN",n,tickets,0)
    
    # return route



print(solution(ticket))