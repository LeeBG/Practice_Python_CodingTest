'''

### 분기 if

weather = "비"
# if 조건 :
#     실행 명령문

if weather == "비" :
    print("우산을 챙기세요.")
elif weather == "미세먼지":  # if조건에 맞지 않는 조건중 해당 조건에 만족할 시
    print("마스크를 챙기세요")
else:                       #명시된 조건 외의 조건
    print("날씨는 맑음")


weather = input("오늘의 날씨는 어떤가요?")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":  # if조건에 맞지 않는 조건중 해당 조건에 만족할 시
    print("마스크를 챙기세요")
else:                       #명시된 조건 외의 조건
    print("날씨는 맑음")

temp = int(input("기온은 어때요??")) #input받은 내용을 정수타입으로 변환
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<=temp and temp <30:
    print("적당한 온도의 날씨네요")
elif 0<= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")




### 반복문 for

print("대기번호 :1")
print("대기번호 :2")
print("대기번호 :3")
print("대기번호 :4")

for waiting_no in [0,1,2,3,4]:
    print("대기번호:{0}".format(waiting_no))

# in에 있는 번호들을 하나씩 돌어가면서 waiting_no를 출력

#순처적으로 커지게 하려면
for waiting_no in range(0,5): #0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): #1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))


# 커피숍 주문

starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 여러가지 반복해야하는 주문을 한번에 출력할 수 있다.




### 반복문 while
#
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었급니다. {1}번 남았어요".format(customer,index))
#     index+=1  #항상 index가 1보다 크거나 같기 때문에 무한루프
#


customer = "토르"
person = "Unknown" #종업원에게 찾아오는 사람
while person != customer:   #토르라는 사람이 올때까지 반복
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?? ")



###continue / break (반복문 내에서 쓰는 제어)

absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue              #스킵하고 다음 반복문주기를 진행
    elif student in no_book:
        print("오늘 수업은 여기까지, {0}는 교무실로 올것.".format(student)) # 책이 없음으로 선생님이 수업 종료
        break #반복문 종료
    print("{0}야, 책을 읽어봐.".format(student))



### 한줄 for 문

# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104,
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man","Thor","I am groot"]
students = [len(i) for i in students]       # 각 리스트항의 문자열길이를 index별로 출력
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man","Thor","I am groot"]
students = [i.upper() for i in students]    # 리스트 내의 모든 문자열을 대문자로 변환
print(students)




### Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요 시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *

user = 0  # 총 탑승 승객
for count in range(1,51):
    time = randint(5,50) # 승객별 소요 시간
    if(5 <= time <= 15):
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(count, time))
        user += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(count, time))

print("총 탑승 승객 {0}명".format(user))

'''