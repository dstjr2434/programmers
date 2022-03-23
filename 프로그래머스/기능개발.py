import queue


progress=[95, 90, 99, 99, 80, 99]
speed=[1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):

    answer = []
    count=0

    while progresses:
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
        if progresses[0]>=100:
            while progresses and progresses[0]>=100:
                progresses.pop(0)
                speeds.pop(0)
                count=count+1
            answer.append(count)
        count=0       
    return answer

print(solution(progress,speed))