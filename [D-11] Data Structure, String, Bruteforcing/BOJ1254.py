#팰린드롬 만들기
# https://www.acmicpc.net/problem/1254
import sys; input = sys.stdin.readline

s = input().rstrip()
if s[:] == s[::-1]: #이미 회문인 경우
    print(len(s))
else:
    for i in range(len(s)):
        tmp = s[:]+s[i::-1] #임시로 만들어둔 문자열
        if tmp[:] == tmp[::-1]: #회문인지 확인
            print(len(tmp))
            break
