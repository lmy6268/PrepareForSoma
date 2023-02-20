#단어 뒤집기 2
# https://www.acmicpc.net/problem/17413
import sys; input =sys.stdin.readline

s = input().rstrip() #입력으로 들어오는 문자열
stack = [] #태그와 단어를 구분할 스택
res = "" #최종적으로 출력할 결과값 
for i in s:
    if i == '<': #태그를 여는 괄호를 만난 경우
        if stack: #만약 스택에 단어가 있는 경우 
            while stack:
                res+= stack.pop() #결과값에 뒤집힌 단어를 넣어줌
        stack.append(i) #괄호를 스택에 추가 

    elif i == '>': #태그를 닫는 괄호를 만난 경우
        temp =[]
        while stack:
            temp.append(stack.pop())
        temp.reverse() #스택에서 pop하는 경우 값이 뒤집혀서 나오므로 다시 원래대로 뒤집어줘야함. (태그는 그대로 둬야하므로) 
        res+= "".join(temp)
        res+= ">" 

    elif i == ' ':
        if not '<' in stack: #만약 현재 태그가 스택에서 진행되지 않는 경우
            while stack:
                res+=stack.pop() #단어를 뒤집어 결과값에 추가 
            res+= " " #결과값 끝에 공백 추가
        else:
            stack.append(i)
    else:
        stack.append(i)
if stack:
    while stack:
        res+=stack.pop() #단어를 뒤집어 결과값에 추가 
print(res)   

