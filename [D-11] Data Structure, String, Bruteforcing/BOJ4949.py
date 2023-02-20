import sys;input = sys.stdin.readline
while True:
    line = input().rstrip()
    stk = [];flag = False
    if line == ".": #온점 하나가 들어오는 경우 입력이 종료됨.
        break
    for i in line:
        if i in ('(','['):
            stk.append(i)
        elif i in (')',']'):
            if not stk: #스택이 비어있는 경우
                print("no")
                flag = True
                break
            else:
                value = stk.pop()
                if i == ')' and value != '(':
                    print("no")
                    flag = True
                    break   
                if i == ']' and value != '[':
                    print("no")
                    flag = True
                    break   
    if not flag:
        if stk: #스택이 비어있지 않은 경우
            print("no")
        else:
            print("yes")