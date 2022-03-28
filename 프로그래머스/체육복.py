# n은 정수,lost는 리스트,reserve는 리스트
   
def solution(n, lost, reserve):
    # set의 특징은 중복을 허용하지 않고 순서가 없다는 것이다.
    # 그럼 왜 set을 사용할까? 다른 집합자료형에 비해 교집합,합집합,차집합을 쓸때 유용하다.
    # 이 문제는 여분을 가진사람과 체육복이 없는 사람을 비교하면 되는문제이기때문이다.
    
    # 1-1. set은 중복이 안되고 순서가 없다는 특징을 이용하여 여벌을 가진사람과 여벌이 없는사람이 누구인지 파악한다.(차집합을 이용)
    # set(reserve)-set(lost) 이걸통해 여분을 가진사람만 찾을수있다.
    reserve_only=set(reserve)-set(lost)
    # set(lost)-set(reserve) 이걸통해 여분이 아에 없는사람만 찾을수있다.
    lost_only =set(lost)-set(reserve)
    
    #1-2. 앞뒤의 인덱스를 저장하여 값을 비교한다.
    # _reserve안에 앞뒤의 인덱스를 저장한다.back->b, front->f
    for reserve in reserve_only:
        front = reserve-1
        back=reserve+1

        #1-3. if elif를 통해 만약 앞에조건문이 먼저 실행되면 뒤에껀 실행안되도록하여 lost의 값을 지우도록한다.
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
            
    #1-4. 전체 인원에서 lost에 남아있는 인원수만큼 빼준값을 리턴해준다.
    return n - len(lost_only)   


def solution(n, lost, reserve):
    answer = 0
    # 2-1. 체육복을 모두 가지고있다는 가정하에 배열을 만든다.
    # 배열을 사용하여 -1:체육복을 잃어버린사람, 0:체육복을 1개가지고잇는 사람, 1: 체육복 여벌을 가지고 있는 사람
    # 만약 인원수만큼 배열을 선언하게 되면 몇개의 조건문을 더 추가해야한다.
    # 배열을 크기를 2개늘려주게 되면 조건문실행을 줄여주며 인덱스 번호를 1번부터 사용할수있다
    arr=[0]*(n+2)
    
    # 2-2. 체육복이 없는 인원과 체육복이 있는 인원을 파악한다.
    # 체육복을 잃어버린 사람은 -1
    for i in lost:
        arr[i]-=1
    # 여벌을 가진사람은 +1
    for i in reserve:
        arr[i]+=1

    # 2-3. 반복문을 통해 1번부터 n번까지 실행하며 앞뒤의 값들중 0보다 큰값(여벌이 있는사람),0보다 작은값(체육복이 없는 사람을 찾는다.)
    for i in range(1,n+1):
        if arr[i] > 0 and arr[i-1]<0:
            arr[i]-=1
            arr[i-1]+=1
        elif arr[i]>0 and arr[i+1]<0:
            arr[i] -=1
            arr[i+1]+=1  

    #2-4 . for문을 통해 arr[i]의 값이 1보다 큰숫자들을 찾고 answer을 더해준다. 
    for i in range(1,n+1):
        if arr[i]>=0:
            answer+=1

    return answer


def solution(n, lost, reserve):
    #[표현식 for 항목 in 반복 가능 객체 if 조건]
    #_reserve 리스트 안에는 for r의 lost배열에 있지않는 reserve값들을 집어넣는다
    _reserve = [r for r in reserve if r not in lost]
    
    #_lost 리스트 안에는 for r의 reserve배열에 있지않는 lost값들을 집어넣는다
    _lost = [l for l in lost if l not in reserve]

    # _reserve안에 앞뒤의 인덱스를 저장한다.back->b, front->f
    for r in _reserve:
        f = r - 1
        b = r + 1
        # if elif를 통해 만약 앞에조건문이 먼저 실행되면 뒤에껀 실행안되도록하여 lost의 값을 지우도록한다.
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
        # 전체 인원에서 lost에 남아있는 인원수만큼 빼준값을 리턴해준다..
    return n - len(_lost)

print(solution(5,[2,3,4],[3,4,5] ))

# 5,[2,3,4],[3,4,5]
# 3,[1,3],[2] 2
# 5,[1,2,3,4],[5] 2
# 5,[1, 5],[2,3,4] 5
# 5,[2, 4],[1, 3, 5] 5
# 5,[2, 4],[3] 4
# 3,[3],[1] 2
# counter클래스는 딕셔너리 형태..!특정조건으로 함수를 구할때!사용된다.