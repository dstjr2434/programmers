def solution(priorities, location):
    arr=[]
    answer = 0
 
    # 1-1. 입력값으로 들어온 값과 인덱스번호를 하나의 튜플형태로 묶어준다.
    for idx, num in enumerate(priorities) :
        arr.append((idx,num))
    #  flag=0
    # 1-2.arr의 2번째 요소들의 값을 비교한후 정렬을 시켜준다.
    while arr:
        flag=0
        max=arr.pop(0)
        for element in arr:
            if max[1]<element[1]:
                arr.append(max)
                flag=1
                break
        
        if location==max[0] and flag==0:
            answer+=1
            return answer
        if flag==0:
            answer+=1
print(solution([3,4,1,5,7],3))
# [2, 1, 3, 2],2
# [1, 1, 9, 1, 1, 1],0
# [3,4,1,5,7],3


    # for element in iterable:
    #     if max[0]<element:
    #         return True
    # return False
        
        
        # location==max[0]:
    # for i in range(len(arr)-1): 
    #     if max[1]<arr[i+1][1]:
    #         arr.append(max)
    #         max=arr[i+1]
    #         del arr[0]


# def solution(priorities, location):
#     printer=[(i,p)for i,p in enumerate(priorities)]
#     turn=0
#     while printer:
#         job=printer.pop(0)

#         if any(job[1]<other_job[1] for other_job in printer):
#             printer.append(job)
#         else:
#             turn+=1
#             if job[0]==location:
#                 break
#     return turn

# print(solution([2, 1, 3, 2],2))
