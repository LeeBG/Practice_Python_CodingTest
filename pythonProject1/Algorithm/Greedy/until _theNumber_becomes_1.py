import time
# 1이 될 때까지 반복연산
'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정을 반복적으로 '선택'하여 수행한다.
    1. N에서 1을 뺀다.
    2. N에서 K로 나눈다.
단 두번째 연산은 N이 K로 나누어 떨어질 때만 사용할 수 있다.

예를들어) N이 17이고 K가 4라고 가정하자 이때 1번의 과정을 한 번 수행하면
    N은 16이 된다. 이후에 2번의 과정을 두 번 수행하면 N은 1이 된다.
    결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다. 이는
    N을 1로 나누는 최소 횟수이다.
'''
start_time = time.time()
# 입력
N, K = map(int, input().split())
count = 0
print(N, K)
while N != 1:
    if N % K == 0:
        N /= K
        count +=1
    else:
        N -= 1
        count +=1
    
print(count)
    
