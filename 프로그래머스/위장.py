# def solution(clothes):
#     result=1
#     dic={}
#     #1-1. 총 의상의 수를 입력 받는다.
#     for i in range(len(clothes)):
#         #1-2. 의상의 종류를 해시값으로 만들어준다.
#         # num는 해시값이다.
#         num=hash(clothes[i][1])
    
#         #1-3. 만약에 dic[해시값]이 dic이라는 딕셔너리 리스트에 있다면 dic[해시값]에는 +1 해준다.
#         if num in list(dic.keys()):
#             dic[num]=dic[num]+1
#         #1-3. 해시값이 없다면 새로운 해시맵 선언후 1로 초기화
#         else:
#             dic[num]=1
#     #1-4. 해시맵이 1개라면(의상의 종류가 1개라면) 나올 수 있는 조합의 수는 해시맵의 개수만큼 나올 수 있다.        
#     if len(dic) == 1:
#         answer=list(dic.values())[0]
#     #1-5 이외의 경우는 (의상종류가 가지는 개수+1)*(의상종류가 가지는 개수+1)...    
#     else:
#         arr=list(dic.values())
#         for i in range(len(arr)):
#             arr[i]=arr[i]+1
#             result=result*arr[i]
#     # 아무것도 안입는 경우의 수 1개는 빼야한다.
#         answer=result-1
#     return answer

# # clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# # clothes=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
# # print(solution(clothes))


# def solution(clothes):
#     # 2-1.의상의 종류를 저장할 딕셔너리를 선언해준다.
#     clothes_type = {}
    
#     for c, t in clothes:
#         # 2-2. 의상의 종류가 딕셔너리에 존재하지 않았다면 2로 초기화(2로 초기화시키는 이유는 조합의 갯수가 맨처음들어오는 조합의 수는(0,1)이다)
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         # 2-2. 의상의 종류가 기존에 존재했다면 1만 추가(1만추가하는 이유는 (0,1,2)이렇게 늘어나기 때문이다.)
#         else:
#             clothes_type[t] += 1

#     #곱셈을 해주기 위해 변수선언
#     cnt = 1
#     # 2-3.clothes_type.values()를 사용하게 되면 dict_values([3, 2]) 이런형태로 리스트가 선언된다.
#     # 따라서 for문의 num는 3과 2가 들어가게된다.
#     for num in clothes_type.values():
#         cnt *= num
#     # 2-4.아무것도 안입는 경우의 수 1개는 빼야한다.
#     return cnt - 1

# # clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# # clothes=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
# # print(solution(clothes))

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes)) 
