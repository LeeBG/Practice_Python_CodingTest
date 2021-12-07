"""



### 함수
# 함수는 어떤것을 하나의 박스에 담아서 어떤 연산에 대한 결과를 반환해준다.

def open_account(): #함수정의: def 함수이름:
    print("새로운 계좌가 생성되었습니다.")   #함수의 내용

open_account() # 함수를 호출


### 전달값과 반환값
def open_account(): #함수정의: def 함수이름:
    print("새로운 계좌가 생성되었습니다.")   #함수의 내용

def deposit(balance,money):#입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다. ".format(balance+money))
    return balance+money
def withdraw(balance,money):#출금
    if(balance >= money):
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance
def withdraw_night(balance,money): #저녁에 출금
    commission = 100 # 수수료 100원(저녁)
    return commission, balance-money-commission     # 튜플형식으로 반환해준다.(여러개의 값)

balance = 0 # 잔액
balance = deposit(balance,1000)#1000원 입금
# balance = withdraw(balance,2000) # 잔액부족
# balance = withdraw(balance,500)
commission,balance = withdraw_night(balance,500)
print("수수료{0}원이고, 잔액은{1}원 입니다.".format(commission,balance))



### 기본값

def profile(name,age,main_lang):# 이름,나이,주 사용 언어
    print("이름: {0},\t나이: {1},\t주 사용 언어:{2}" \
          .format(name, age, main_lang))

profile("유재석",20,"파이썬")
profile("김태호",25,"자바")

# 같은 학교 같은 학년 같은 반 같은 수업. => 이 때 사용하는 것이 기본값

def profile(name,age = 17,main_lang="파이썬"):# 같은 나이,주 사용 언어
    print("이름: {0},\t나이: {1},\t주 사용 언어:{2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")
# 결과
# 이름: 유재석,	나이: 17,	주 사용 언어:파이썬
# 이름: 김태호,	나이: 17,	주 사용 언어:파이썬




### 키워드 값

# 이런식으로 함수에서 전달받는 매개변수의 값을 키워드를 이용해서 함수를 호출하면 순서가
# 바뀌어도 키워드에 해당하는 값이 순서가 뒤섞여 있어도 잘 찾아서 대입할 수 있다.

def profile(name,age,main_lang):
    print(name,age,main_lang)

profile(name="유재석",main_lang="파이썬",age=20) # 키워드를 이용해서 함수를 호출
profile(main_lang="자바",age=25,name="김태호")





### 가변인자

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end="")
#     print(lang1,lang2,lang3,lang4,lang5)


def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end="")
    # print(*language)
    for lang in language:
        print(lang,end=" ")
    print()

profile("유재석",20,"python","Java","C","C++","C#")
profile("김태호",25,"Kotlin","Swift","","","")




### 지역변수와 전역변수
# 지역변수는 함수 내에서만 사용할 수 있는 변수(함수 호출과 끝까지만)
# 전역변수는 함수 바깥의 전역에서 사용할 수 있는 변수

# 이번에는 군대의 총을 예로 든다.
import math

gun = 10 # 전역변수 gun - 총의 총 갯수
def checkpoint(soldiers):  # 경계근무
    global gun # 전역 공간에 있는 gun 사용한다고 선언
    gun = gun - soldiers        # 오류가 발생
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):  # 경계근무
    gun = gun - soldiers        # 오류가 발생
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun          #변경된 값을 리턴

print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 두명이 경계 근무를 나감(총기 반출)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0} ".format(gun))

## global 사용x 일 때 실행 결과
# 전체 총 : 10
# [함수 내] 남은 총 : 18
# 남은 총 : 10



### Quiz) 표준 체중을 구하는 프로그램을 작성하세요

# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
#   남자 : 키(m) x 키(m) x 22
#   여자 : 키(m) x 키(m) x 21

# 조건 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 175 남자의 표준 체중은 67.38kg입니다.

import math


def std_weight(height, gender):
    if gender == "남자":
        print(height)
        weight = height**2 * 22
        return weight
    elif gender == "여자":
        weight = height**2 * 21
        return weight
    else:
        print("성별을 잘못 입력하셨습니다.")


while True:
    gender = str(input("성별을 입력하세요 (남자,여자) : "))
    height = int(input("키를 입력하세요 (cm) "))
    weight = round(std_weight(height / 100, gender), 2)
    print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))


"""

