#키로거 (https://www.acmicpc.net/problem/5397)
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    Astk = []
    Bstk = []
    pwd = list(input().rstrip())  # 입력한 비밀번호와 기타 키들
    for i in pwd:
        if i == '<':
            if Astk:
                Bstk.append(Astk.pop())
        elif i == '>':
            if Bstk:
                Astk.append(Bstk.pop())
        elif i == '-':
            if Astk:
                Astk.pop()
        else:
            Astk.append(i)
    Bstk.reverse() # 여분의 스택에는 거꾸로 값이 저장되기 때문!
    Astk.extend(Bstk)
    print("".join(Astk))
