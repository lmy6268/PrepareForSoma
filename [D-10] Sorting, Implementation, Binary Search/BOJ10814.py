#나이순 정렬
#https://www.acmicpc.net/problem/10814
import sys;input = sys.stdin.readline
member= []
for i in range(int(input())):
    age, name = input().rstrip().split()
    age = int(age)
    member.append([age,name])
member.sort(key=lambda x:x[0])
for i in member:
    print(i[0],i[1],sep=" ")