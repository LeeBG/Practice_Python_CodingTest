"""
### 클래스
# 스타크래프트 게임을 예로 든다. (클래스의 필요성)

# 마린 : 공격유닛 - 총을 사용함
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 6 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1} \n".format(hp,damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35


print("{0} 유닛이 생성되었습니다. ".format(tank_name))
print("체력 {0}, 공격력 {1} \n".format(tank_hp,tank_damage))

def attack(name,location,damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(\
        name, location, damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)


# 새로운 탱크를 만들어서 attack
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

attack(tank2_name,"1시",tank2_damage)

# 게임에서는 수십개의 유닛이 나와 전투하게 되는데 그럴때마다 새로운 탱크를 만들어서 체력과 데미지를 따로
# 만들어주는 것이 불편하기 때문에 클래스를 만들어 사용함으로써 코드의 중복을 방지한다.
# 붕어빵의 틀과 같다. 이 틀이 바로 클래스이다. 틀만 제대로 갖추어 져있으면 재료를 넣어 붕어빵을 무한으로 만들 수 있다.

# 위의 내용을 클래스화 시켜서 다시 만들어 본다.

class Unit: # 클래스이름의 가장 첫 글자는 대문자로 사용한다.(숫자x)
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))
marine1 = Unit("마린",40,6)
marine2 = Unit("마린",40,6)
tank = Unit("탱크",150,35)

# Unit이라는 공통점을 가진 클래스 틀에 마린과 탱크를 쉽게 만들 수 있다. 코드의 양이 확 줄어들었다.



### __init__ 함수 (파이썬에서 쓰이는 생성자)
# 생성자함수란 클래스(틀)에 맞게 객체가 만들어질때 자동으로 호출되는 함수이다.
# 마린이나 탱크와 같이 클래스로 부터 만들어지는 것들을 객체라고 표현한다.
# 이 때 마린과 탱크는 Unit클래스의 인스턴스라고 한다.


class Unit: # 클래스이름의 가장 첫 글자는 대문자로 사용한다.(숫자x)
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린",40,6) # self를 제외하고 동일하게 값을 던져 줘야한다.
marine2 = Unit("마린",40,6) # self를 제외하고 동일하게 값을 던져 줘야한다.
tank = Unit("탱크",150,35)  # self를 제외하고 동일하게 값을 던져 줘야한다.
marine3 = Unit("마린",40)   # 오류 발생 !!! - 두개의 필요한 인자가 빠져있다.(메개변수에 맞춰야 한다.)




### 멤버 변수

class Unit: # 클래스이름의 가장 첫 글자는 대문자로 사용한다.(숫자x)
    def __init__(self,name,hp,damage):
        self.name = name        # 멤버변수
        self.hp = hp            # 멤버변수
        self.damage = damage    # 멤버변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않는 기술)

wraith1 = Unit("레이스",120,8)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 프로토스 유닛의 - 마인드 컨트롤 : 상대방의 유닛을 내 것으로 만드는 것 (빼앗음)
# 마인드 컨트롤로 상대방의 레이스를 빼앗는다고 한다.
wraith2 = Unit("빼앗은 레이스",120,8) # 이미 빼앗은 레이스(이름,체력,공격력)
wraith2.clocking = True # 클래스 외부에서 cloking이라는 변수를 추가로 할당한 것이다.(확장)

# 파이썬에서는 어떤 객체에 추가로 쓸 수 있다. wraith1에는 clocking이 없다.

if wraith2.clocking == True:
    print("{0}는 클로킹 상태입니다.".format(wraith2.name))




### 메소드

class Unit: # 클래스이름의 가장 첫 글자는 대문자로 사용한다.(숫자x)
    def __init__(self,name,hp,damage):
        self.name = name        # 멤버변수
        self.hp = hp            # 멤버변수
        self.damage = damage    # 멤버변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage        # 여기서의 damage는 이 클래스의 객체의 공격력이다.

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
                #location은 전달받은 값을 쓴다는 얘기이다.

    def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50 ,16) # 객체생성
firebat1.attack("5시")

# 25데미지 공격을 2번 받는다고 가정
firebat1.damaged(25) # firebat1 의 상태변화
firebat1.damaged(25)




### 상속

# 공격력이 없는 유닛이 있기도 하다 (테란의 메딕 등)

#일반 유닛
class Unit: # 클래스이름의 가장 첫 글자는 대문자로 사용한다.(숫자x)
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        # 데미지 삭제

# class AttackUnit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage        # 여기서의 damage는 이 클래스의 객체의 공격력이다.
#
#     def attack(self,location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#               .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
#                 #location은 전달받은 값을 쓴다는 얘기이다.
#
#     def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
#         print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
#         self.hp -=damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
#         if self.hp <= 0:
#            print("{0} : 파괴되었습니다.".format(self.name))

# 일반 Unit과 공격이 가능한 AttackUnit의 겹치는 부분이 생긴다. name,hp는 모든 유닛이 가진다.
# 이럴때 우리가 상속을 쓸 수 있는데 상속은 AttackUnit이 Unit을 상속받아 사용할 수 있다.
# 상속받을 클래스의 멤버볌수와 메서드를 AttackUnit에서 쓸 수 있다.

class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp) # 이름과 체력을 넘김 damage는 추가
        self.damage = damage        # 여기서의 damage는 이 클래스의 객체의 공격력이다.

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
                #location은 전달받은 값을 쓴다는 얘기이다.

    def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50 ,16) # 객체생성
firebat1.attack("5시")

# 25데미지 공격을 2번 받는다고 가정
firebat1.damaged(25) # firebat1 의 상태변화
firebat1.damaged(25)

# 상속이 잘 된것을 알 수 있다.




### 다중상속
# 지금까지는 우리가 상속을 한 클래스만 받았다.
# 공중 유닛과 지상 유닛을 예로 들어 구분을 해 보겠다.
#일반 유닛
class Unit: # 부모클래스 (상속을 해주는 클래스)
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
        # 데미지 삭제

# 공격 유닛
class AttackUnit(Unit): #(상속을 받는 클래스)
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp) # 이름과 체력을 넘김 damage는 추가
        self.damage = damage        # 여기서의 damage는 이 클래스의 객체의 공격력이다.

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
                #location은 전달받은 값을 쓴다는 얘기이다.

    def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 파이어뱃 탱크 등의 지상유닛 수송이 가능하다.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): # 다중 상속
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)    #멤버변수 상속 초기화
        Flyable.__init__(self,flying_speed)         #멤버변수 상속 초기화

# 발키리 : 공중 공격 유닛, 한번에 여러발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시") # 부모의 fly()함수 호출




### 연산자 오버라이딩
# 부모클래스에서 정의한 메소드 말고 자식클래스에서 정의한 메소드를 쓰고 싶을때 메소드를 새롭게
# 정의해서 쓸때 이것을 오버로딩이라고 한다.
# 유닛클래스에서 speed정보를 추가한다.

#일반 유닛 -
class Unit: # 부모클래스 (상속을 해주는 클래스)
    def __init__(self,name,hp,speed): # 스피드 정보 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    # 유닛을 이동할 수 있다는 가정하에
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit): #(상속을 받는 클래스)
    def __init__(self,name,hp,speed,damage): # 스피드 추가
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
                #location은 전달받은 값을 쓴다는 얘기이다.

    def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 파이어뱃 탱크 등의 지상유닛 수송이 가능하다.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): # 다중 상속
    def __init__(self,name,hp,damage,flying_speed): # 날아다니는 속도가 있기 때문에 지상유닛 속도가 필요없다.
        AttackUnit.__init__(self,name,hp,0,damage)    #지상 스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self,location):    # 오버라이딩을 사용하면 상위클래스의move함수를 재정의 한다.
        print("[공중 유닛 이동]")
        self.fly(self.name,location)
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋고, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시") # 이 경우 지상유닛은 move함수를 쓰고 공중 유닛은 fly함수를 써야한다.
battlecruiser.move("9시") # 재정의된 함수 사용






### Pass

#일반 유닛 -
class Unit: # 부모클래스 (상속을 해주는 클래스)
    def __init__(self,name,hp,speed): # 스피드 정보 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    # 유닛을 이동할 수 있다는 가정하에
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit): #(상속을 받는 클래스)
    def __init__(self,name,hp,speed,damage): # 스피드 추가
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage)) # self를 붙이면 클래스 자기자신의 멤버변수를 쓰는것
                #location은 전달받은 값을 쓴다는 얘기이다.

    def damaged(self,damage): # 여기서의 damage는 따로 입력받는 상대방의 공격력이자 이 객체가 받는 데미지이다.
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 마린 파이어뱃 탱크 등의 지상유닛 수송이 가능하다.

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable): # 다중 상속
    def __init__(self,name,hp,damage,flying_speed): # 날아다니는 속도가 있기 때문에 지상유닛 속도가 필요없다.
        AttackUnit.__init__(self,name,hp,0,damage)    #지상 스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self,location):    # 오버라이딩을 사용하면 상위클래스의move함수를 재정의 한다.
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

# 우리가 어떤 건물을 만든다고 한다.
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass            # 아무것도 안하고 일단 넘어간다. -> pass

# 서플라이 디폿 : 건물 1개 건물1당 생산 가능 유닛의 최대치가 증가
supply_depot = BuildingUnit("서플라이 디폿",500,"7시")

#실행을 하니 아무것도 하지 않음

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

# game_over()은 pass이기 때문에 아무것도 안하고 넘어간다.



### Super


#일반 유닛 -
class Unit: # 부모클래스 (상속을 해주는 클래스)
    def __init__(self,name,hp,speed): # 스피드 정보 추가
        self.name = name
        self.hp = hp
        self.speed = speed
    # 유닛을 이동할 수 있다는 가정하에
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit): #(상속을 받는 클래스)
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

# 우리가 어떤 건물을 만든다고 한다.
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        Unit.__init__(self,name,hp,0)   # 건물은 이동 못한다고 가정
        super.__init__(name,hp,0)  # super=부모클래스,hp,0 슈퍼는 self를 뺴고 __init__을 해주면 된다.
        self.location = location





### Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화
    def __init__(self,location,house_type, deal_type,price,completion_year):
        self.location =location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))


h1 = House("강남","아파트","매매","10억","2010년")
h2 = House("마포","오피스텔","전세","5억","2007년")
h3 = House("송파","빌라","월세","500/50","2000년")

list_houses = []
list_houses.append(h1)
list_houses.append(h2)
list_houses.append(h3)

print("총 {0}대의 매물이 있습니다.".format(len(list_houses)))
for house in list_houses:
    house.show_detail()

"""