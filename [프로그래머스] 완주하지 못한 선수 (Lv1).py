#!/usr/bin/env python
# coding: utf-8

# ### 해시 > 완주하지 못한 선수 (Level 1)
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/42576

# In[2]:


def solution_notComplete(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    
    for i in range(len(participant)):
        if i == len(participant) - 1:
            answer = participant[i]
            break
            
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    return answer


# In[5]:


# 입출력 테스트
participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
solution_notComplete(participant, completion)


# #### 문제 리뷰
#      - 참가자 중 단 한명만 마라톤에 완주하지 못했기 때문에, 참가자와 완주자는 한명 차이
#      - 두 리스트를 정렬시키면 같은 순서로 정렬되므로 참가자 리스트에는 있으나,
#        완주자 리스트에는 존재하지 않으면 해당 참가자가 완주하지 못한 선수이다.
#      - 따라서 참가자 리스트를 기준으로 비교하여 같은 인덱스의 값이 일치하지 않았을 때를
#        찾아내면 된다. 또한, 마지막까지 추출되지 않으면 완주자 리스트에는 비교대상이
#        더이상 없기 때문에 해당 참가자가 완주하지 못한 것으로 간주하면 된다.
