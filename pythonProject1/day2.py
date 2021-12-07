''' 파이썬 문법 끝내기 '''

from random import *

'''
print(5>10)
print(10>5)

### 숫자 처리 함수
print(abs(-5)) #5 절댓값
print(pow(4,2)) #4의 2제곱
print(max(5,12)) # 최댓값
print(max(5,12,15)) # 최댓값
print(min(3,14)) #최솟값
print(round(3.14)) #3.14반올림
print(round(4.99)) # 5 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) #제곱근 4




### 랜덤함수 : 랜덤이라고 하면 그야말로 난수이다.

print (random()) # random은 0.0 ~ 1.0 사이의 임의의 값을 생성한다.
print(random()*10) # 0.0에서 10.0 미만의 임의의 값을 생성한다.
print(int(random()*10)) # 0에서 10 미만의 임의의 값을 생성한다.
print(int(random()*10)+1) # 1 ~ 45이하의 임의의 값을 생성한다.

print(int(random()*45)+1) #1~45이하의 임의의 값 생성
print(randrange(1,45)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성
print(randrange(1,46)) # 1부터 45 미만의 임의의 값 생성

print(randint(1,46)) # 1부터 45 이하의 임의의 값 생성
print(randint(1,46)) # 1부터 45 이하의 임의의 값 생성
print(randint(1,46)) # 1부터 45 이하의 임의의 값 생성
print(randint(1,46)) # 1부터 45 이하의 임의의 값 생성

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었다. 월 4회 스터디를 하고 3번은 온라인 1번은
# 오프라인으로 진행한다.
# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
# 조건 1. 랜덤으로 날짜를 뽑는다. 월별 날짜는 최소일수 고려 28일 이내로 정함
# 조건 2. 매월 1~3일은 스터디 준비를 해야하므로 제외
studyDate = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(studyDate)+"일로 선정되었습니다.")



### 문자열

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요.
여러줄에 걸친 문자열 \"\"\"
"""
print(sentence3)


### 슬라이싱
# 주민등록번호로 예시
jumin = "960528-1234567"

print("성별 : "+jumin[7])
print("연도 : "+jumin[0:2]+"년생입니다.")
print("월 : "+jumin[2:4]+"월생입니다.")
print("월 : "+jumin[4:6]+"일생입니다.")
print("생년월일 : "+jumin[:6]) # 처음(0)부터 주소 6직전까지
print("주민 뒤 7자리 : "+jumin[7:]) # 7부터 끝까지
print("주민 뒤 7자리를 거꾸로 : "+jumin[-7:]) #-7부터 끝까지

### 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python)) #문자열의 길이를 반환하여 준다.
print(python.replace("Python","Java")) #"Python"이라는 문자를 찾아서 "Java"로 대체해준다.

index = python.index("n")
print(index)
index = python.index("n",index+1) # 6번째 부터 다시 찾아서 n의 index찾기
print(index)

print(python.find("Java")) # 원하는 값이 없을 때에는 -1반환
#print(python.index("Java")) # 원하는 값이 없을 때에는 오류와 함께 프로그램 종료

print("hi")

print(python.count("n")) # "n"이 python에서 총 몇번 나왔는가


###문자열 포맷

print("a"+"b") # 문자열을 합칠 때 +를 이용한 붙이기
print("a","b") # 문자열을 합칠 때 +를 이용한 띄어서 붙이기

# 문자열 포멧 지정 방법 1
print("나는 20살입니다.")
print("나는 %d살입니다." % 20) # % 원하는 값 을 %d의 위치에 넣는다는 것이다.
print("나는 %s을 좋아야요." % "파이썬") # %s는 문자열을 대입시켜준다.
print("Apple 은 %c로 시작해요 " % 'A') # %c는 하나의 문자을 대입시켜준다.
# %s를 주로 사용한다.

print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

# 방법2
print("나는 {}살입니다.".format(20)) #format() 안에 있는 겂을 {}안에 대입한다.
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간")) #{}안에 주소를 넣으면 format안의 순서에 맞게 사용가능하다.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="빨간")) #format안에 변수를 선언해서 {}안에 변수를 널고 사용가능
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간",age=20)) #순서상관없이 원하는 문자를 출력 가능

# 방법 4 (python 버전 3.6이상 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #이렇게 하면 중괄호 속에 이 변수는 실제 변수에 저장된 값을 가져다 쓸 수 있다.



### 탈줄문자

print("백문이 불여일견 \n백견이 불여일타") # \n을 사용하면 줄바꿈으로 문자열을 출력한다.

# 또 다른 탈출 문자
# \"\' : 문자 내에서 따옴표
print("저는 \"파이썬 코딩초보\" 입니다") # 우리가 print문 안에 큰 따옴표를 사용하기 위해서는 \" 백슬레시 큰따옴표 사용
print("저는 '파이썬 코딩초보' 입니다") # print문 안에 작은 따옴표 사용

# \\: 문장 내에서 \ -> 주로 파일의 경로를 문자열로 사용할 시
print("C:\\Users\\Nadocoding\\Desktop")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # \r을 사용하면 커서를 맨 앞으로 가져와서 Pine이라는 글자가 "Red " 부분을 덮는다.

# \b : 백스페이스 (한 글자 삭졔)
print("Redd\bApple") # Redd이후에 백스페이스를 하니까 한 글자를 삭제한 후 Apple을 출력한다.

# \t : 탭
print("Red\tApple") # Red뒤에 여러칸을 띄운후에(한 tab)을 띄운 후 Apple출력

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 규칙1 : http://부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

url = "http://naver.com"
if(url.find("http") != -1 or url.find("https")!=-1):
    password = url.replace("https://","")
    password = url.replace("http://", "")
    password = password[:password.index(".")]
    count = len(password)
    password = password[:3]+str(count)+str(password.count("e"))+"!"

print("생성된 비밀번호:",password)


'''
