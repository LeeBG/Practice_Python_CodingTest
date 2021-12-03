
'''
# 분기 if
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




# 반복문 for

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


'''

# 반복문 while
#
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었급니다. {1}번 남았어요".format(customer,index))
#     index+=1  #항상 index가 1보다 크거나 같기 때문에 무한루프
#
customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?? ")

