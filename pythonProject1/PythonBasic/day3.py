from random import *
'''
### 리스트 []

#지하철 칸 별로 10명,20명,30명이 있다고 한다.
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30] # 위에서는 서로다른 변수를 3개 만들었지만 리스트를 사용하면 하나의 변수에 모두 담을 수 있다.
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?

print(subway.index("조세호")) # 1번지에 잘 타고 있다고 뜬다. 0,1,2

# 하하씨가 다음 정류장에서 다음 칸에 탄다면
subway.append("하하")
print(subway)   # 하하 씨가 추가 되었음

# 정형돈씨를 유재석/조세호 사이에 태워봄
subway.insert(1, "정형돈") # (어디에 "누구를")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼낸다. pop()
print(subway.pop()) # 어떤 사람을 뺐는지 알 수 있음
print(subway) # 남은 사람

print(subway.pop()) # 어떤 사람을 뺐는지 알 수 있음
print(subway) # 남은 사람

print(subway.pop()) # 어떤 사람을 뺐는지 알 수 있음
print(subway) # 남은 사람


# 같은 이름의 사람이 몇 명 있는 지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()# 오름차순으로 정렬
print(num_list) #순서대로 정렬된 모습

# 순서 뒤집기
num_list.reverse() #거꾸로 뒤집는다.
print(num_list)

# 모두 지우기
num_list.clear()# 안에 포함되어있던 모든 리스트를 제거
print(num_list)

# 이런 리스트는 자료형에 구애받지 않고 섞어서 쓸 수 있다.
num_list = [5,4,3,2,1]
mix_list= ["조세호",20,True]
print(mix_list)

# 리스트 확장(리스트를 합치기)
num_list.extend(mix_list)
print(num_list) #하나의 리스트로 합쳐진 리스트



### 사전(딕셔너리)

# 단어와 뜻이 있는 사전처럼 사전자료형도 키와 값이 있는 자료형이다.
# 항상 키는 내가 100번 열쇠를 받았는데 200번 사물함을 열 수 없다.
# 키는 중복이 되지 않는다

cabinet = {3:"유재석", 100:"김태호"}  # {키 : 값} 형태
print(cabinet[3]) # 캐비넷의 3번 키는 유재석이라는 값이 나오게 된다.

#사전자료형에서 값을 가져오는 방법
print(cabinet[3])
print(cabinet.get(3))
# print(cabinet[5])   # cabinet에 5라는 키가 없기 때문에 hi가 출력 되지 않고 바로 끝났다.
# print("hi")
print(cabinet.get(5)) # cabinet에 5라는 키가 없으면 None이라는 NoneType문구가 출력이된다.

#None으로 출력하고 싶지 않다면
print(cabinet.get(5,"빈사물함..! 사용 가능")) # None대신에 출력할 문구를 설정할 수 있다.

# 사전 자료형안에 어떤 값이 있는 지 확인할 수 있음.
print(3 in cabinet) # 3이 이 사전내에 값이 있는지 확인
print(5 in cabinet) # 5이 이 사전내에 값이 있는지 확인

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"]) # 키에 해당하는 값들을 잘 출력

# 새 손님
print(cabinet) # 바뀌기 전
cabinet["A-3"] = "김종국" # 이러면 "유재석"이 빠지고 김종국으로 대체되고
cabinet["C-20"] = "조세호" # C - 20키에 "조세호"라는 값이 추가된다.
print(cabinet) # 값을 업데이트 하거나 추가 가능

# 손님이 갔다.
del cabinet["A-3"]
print(cabinet)

# Key들만 출력
print("keys = "+str(cabinet.keys()))
# Value들만 출력
print("values = "+str(cabinet.values()))

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear() # 안에 있는 모든 값들을 지울 수 있다.



### 튜플
# 튜플은 리스트와는 다르게 내용변경과 추가를 할 수 없다.
# 속도가 리스트보다 빠르다.

# 돈까스 예시(절대 메뉴변경이 없는)
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") #튜플은 변경이나 추가가 불가능하기 때문에 add()를 사용하면 오류가 발생한다.

#튜플은 어디서 활용될 수 있냐면
name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

(name,age,hobby) = ("김종국",20,"코딩") # 튜플은 이용하면 간단하게 서로 다른 변수에 서로 다른 값들을 한번에 선언할 수 있다.
print(name,age,hobby)

### 집합(Set)
# 중복이 되지 않고, 순서가 없다.

my_set = {1,2,3,3,3} # 세트에서는 값만 나열한 형태로 딕셔너리와 다르다.
print(my_set) # 중복을 제외하고 {1,2,3}만 출력이 되는 모습이다.

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

# 교집합 ( java와 python을 모두 할 수 있는 개발자)
print(java & python) #
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할 수 있지만 python을 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

# 교육을 받아서 python을 할 줄 아는 사람이 늘었다면
python.add("김태호")
print(python) # set에 값을 추가할 수 있다.

# 만약 java를 까먹었다면
java.remove("김태호")
print(java)


### 자료구조의 변경
menu = {"커피","우유","쥬스"}
print(menu,type(menu)) # set자료형이다. (집합형태)

menu = list(menu)
print(menu,type(menu)) # set자료형을 list로 바꾸었다.

menu = tuple(menu)
print(menu, type(menu)) # tuple로 자료형을 바꾸었다. 괄호 모양이 다 바뀐다.

menu = set(menu)
print(menu, type(menu)) # tuple로 자료형을 바꾸었다. 괄호 모양이 다 바뀐다.



### Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오
#
# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가능
# 조건 3 : random 모듈의 shuffle과 sample을 활용
#
# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

#list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list = list(range(1,21)) # 1부터 20까지의 숫자를 생성

print("-- 당첨자 발표 --")
shuffle(list)       # 리스트 섞어버림
winners = sample(list,4)
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("-- 축하드립니다. --")


'''