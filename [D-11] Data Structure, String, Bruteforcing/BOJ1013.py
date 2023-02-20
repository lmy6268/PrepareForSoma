#Contact
#https://www.acmicpc.net/problem/1013
# import re
# import sys
# input = sys.stdin.readline
# n = int(input())
# for i in range(n):
#     line = input().rstrip()
#     m = re.fullmatch("(100+1+|01)+", line)
#     if m == None:
#         print("NO")
#     else:
#         print("YES")

#오토마타 전이도를 사용한 방법
#     0   1
# 0   1   2
# 1   1   3
# 2   4   F
# 3   1   2 -> 01+
# 4   5   F
# 5   5   6
# 6   1   7 -> 100+1+
# 7   8   7 -> 100+1+
# 8   5   0
import sys
input = sys.stdin.readline

def check(state, char):
    case0 = [1,1000,4,1,5,5,1,8,5]
    case1 = [2,3,1000,2,1000,6,7,7,0]
    if char == '0':
        return case0[state]
    if char == '1':
        return case1[state]


n = int(input())
for i in range(n):
    line = input().rstrip()
    state = 0
    flag = False
    for i in line:
        try:
            state = check(state,i)
        except IndexError:
            print("NO")
            flag =True
            break
    if state in (0, 3, 6, 7):
        print("YES")
    elif not flag :
        print("NO")
