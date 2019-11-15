'''
초기코드 => [1, 6, 5, 4, 3, 2]
결과가 이렇게 나왔다 이것은 조건문에 left를 기준으로 하고
첫 번째 반복에서 left 값이 증가하였지만 그 이후로는
조건문에 걸릴 수가 없어서 계속 else 문이 동작한 것이다.
반복문이 돌아가면서 영향을 받는 변수는 idx이고
조건문에는 left가 아닌 idx의 변화에 따라 if/else가
한번씩 번갈아가며 동작할 수 있도록 해주어야 한다.
'''
def solution(arr):
    left, right = 0, len(arr) - 1
    idx = 0
    answer = [0 for _ in range(len(arr))]
    while left <= right:
        if idx % 2 == 0: # 정상적인 결과 출력 [1, 6, 2, 5, 3, 4]
            answer[idx] = arr[left]
            left += 1
        else:
            answer[idx] = arr[right]
            right -= 1
        idx += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")