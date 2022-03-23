# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p,c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant.pop()


def solution(participant, completion):
    answer = ''
    # participant가 리스트형태로 들어오기때문에 이것을 sort시킨다.
    participant.sort()
    
    # completion이 리스트형태로 들어오기때문에 이것을 sort시킨다.
    completion.sort()
    a=len(completion)-1
    for i in range(len(completion)):    
            if participant[i]!=completion[i]:
                return participant[i]
    if participant[len(completion)-1]==completion[len(completion)-1]:
        return participant[len(participant)-1]

print(solution(		["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]   ))
