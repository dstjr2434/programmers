answers=[1,3,2,4,2]

def solution(answers):
    answer = []
    count=[0,0,0]
    check1=[1,2,3,4,5]
    check2=[2,1,2,3,2,4,2,5]
    check3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i]==check1[i%5]:
            count[0]=count[0]+1
        if answers[i]==check2[i%8]:
            count[1]=count[1]+1
        if answers[i]==check3[i%10]:
            count[2]=count[2]+1
    
    max=0
    answer.append(1)
    for idx,num in enumerate(count,start=1):
        
        if max<num:
            answer.pop()
            answer.append(idx)

            max=num
        elif max==num and max!=0:
            answer.append(idx)
                                             
    return answer