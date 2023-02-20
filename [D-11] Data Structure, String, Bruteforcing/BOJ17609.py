#회문
# https://www.acmicpc.net/problem/17609


# import sys
# input = sys.stdin.readline


# def check(string):
#     left = 0
#     right = len(string)-1
#     #유사회문의 조건이 문자 한 개만 삭제했을 때 회문이 되는 경우이므로, 문자를 최대 한개만 지울 수 있는 장치가 필요
#     rm = False

#     while (left < right):

#         # 앞뒤 문자가 같은 경우
#         if string[left] == string[right]:
#             left += 1
#             right -= 1

#         #앞뒤 문자가 다른경우
#         else:
#             #아직 문자를 한번도 제거하지 않은 상태인 경우
#             if not rm:
#                 #왼쪽에 있는 문자를 제거하고 진행하는 경우
#                 if string[left+1] == string[right]:
#                     print("case1",string[left+1],string[right])
#                     left += 2
#                     right -= 1
#                     rm = True
#                 #오른쪽에 있는 문자를 제거하고 진행하는 경우
#                 elif string[left] == string[right-1]:
#                     print("case2",string[left],string[right+1])
#                     left += 1
#                     right -= 2
#                     rm = True
#                 #두 경우에도 진행이 안된다면 그외 문자열로 판단.
#                 else:
#                     return 2
#             #이미 문자를 하나 제거한 경우
#             else:
#                 return 2  # 그외 문자열인 경우

#     if rm:  # 유사회문인 경우
#         return 1
#     else:  # 회문인 경우
#         return 0


# n = int(input())  # 입력의 수
# for i in range(n):
#     line = input().rstrip()  # 입력 문자열
#     print(check(line))  # 회문, 유사회문 ,일반 문자열 분석

import sys
input =sys.stdin.readline
def check(word,l,r):
	while l < r:
		if word[l] == word[r]:
			l += 1
			r -= 1
		else:
			l_remove = check2(word,l+1,r)
			r_remove = check2(word,l,r-1)
			if (l_remove or r_remove):
				return 1
			else:
				return 2
	return 0

def check2(word,l,r):
	while l < r:
		if word[l] == word[r]:
			l += 1
			r -= 1
		else:
			return False
	return True

t = int(input())
for _ in range(t):
	word = input().rstrip()
	l = 0
	r = len(word)-1
	print(check(word,l,r))
    
