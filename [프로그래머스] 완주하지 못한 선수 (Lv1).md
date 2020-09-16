# 해시 > 완주하지 못한 선수 (Level 1)
문제 : https://programmers.co.kr/learn/courses/30/lessons/42576

## 문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

## 제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

## 입출력 예

| participant |	completion | return |
| --- | --- | --- | 
| [leo, kiki, eden]	| [eden, kiki] | leo |
| [marina, josipa, nikola, vinko, filipa] |	[josipa, filipa, marina, nikola] | vinko |
| [mislav, stanko, mislav, ana] | [stanko, ana, mislav] | mislav |

____

> #### < Code : Python >
```python
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
```

## 문제 리뷰
- 참가자 중 단 한명만 마라톤에 완주하지 못했기 때문에, 참가자와 완주자는 한명 차이
- 두 리스트를 정렬시키면 같은 순서로 정렬되므로 참가자 리스트에는 있으나, 완주자 리스트에는 존재하지 않으면 해당 참가자가 완주하지 못한 선수이다.
- 따라서 참가자 리스트를 기준으로 비교하여 같은 인덱스의 값이 일치하지 않았을 때를 찾아내면 된다. 또한, 마지막까지 추출되지 않으면 완주자 리스트에는 비교대상이 더이상 없기 때문에 해당 참가자가 완주하지 못한 것으로 간주하면 된다.