# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 # nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
#     dfs(0,0)
#     return answer

# def solution(numbers, target):
#     answer = 0
#     visited=[]
#     need_visit=[]
#     def dfs(v):

#     return answer

    
def solution(numbers, target):
    visited=[0]
    answer=0
    while numbers:
        score=numbers.pop(0)
        tmp=[]
        for i in visited:
            tmp.append(i+score)
            tmp.append(i-score)
        visited=tmp
    for i in visited:
        if target==i:
            answer+=1
    return answer

print(solution([5, 2, 1, 1],3))