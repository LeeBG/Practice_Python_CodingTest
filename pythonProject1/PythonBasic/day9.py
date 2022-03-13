"""
### 모듈
# 모듈은 쉽게 설명하면 필요한 것들끼리 부품처럼 잚 만들어진 파일
# 자동차를 예로들면 자동차를 이용하다가 타이어가 마모가 되거나 펑크가 되면
# 타이어만 교체하면 된다. 범퍼가 파손되면 법퍼만 교체해주면 된다.
# 소프트웨어도 타이어나 범퍼처럼 부품만 교체하거나 추가할 수 있으면 유지보수가 쉽고 코드재사용에서 효율적이다.

# 예를 들어 극장이 있다고 생각한다(현금만 받음)
# 잔돈을 안바꿔준다.(4만원을 주면 5천원을 거슬러 주지 않는다

# 극장에 가기 전에 사람수에 따라서 얼마의 가격이 나오는지 알 수 있는 모듈을 하나 만들것이다.
# .py파일을 하나 만든다 . theater_module.py 파이썬 파일에는 상황별로 사람에 따른 가격을 설정한다.
# 설정이 완료되면 불러올것이다.  모듈은 내가 그 모듈을 쓴 경로가 같거나 모듈을 모아놓은 경로에 있어야한다.
# 방금만든 파일은 동일한 theater_module.py 와 day8.py의 경로가 같기 때문에 그냥 사용이 가능하다.

# import theater_module
#
# theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명에서 조조 할은 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때


# 너무 코드가 길기 때문에 as 를 사용해서 별명사용을 한다.
import theater_module as mv     # 모듈의 별명을 지어서 줄일수 있다.

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# 또 다른 방법으로는 지금까지는 import문을 쓰는 것외에 from문을 쓰는 것이다.
from theater_module import *
# from random import *

price(3)            # 모듈명. 필요없이 모듈에 포함된 모든것(*)을 사용한다는 것이다. 바로 함수호출해서 사용
price_morning(4)
price_soldier(5)



from theater_module import price, price_morning # 특정 함수만을 사용할 때에는 이런식으로 사용

price(3)
price_morning(4)
# price_soldier(5) # 오류



from theater_module import price_soldier as price
# price_soldier에 별명을 붙인다.
price(5) # price가 아니라 price_soldier의 내용이 나온다.





### 패키기
# 패키지는 모듈들을 모아놓은 집합이다. - 하나의 디렉토리에 여러개의 모듈파일들을 모아놓은 것이라고 보면 쉽게 이해할 수 있다.
# 예를 들어서 어떤 신규 여행사 프로젝트를 담당했다고 가정한다. 이 여행사는
# 태국과 배트남의 패키지 여행상품을 제공한다고 했을때 우리가 이 패키지의 내용을 직접 파이썬 패키지로 만들어서 직접 사용할 수 있게 만든다.
# 새로운 폴더 travel폴더를 만든다.

# 우리가 만든 패키지를 가져온다.
# import travel.thailand      # import 맨 뒤에는 항상 모듈이나 패키지만 가능하다.(클래스나 함수는 import 직접 불가능하다)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
#
# from travel.thailand import ThailandPackage # from import구문애서는 import뒤에 모듈 패키지 클래스명과 함수 모두 사용이 가능하다.
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import vietnam      # 패키지 까지만 from해놓고 import 모듈
trip_to = vietnam.VietnamPackage() #
trip_to.detail()




### __all__
# 우리가 이전에 랜덤모듈을 썼었는데
# from random import * # 랜덤모듈안에 있는 모든 함수들을 사용하겠다 선언

# from travel import * #travel패키지 안에 있는 모든 것을 가져오겠다는 것이다.
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 오류발생 vetname이 정의되지 않았다고 뜬다.

# 실제로는 개발자가 이 문법상에서 공개 범위를 설정해줘야한다.
# 무슨 말이냐면 우리가 패키지 안에 포함된 것들중에서 import 되기를 원하는 것만 공개를 하고 나머지는 비공개로 공개범위를 설정할 수 있다.
# __init__.py 파일에서 설정 >> __all__ = ["vietnam"] #설정

from travel import * # travel패키지 안에 있는 모든 것을 가져오겠다는 것이다.
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# 이번에는 출력이 잘 되는것을 알 수 있다.

# 이상태에서 우리가 __all__ = ["thailand"] 를 설정하면
from travel import * # travel패키지 안에 있는 모든 것을 가져오겠다는 것이다.
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 태국 패키지여행 정보도 잘 작동한다.



### 모듈 직접 실행
# 그런데 지금 우리가 만든 패키지는 사실 내용이 별로 없어가지고 별다른 테스트없이 그냥 바로 코드를 작성함
# 실제로 우리가 패키지나 모듈을 만들때에는 모듈이 잘 동작하는지 테스트를 해봐야한다.
# 그러기 위해서는 이런 방법을 사용한다.
# ThailandPackage클래스에서 내부 외부 모듈 설정을 해준다. Thailand.py 참고


###  패키지 모듈 위치
# 마지막으로 지금까지 작성한 패키지나 모듈은 현재 작성중인 day9.py와 같은경로에 있었다.
# 그래서 이 모듈을 호춢하는 혹은 패키지를 호출하는 동일한 폴더에 있거나 혹은 파이썬 라이브러리가 모여있는 폴더에 있어야 사용가능
# 지금 어느 위치에 있는 지 확인하기 위해서는 inspect를

from travel import *
import inspect
import random
print(inspect.getfile(random)) # 파이썬 기본 라이브러리가 모여있는 경로가 나온다.
print(inspect.getfile(thailand)) # thailand.py 모듈의 경로가 나온다.


# thailand.py를 random라이브러리가 있는 경로로 옮기고 실행을 해보면 기본 라이브러리위치가 나타나고
# 이런식으로 내가 만든 모듈을 기존의 라이브러리 경로에 두면 다른 프로젝트를 할 때에서 모듈으 꺼내서 사용가능하다.



### pip로 패키지 설치하기
# 파이썬은 이미 잘 만들어진 패키지를 설치해서 사용하는 것이 중요하다.
# 내가 모듈을 새로 만들려고 하면 엄청난 시간이 소모된다.
# 다른 사람들이 만든 패키지가 어떤것들이 있는지 앓아보기 위해서는 pypi를 구글에 검색해본다
# 맨 첫번째 사이트에서 30만개이상의 project가 있다고 뜬다. 다양한 프로젝트를 찾아볼 수 있다.
# 우리는 웹 스크립팅을 위한 라이브러리인 beautifulsoup이라는것을 사용해 볼 것이다.
# 검색한후 해당 프로젝트의 상단에 보면
# pip install beautifulsoup4 이라고 뜬다. 이것은 beautifulsoup 4버전을 설치하기 위한 명령어이다.

# 실제로 설치하기 위해서 terminal로 들어가서 pip명령어를 친다.
# 그랬더니 다운로드를 받기 시작한다.
# pipy의 아래에 있는 예제들을 쳐본다.



from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


# 그리고 터미널에서 >> pip list 라고 치면 pip로 설치한 패키지들의 목록이 나타난다.

# pip show beautifulsoup4 를 치면 beatifulsoup4 패키지의 버전 등에 관한 설명이 나온다.

#만약에 설치한 패키지가 새로운 버전이 나와서 업그레이드가 필요하다면
# pip install --upgrade [패키지명]

# 이미 설치되어있는 패키지를 삭제하고 싶다면
# pip uninstall [패키지명]
# 삭제를 하면 위의  부분을 사용하지 못하게 된다.



### 내장함수

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요")
# print("{0}은 아주 좋은 언어입니다!!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())    # import하기 전
import random # 외장 함수
print(dir())    # import한 후 random이 추가
import pickle
print(dir())    # pickle과 random을 쓸 수 있다.

print(dir(random)) # random모듈내에서 쓸 수 있는 것들이 나온다. randint 등 random.이후에 쓸 수 있는 것들

#print(dir(random))
lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name)) # 문자열에 관해 쓸 수 있는 것들이 굉장히 많다.
# 파이썬 표준 라이브러리를 검색해 보면 굉장히 많은 내장함수들이 나오는데 참고하여 사용하면 된다.




### 외장함수
# google에서 list of python module을 검색하면 외장함수들을 검색할 수 있다.
# random함수를 예로 들면 다양한 random에 관한 함수와 사용예제가 나오니 참고하면서 필요한 부분을 가져다 쓰면된다.
# 몇가지 외장함수를 써본다.

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
import glob
print(glob.glob("*.py")) # 현재 경로에서 확장자가 py인 모든 파일

# os : 운영체제(OS)에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉토리를 표시해준다.

folder = "sample_dir"
if os.path.exists(folder):  # 위의 내가 만들려는 폴더가 이미 있으면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) #폴더 생성
    print(folder,"폴더를 생성하였습니다.")

print(os.listdir()) # 폴더내의 모든 파일과 폴더들을 나타낸다.




# time : 시간 관련 함수
import time
print(time.localtime()) # 현재 시간을 표시한다.
print(type(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ",datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()   #오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장 (100일의 간격을 저장)
print("우리가 만난지 100일은", today+td) # 오늘부터 100일 후


"""

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
#
# 조건) 파일명은 byme.py로 작성 \
#
# (모듈 사용 예제)
import byme
byme.sign()

# (출력예제)
# 이 프로그램은 나도코딤에 의해 만들어졌습니다
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com