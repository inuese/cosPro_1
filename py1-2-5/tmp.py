#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.
    length = 1
    answer = 0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            length+=1
        else : length = 1 #같거나 작을 경우
        answer = max(answer,length)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")