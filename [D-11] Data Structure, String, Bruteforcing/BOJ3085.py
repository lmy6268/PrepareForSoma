#사탕게임
#https://www.acmicpc.net/problem/3085

import sys
input = sys.stdin.readline
n = int(input())  # 보드의 크기
board = [list(input().rstrip()) for _ in range(n)]
maxCandy = 0

#사탕의 최대 갯수 확인


def check(candy):
    global maxCandy
    for i in range(n):
        
        cnt = 1
        for j in range(1, n):
            #열 확인
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if maxCandy < cnt:
                    maxCandy = cnt

        cnt = 1
        for j in range(1, n):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if maxCandy < cnt:
                    maxCandy = cnt


for i in range(n):
    for j in range(n):
            if j + 1 <n:
                board[i][j], board[i][j+1] = board[i][j+1] ,board[i][j]
                check(board)
                board[i][j], board[i][j+1] = board[i][j+1] ,board[i][j]# 원상복귀

            if i+1<n:
                board[i][j], board[i+1][j] = board[i+1][j] ,board[i][j]
                check(board)
                board[i][j], board[i+1][j] = board[i+1][j] ,board[i][j]# 원상복귀
print(maxCandy)