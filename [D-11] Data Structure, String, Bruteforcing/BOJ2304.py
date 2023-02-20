#창고 다각형
import sys;input = sys.stdin.readline
n = int(input())
pill = [0] * 1001
maxH = 0 ; maxPos = 0 ; lH= 0; rH = 0 ; ans = 0; lastPos = 0
#값 입력 받기
for i in range(n):
    l,h = map(int,input().split())
    if maxH<h: #만약 현재 저장된 최대 높이보다 큰 기둥이 있는 경우
        maxH = h
        maxPos = l
    if lastPos < l:
        lastPos = l
    pill[l] = h # [위치, 높이]

#왼쪽부분 넓이 구하기
for i in range(0,maxPos):
    lH = max(lH,pill[i]) #최고 높이를 갱신
    ans += lH #계속해서 왼쪽부분의 최고 높이를 더해나감

#오른쪽 부분 넓이 구하기
for i in range(lastPos,maxPos,-1):
    rH = max(rH,pill[i])#최고 높이를 갱신
    ans += rH #계속해서 오른쪽 부분의 최고 높이를 더해나감

ans += maxH #가장 높은 높이 더해주기
print(ans) #최종 결과값 출력