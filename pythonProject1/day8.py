### 예외 처리
# 어떤 에러가 발생했을때 그 에러에 대해 처리를 하기 위함이다.
# 에러라는 것은 어떤 결합이나 실책 등 잘못된것이다.

# 컴퓨터에서는 문자를 입력해야하는데 숫자를 입력하거나 하는 것 등

# 간단한 계산기를 예제로 사용한다.
"""
print("나누기 전용 계산기입니다.")
num1 = int(input("나눌 수를 입력하세요 : "))
num2 = int(input("나누고 싶은 수를 입력하세요 : "))

print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
"""
# 그런데 여기서 input에 숫자가 아닌 문자열이나 문자를 적게 되면 에러가 발생한다.(ValueError)


"""
# 예외처리는 try를 사용한다.
import sys
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("나눌 수를 입력하세요 : "))
    num2 = int(input("나누고 싶은 수를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다!!",file=sys.stderr)
except ZeroDivisionError as err:
    print(str(err),file=sys.stderr)


import sys
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("나눌 수를 입력하세요 : ")))
    nums.append(int(input("나누고 싶은 수를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다!!",file=sys.stderr)
except ZeroDivisionError as err:
    print(str(err),file=sys.stderr)
except Exception as err:
    print("파악하지 못한 에러가 발생하였습니다.")
    print(err)



import sys
### 의도적으로 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError        # 에러 가져오기!! ValueError로 취급
    print("{0} / {1} = {2}".format(num1,num2,int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력해 주세요",file=sys.stderr)
except Exception as err:
    print("알 수 없는 에러 발생 : "+ str(err))



### 사용자 정의 예외처리

# 직접에러를 정의해서 에러를 만들수도 있다.
import sys
class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self,msg): # 메시지를 어떻게 찍을건지 정할수도 있다.
        self.msg = msg
    def __str__(self):
        return  self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : ({0} , {1})".format(num1,num2))        # 내가 정의한 에러 가져오기!! msg던지기
    print("{0} / {1} = {2}".format(num1,num2,int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력해 주세요",file=sys.stderr)
except BigNumberError as BigNumErr:
    print("큰 숫자 에러 발생 : "+ str(BigNumErr)+"\n한자리 숫자만 입력해 주세요!!")



### Finally
# finally는 예외처리중에서 정상적으로 처리가 되건 오류가 발생하던 무조건 실행되는 부분이다.

import sys
class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return  self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : ({0} , {1})".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력해 주세요",file=sys.stderr)
except BigNumberError as BigNumErr:
    print("큰 숫자 에러 발생 : "+ str(BigNumErr)+"\n한자리 숫자만 입력해 주세요!!")
finally:
    print("계산기를 이용해 주셔서 감사합니다.")    # 잘 작동하는지의 여부에 상관없이 무조건 실행됩니다.


"""

### 예외처리 퀴즈

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메시지: "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 #홀 안애는 현재 만석, 대기번호 1번부터 시작
try:
    while(True):
        print("[남은 치킨 : {0}] ".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까??"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                  .format(waiting,order))
            waiting +=1
            chicken -=order
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as soldout:
    print("재료가 부족합니다.")
    print(str(soldout))
except Exception as err:
    print("파악하지 못한 에러")

