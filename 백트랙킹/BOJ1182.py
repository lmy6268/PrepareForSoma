#반례 모음
'''
5 -2
-1 -1 -1 -1 -1
A: 10

5 0
-7 -3 -2 5 9
A: 2
'''

import sys;input = sys.stdin.readline
#부분수열의 합
n,s = list(map(int,input().rstrip().split()))
arr = list(map(int,input().split()))
cnt= 0
visited = [False]*n

def dfs(now,S,data):
    global cnt

    if now == n: #더이상 가지치기를 하지 않는다.
        return

    if s == S and data: #갯수를 저장한다.
        cnt+=1

    for i in range(now,n):
        if not visited[i]:
            visited[i] =True
            dfs(i,S+arr[i],data+[arr[i]])
            visited[i] =False
    return
dfs(0,0,[])
print(cnt)

    