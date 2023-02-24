#바이러스 (0~n-1 번까지의 pc)
import sys;input =sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
def dfs(x):
    count = 1
    visited[x] = True
    if x>-1 and x<n:
        for i in graph[x]:
            if not visited[i]:
                count+=dfs(i)
    return count
for i in range(m):
    x,y = map(int,input().split())
    graph[x-1].append(y-1)
    if not x-1 in graph[y-1]:
        graph[y-1].append(x-1)
print(dfs(0)-1) #1번 컴퓨터 제외
