"""
### 표준입출력
import sys

print("Python","Java", "JavaScript",sep=" vs ") #sep은 ,로 구분된 문장 사이에 sep의 내용을 끼워 넣는다.
print("Pythonn","Java",sep=",",end="?") # end는 문장의 끝부분을 ?로 바꿔달라는 것(default는 줄바꿈\n)

print("Python","Java",file=sys.stdout) #표준 출력
print("Python","Java",file=sys.stderr) #따로 에러 처리(붉은 글씨)

scores = {"수학":0,"영어":50,"코딩":100} # 성적 딕셔너리
for subject, score in scores.items(): # 딕셔너리에서 키값을 들고올때 .items
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4),sep=":") # 8칸의 공간을 확보해서 왼쪽으로 정렬하고, 점수는 4칸 왼쪽정렬


# 은행 대기순번표
# 001,002,003, ...
for num in range(1,21):
    print("대기완료 : "+str(num).zfill(3)) #3크기 만큼의 공간을 확보하고 값이 없는 공간은 0으로 채워넣음
    # 001,002,003

# 표준입력타입
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력으로 값을 받게 되면 그것은 무조건 문자로 받게 되어있다.
print("입력하신 값은 "+answer+"입니다.")



### 다양한 출력 포맷
# 빈자리는 빈 공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 + 로 표시, 음수일때에는 -로 표시
print("{0: >+10}".format(500))  # +를 붙이면 양수일때에도 + 부호를 붙임
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_>10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마를 찍어주는데 추가적으로 +-부호
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기 (부호 콤마 포함 최대 30자리)
print("{0:^<+30,}".format(100000000000))
print("{0:^<+30,}".format(-100000000000))

#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3)) # 소수점 2째 자리 까지



### 파일 입출력
#파일을 하나 열기
score_file = open("score.txt","w",encoding="utf8") # 쓰기 모드로 열기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() #프로젝트 디렉터리에 score.txt라는 파일이 하나 생성이 되고 내용이 써진다.


score_file = open("score.txt", "a" ,encoding="utf8") # 어떤 내용이 존재하는 파일에 추가를 하고 싶으면 "a" appand
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write에서는 줄바꿈이 따로 없기 때문에
score_file.close() # 닫기




# 파일 내용 읽어오기

score_file = open("score.txt","r",encoding="utf8") #read모드
print(score_file.read())
score_file.close()


# 한줄 한줄 불러와서 어떠한 처리를 하고 싶다면
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="")# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file.close()


# 파일의 내용의 길이를 모를때 한줄씩 가져오는 방법 1
score_file = open("score.txt","r",encoding="utf8")
while True: #계속해서 반복문을 수행
    line = score_file.readline() # 한 줄 씩 불러옴
    if not line:
        break # 반복문 탈출
    print(line)
    # print(line, end="") # 줄바꿈 안하는 버전
score_file.close()



# 파일의 내용의 길이를 모를때 한줄씩 가져오는 방법 2
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list 형태로 저장 여러줄을 한번에 가져와서 리스트형태로 저장 readlines()
for line in lines:
    print(line, end="")
score_file.close()



### pickle
# pickle이란 프로그램 상에서 우리가 사용하고 있는 데이터를 파일형태로 저장을 하는것이다.
# 그러며는 파일을 누군가에게 주면 pickle을 이용해서 또 쓸 수 있는 것이다.

import pickle

# profile_file = open("profile.pickle","wb") # 새로운 파일 profile.pickle이라는 파일 #b는 바이너리 타입(pickle 사용 시 필수)
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]} # 프로필 데이터
# print(profile)
#
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file(profile_file)에 저장
# ## profile.pickle이라는 파일이 하나 추가되면서, profile의 내용이 저장이 되었다.
# profile_file.close()


profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)  #file에 있는 데이터를 profile에 불러오기(변수에 저장해서 쓸 수 있다.)
print(profile)
profile_file.close()



### with

#지금까지는 파일에 관한 작업을 할때 파일을 열고(open) 어떤 처리 후 닫아서(close) 사용했음
#with를 사용하면 더 편하게 작업을 할 수 있음

import pickle

with open("profile.pickle","rb") as profile_file: # profile.pickle이라는 파일을 열어서 profile_file이라는 변수에 데이터 저장
    print(pickle.load(profile_file)) # pickle load한 데이터들을 print(출력)한다.
#close해줄 필요없이 자동으로 close해준다.


# 쓰기도 마찬가지다.
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())  # 파일의 내용을 읽어오기

"""

# Quiz) 당신의 회사에는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
#
# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오

# 조건 : 파일명은 '1주차.txt','2주차.txt' ... 와 같이 만듭니다

week = 1
while week <= 50:
    report_file = open(str(week)+"주차.txt","w",encoding="utf8")
    print("-",str(week)," 주차 주간보고 -",file=report_file)
    print("부서 : ", file=report_file)
    print("이름 : ", file=report_file)
    print("업무 요약 : ", file=report_file)
    report_file.close()
    week+=1