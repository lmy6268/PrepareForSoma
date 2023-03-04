from collections import deque

#바꿀 수 있는지 확인하는 함수
def canSwitch(str1,str2):
    cnt = 0
    for a,b in zip(str1,str2): #길이가 같으므로 zip 사용 가능
        if a!=b:
            cnt+=1
    return cnt==1
    

def solution(begin,target,words):
    answer = 0
    #만약 target이 words 내부에 없다면 바로 0을 리턴 
    if target in words:
        words = [i for i in words if i!= begin]
        #탈출 조건
        if canSwitch(begin,target):
                answer +=1
                return answer
        queue = deque()
        for i in range(len(words)):
            if canSwitch(begin,words[i]):
                queue.append(words[i])
                del words[i] #방문한 단어 삭제
                answer +=1
                break
        
        while queue:
            begin = queue.popleft()
            #탈출 조건
            if canSwitch(begin,target):
                answer +=1
                return answer
            for i in range(len(words)):
                if canSwitch(begin,words[i]):
                    queue.append(words[i])
                    del words[i] #방문한 단어 삭제
                    answer +=1
                    break
    #만약 target이 없거나 경로가 없는 경우
    return answer
begin = "hit";target = "hot";words = ["hit", "hot", "lot"] 
print(solution(begin,target,words))