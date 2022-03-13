# import math
# import time
# from random import randint

if __name__ == '__main__':

    # family = ['mother','father','sister','brother']
    # family.sort(reverse=True)
    # print(len(family))
    # family.remove(family[3])
    # print('family: ', family)
    # print(family[2])

    '''
    print('직각 삼각형 그리기')
    leg = int(input('변의 길이:'))

    for i in range(leg):
        print('* '* (i + 1))

    area = (leg ** 2)/2.0
    print('area:',area)


#  연습문제 2 사용자에게 정수를 입력받아, 그 수의 제곱을 계산해 출력하는 파이썬 스크립트를 작성하세요.

    print('★제곱계산기★')
    num = int(input('제곱연산을 할 숫자를 입력:'))

    print(num,'의 제곱은',int(math.pow(num,2)))

# 
    for k in range(len(array)):
        print(array[k],end=" ")
        if k % 10 == 0:
            print("")

####################################################################################################
    # 정렬 수행시간 차이

    def selectSort():
        # 선택 정렬 프로그램 성능 측정 시작(시간)
        start_time = time.time()

        # 선택정렬 알고리즘
        for i in range(len(array)):
            min_index = i  # 가장 작은 인덱스
            for j in range(i + 1, len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]  # 스왑

        end_time = time.time()
        print("선택정렬 알고리즘 실행 시간:", end_time - start_time)  # 수행 시간 출력

    #배열에 10,000개의 랜덤 정수 삽입
    array = []
    for _ in range(10000):
        array.append(randint(1,100))

    selectSort()

    # 배열 다시 초기화
    array = []
    for _ in range(10000):
        array.append(randint(1,100))


    # 기본 정렬 라이브러리 사용 측정
    start_time = time.time()

    array.sort()

    end_time = time.time()
    print("라이브러리 정렬 알고리즘 실행 시간 : ",end_time-start_time) #수행 시간 출력

############################################################################################
    # 3 - 1 거스름돈 문제(그리디 알고리즘) greedy
    # 거스름돈으로 동전을 주는 상황에서 1260원을 거슬러줘야하는 상황에서 거슬러 줘야하는 동전의 최소 갯수는??
    # 500, 100, 50, 10원 동전
    start_time = time.time()
    n = 1260
    count =0 # 동전의 총 갯수

    coin_types = [500,100,50,10]

    for coin in coin_types:
        temp = count
        count += n // coin
        n %= coin
        print(coin,"원 짜리 동전",count-temp,"개")

    print(count)
    end_time = time.time()
    print("그리디 알고리즘 실행 시간 ", end_time-start_time)


    # 사전 자료형 관련 함수
    data = dict()

    data['사과'] = "Apple"
    data['바나나'] = "Banana"
    data['코코넛'] = "Coconut"

    key_list = data.keys()
    value_list = data.values()

    print(data)
    print("key_list:",key_list)
    print("value_list:",value_list)

    # 각 키에 따른 값을 하나씩 출력
    for key in key_list:
        print(data[key])

    # 리스트나 튜플은 데이터를 순차적으로 저장한다는 특징이 있다.
    # 하지만 사전자료형은 키-값 쌍으로 데이터를 가진다는 점에서 우리가 원하는
    # 변경 불가능한 데이터를 키로 시용할 수 있다.
    # 파이썬의 사전자료형은 내부적으로 해시테이블을 이용하로 기본적으로 데이터 검색 및 수정에서 O(1)의 시간에 
    # 처리할 수 있다.


    #집합자료형 - 파이썬에서는 집합(set)을 처리하기 위한 집합 자료형을 제공하고 있다. 집합은 기본적으로 리스트 혹은
    #문자열을 이용해서 만들 수 있는데, 집합은 다음과 같은 특징이 있다.
    # - 중복을 허용하지 않는다.
    # - 순서가 없다.
    # - 키가 존재 하지 않고 값 데이터 만을 담게 된다.
    # - 특정 원소 존재하는지 검사하는 연산의 시간 복잡도는 O(1)

    # 집합 자료형 초기화 방법 1 (set()함수 이용)
    data = set([1,1,2,3,4,4,5])
    print(data)

    # 집합 자료형 초기화 방법 2 ({}이용)
    data = {1,1,2,3,4,4,5}
    print(data)

    a = set([1,2,3,4,5])
    b = set([3,4,5,6,7])

    print()
    print("a:", a)
    print("b:", b)
    print("a | b:",a | b) # 합집합
    print("a & b:",a & b) # 교집합
    print("a - b:",a - b) # 차집합
    print()
    # 집합 자료형 관련 함수
    data = set([1,2,3])
    print(data)

    #새로운 원소 추가
    data.add(4)
    print(data)

    #새로운 원소 여러 개 추가
    data.update([5,6])
    print(data)

    #특정한 값을 가지는 원소 삭제
    data.remove(3)
    print(data)
'''
    # if 조건문 사용해 보기
    array = [1, 2, 3, 4, 5]
    array2 = [4, 5, 6, 7, 8]

    a = 8
    if a not in array:
        print(a, "(이)가 안들어가 있음")
    else:
        print(a, "(이)가 있음")

    # 논리 연산자 연습
    if 3 > 0 and 3 < 2:
        print("yes")
    else:
        print("no")

