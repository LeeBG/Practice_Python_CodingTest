# 반복문으로 구현
def factorial_interative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


# 재귀함수로 구현
def factorial_recursive(n):
    if n <=1:
        return 1
    return n* factorial_recursive(n-1)

import time
start_time = time.time()
print("반복적으로 구현 :",factorial_interative(10))
end_time = time.time()
print("반복적 time: ",end_time-start_time)

start_time = time.time()
print("재귀적으로 구현 :",factorial_recursive(10))
end_time = time.time()
print("재귀적 time: ",end_time-start_time)