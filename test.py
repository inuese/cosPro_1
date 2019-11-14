# 다음과 같이 import를 사용할 수 있습니다.
# import math
def compare(s1, s2):
    # 여기에 코드를 작성해주세요.
    answer = 0
    if s1 == min(s1, s2): #s1 short
        for i in range(len(s1)):
            if s1[i:len(s1)] == s2[:len(s1)-i]:
                answer = len(s1[:len(s1)]+s2[len(s1)-i:])
                break
    else: # s2 short
        for i in range(len(s2)):
            if s1[len(s1)-len(s2)+i:len(s1)] == s2[:len(s2)-i]:
                answer = len(s1[:len(s1)] + s2[len(s2)-i:])
                break
    return answer
def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    a = compare(s1,s2)
    b = compare(s2,s1)

    answer = min(a,b)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"

ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")