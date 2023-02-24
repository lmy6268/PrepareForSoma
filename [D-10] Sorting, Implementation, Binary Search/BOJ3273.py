#두 수의 합
# https://www.acmicpc.net/problem/3273
import sys;input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
x = int(input())
left,right = 0,n-1
cnt=0
while left<right:
    #일치하는 경우에는 왼쪽 포인터를 1 증가
    if arr[left] + arr[right] == x:
        cnt+=1 #쌍 추가 
        left +=1
    #
    elif arr[left] + arr[right] > x:
        right-=1
    else:
        left +=1
print(cnt)


