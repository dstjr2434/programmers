
# def solution(participant, completion):
#     answer = ''
#     # 1-1. participant,completion가 리스트형태로 들어오기때문에 이것을 sort시킨다.
#     participant.sort()
#     completion.sort()

#     # 1-2. for문을 동작시켜서 배열의 자리에 다른 인원이 있으면 해당인원이 완주하지 못한 것
#     a=len(completion)-1
#     for i in range(len(completion)):    
#             if participant[i]!=completion[i]:
#                 return participant[i]
#     # 1-3. 완주자의 마지막배열까지 for문을 돌았는데 없으면 참가자의 마지막 인원이 완주를 못한것
#     if participant[len(completion)-1]==completion[len(completion)-1]:
#         return participant[len(participant)-1]




# def solution(participant, completion): 
#     # 해시함수로 쓴 해시값을 받고 그 값을 저장하기 위한 hash_sum
#     hash_sum = 0 
#     dic = {} 
#     # 2-1. 참가자의 이름들을 해시값으로 변경
#     for i in participant: 
#         hash_val = hash(i)
#         # 2-2. 해시값과 참가자의 이름을 딕셔너리에 저장
#         dic[hash_val] = i 
#         # 2-3. 참가자의 해시결과를 저장
#         hash_sum += hash_val
#     # 2-4. 해시결과를 완주자 목록에서 빼면서 남은 인원의 해시값을 찾아냄
#     for i in completion: 
#         hash_sum -= hash(i) 
#     answer = dic[hash_sum] 
#     return answer

# def solution(participant, completion):
#     # 3-1. 참가자,완주자의 이름을 sort시킴
#     participant.sort()
#     completion.sort()
#     # 3-2. for 문을 동작하여 참가자와 완주자를 zip을 통해 하나의 튜플형태로 만들어 놓는다.
#     for p,c in zip(participant, completion):
#         # 3-3. 튜플형태로 만드는 과정중에서 참가자와 완주자가 다르면 참가자의 이름을 리턴
#         if p != c:
#             return p
#     # 3-4. zip이 끝까지 만들었는데 모두 같은이름이면 pop을 통해 마지막 참가자의 이름 리턴
#     return participant.pop()

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]   ))

# from collections import Counter
# def solution(participant, completion): 
#     # 4-1.participant의 counter를 구한다
#         count_part=Counter(participant)
#     # 4-2.completion의 counter를 구한다.
#         count_comple=Counter(completion)
#     # 4-3.둘의 차를 구하고,key를 읽어온다.
#         answer=count_part-count_comple
#         # 4-4. 딕셔너리 형태로 출력되는 값을 리스트 형태로 바꿔주는 과정을 거쳐야한다.
#         answer=list(answer.keys())[0]
#         return answer

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]   ))