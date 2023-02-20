#오큰수
# # 시간초과 코드
# import sys; input = sys.stdin.readline
# input()
# Lstk = list(map(int,input().split())) #제공되는 데이터 배열
# Lstk.reverse() #O(N)
# while Lstk: #O(N)
#     flag = False
#     data = Lstk.pop() #O(1)
#     if len(Lstk) ==0:
#         print(-1,end=" ")
#     else:
#         for i in range(len(Lstk)-1,-1,-1): #O(N)
#             if Lstk[i] > data:
#                 print(Lstk[i],end=" ")
#                 flag = True
#                 break
#         if not flag:
#            print(-1,end=" ")

'''
스택의 활용방안을 알게된 문제 
-> 값을 직접 넣는 게 아닌 인덱스를 넣어 접근하도록 함
-> 이미 확인한 값은 다시 확인하지 않도록 함. 
'''

import sys; input = sys.stdin.readline
n =int(input())
A = list(map(int,input().split())) #제공 배열
answer = [-1] * n #정답 배열을 -1로 채움 (값이 없을 떈 -1을 출력해야 하므로)
stack = [0]
for i in range(1,n):
    # 만약 스택이 비어있지 않고, 스택 상단의 인덱스 위치의 수열 값이 현재 수열의 값보다 작은 경우에만 루프를 돌음 
    while stack and A[stack[-1]]< A[i]: 
        answer[stack.pop()] = A[i]  
    stack.append(i) #현재 인덱스를 스택에 추가 
print(*answer) #순회하여 출력
