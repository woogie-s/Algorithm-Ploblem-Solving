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