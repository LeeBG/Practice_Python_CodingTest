### 표준입출력
import sys

print("Python","Java", "JavaScript",sep=" vs ") #sep은 ,로 구분된 문장 사이에 sep의 내용을 끼워 넣는다.
print("Pythonn","Java",sep=",",end="?") # end는 문장의 끝부분을 ?로 바꿔달라는 것(default는 줄바꿈\n)

print("Python","Java",file=sys.stdout) #표준 출력
print("Python","Java",file=sys.stderr) #따로 에러 처리(붉은 글씨)

scores = {"수학":0,"영어":50,"코딩":100} # 성적 딕셔너리
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), score) # 8칸의 공간을 확보해서 정렬한다.