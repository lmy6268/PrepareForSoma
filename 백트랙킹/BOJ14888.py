import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
add,sub,mul,div = list(map(int, input().split()))
m = 10**10
M = -10**10


def dfs(cur_result, add, sub, mul, div, depth):
    global m,M

    if depth == n:
        m = min(cur_result, m)
        M = max(cur_result, M)
        return

    if add > 0:
        add -= 1
        dfs(cur_result+num[depth], add, sub, mul, div, depth+1)
        add += 1

    if sub > 0:
        sub -= 1
        dfs(cur_result-num[depth], add, sub, mul, div, depth+1)
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(cur_result*num[depth], add, sub, mul, div, depth+1)
        mul += 1

    if div > 0:
        div -= 1
        # 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
        # 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
        dfs(-((-cur_result)//num[depth]) if cur_result<0 and num[depth]>0 
            else cur_result//num[depth], 
            add, sub, mul, div, depth+1)
        div += 1

dfs(num[0],add,sub,mul,div,1)
print(M,m,sep="\n")