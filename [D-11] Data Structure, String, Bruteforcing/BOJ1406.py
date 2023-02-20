#리스트를 이용하여 진행하다 보면, 시간초과가 밣생

#다음은 시간 초과 코드
'''
import sys;input = sys.stdin.readline
init =list(input().strip()) #초기에 입력된 문자열
init = [""]+[init[i//2] if(i%2==0) else "" for i in range(len(init)*2-1) ] +[""] #기본 배열 
m = int(input()) #입력할 명령어의 개수
cur = len(init)-1 #현재 커서의 위치
for i in range(m): #O(N)
    cmd = input().split()
    if cmd[0]=='P':
        init.insert(cur,cmd[1]) #O(N)
        init.insert(cur,"") #O(N)
        cur +=2 
    elif cmd[0]=='L': #커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨앞이면 무시됨)
        if cur != 0: 
            cur -= 2
    elif cmd[0]=='D': #커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        if cur != len(init)-1:
            cur+=2
    elif cmd[0] == 'B':#커서 왼쪽에 있는 문자를 삭제함(커서가 문장의 맨앞이면 무시됨)
        if cur != 0:
            init.pop(cur-1) #O(N)
            init.pop(cur-1) #O(N)
            cur -=2

print("".join(init))
'''

#시간초과 방지를 위해 두 개의 스택을 이용한다.
# L,R 스택 이용 (커서 이동에 따른 스택 구분)
# L,R 스택은 커서를 기준으로 나뉘어짐
# L -> 주어진 초기 문장을 삽입 (커서가 문장의 맨끝에 있다고 문제에 제시되어 있으므로)

# 왼쪽으로 커서 옮기는 경우 -> L 스택에 있는 것이 R 스택으로 감
# 오른쪽으로 커서 옮기는 경우 -> R 스택에 있는 것이 L스택으로 감
# 커서 왼쪽에 있는 것을 지움 = L스택에 있는 top을 지움
# 커서 왼쪽에 문자 추가 = L스택의 top에 추가하는 것.

#코드
import sys;input = sys.stdin.readline
L = list(input().strip()) #초기에 입력된 문자열
R = []
m = int(input()) #명령 횟수
for i in range(m):
    cmd = input().split()
    if cmd[0]=='P': #문자 추가
        L.append(cmd[1])
    elif cmd[0]=='L': #커서를 왼쪽으로 한 칸 옮김 
        if len(L)>0:#(커서가 문장의 맨앞이면 무시됨)
            R.append(L.pop())
    elif cmd[0]=='D': #커서를 오른쪽으로 한 칸 옮김 
        if len(R)>0: #(커서가 문장의 맨 뒤이면 무시됨)
            L.append(R.pop())
    elif cmd[0] == 'B':#커서 왼쪽에 있는 문자를 삭제함
        if len(L)>0: #(커서가 문장의 맨앞이면 무시됨)
            L.pop()
R.reverse()
print("".join(L),"".join(R),sep="")