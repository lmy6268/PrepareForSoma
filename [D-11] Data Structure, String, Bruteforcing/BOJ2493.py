# BOJ 17298(오큰수)와 연계문제

import sys;input = sys.stdin.readline
n = int(input())
answer = [0] *n #0으로 배열 초기화 ( 수신 불가인 경우 0을 출력하기 위함)
top = list(map(int,input().split()))
stack = [n-1]
for i in range(n-2,-1,-1):
    #스택이 비어있거나 현재 탑의 위치보다 낮거나 같은 경우 ( 레이저가 수신이 가능한 경우 )
    while stack and top[stack[-1]] <= top[i]:  
        answer[stack.pop()] = i+1  # 번호는 1부터 시작이므로, 답 저장 시 1을 더해줌.
    stack.append(i) #해당 인덱스를 스택에 추가 (다음 탑에서 수신가능한지 파악하기 위함)
print(*answer) #정답을 출력 
