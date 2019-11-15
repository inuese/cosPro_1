def func_a(n):
    ret = 1 #ret 값을 곱하기 떄문에 ret 값을 1로 설정했다.
    while n > 0: #자릿수가 0 미만이면 반복문을 탈출한다.
        ret *= 10 #중간 값에서 멈춰야 하기 때문에 자릿수가 그대로 들어오는 것이 아니라 /2를 해주어야 한다.
                  #값을 정수로 받아야 하기 때문에 //2 연산을 해주는 것이 안정적이다.
        n -= 1 # n을 1씩감소시키는걸로 봐서 이 부분에 들어가는건 숫자데이터가 아니라 자리수 데이터이다.
    return ret

def func_b(n):
    ret = 0
    while n > 0: #자릿수가 0 미만으로 가면 반복문을 탈출하고 자릿수를 반환한다.
        ret += 1 #자릿수를 카운트하는 변수 ret
        n //= 10 #//=10 연산을 하면 맨 끝 자리부터 하나씩 사라진다.
    return ret

def func_c(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

def solution(num):
    next_num = num #현재 자리수를 저장한다.
    while True:
        next_num += 1 #게시글 번호를 1 증가시키고 자리수를 구한다
        length = func_b(next_num) #자리수를 구하는 함수
        if length % 2: #자리수가 짝수인지 확인한다. bool 연산자를 조건문 인자로 받기 때문에
            #짝수이면 0(false)이 나올 것이고 #짝수가 아니면 1(True)이 나올 것이다,
            continue #결국 홀수가 나오면 반복문을 continue시켜 짝수가 나올 때 까지 반복하는 것이다.

        divisor = func_a(length//2) #내가 틀렸던 부분
        #func_a의 목적은 중간 인덱스를 잡아주기 위한 자릿수를 리턴하는 함수이고
        #인자로는 전체 자릿수에서 /2를 해주어야한다.
        front = next_num // divisor
        back = next_num % divisor
        #func_a 를 통해 100, 1000의 형식으로 나온 divisor 변수는 게시글 번호로 나누게 되면 다음과 같은 조건을 성립한다.
        #  3-1. 앞 자릿수 절반과 뒷 자릿수 절반을 분리합니다. -> 앞 자릿수와 뒷 자릿수가 나뉘어짐
        front_sum = func_c(front) #func_c는 각 자리수의 합을 구하는 함수다.
        back_sum = func_c(back)
        if front_sum == back_sum: #func_c로 구한 front_sum과 back_sum의 값이 같을 경우 반복문을 탈출한다.
            #그 지점이 경품을 받을 수 있는 게시글 번호이다.
            break

    return next_num - num #경품을 받을 수 있는 게시글 번호에서 현재 게시글 번호와의 차이를 구해
                        #그 값이 앞으로 몇개의 글을 더 써야 경품을 받을 수 있는지에 대한 값이 나온다.


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")