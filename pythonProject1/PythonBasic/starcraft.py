from time import *
from random import *

#일반 유닛 -
class Unit: # 부모클래스 (상속을 해주는 클래스)
    def __init__(self,name,hp,speed): # 스피드 정보 추가
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    # 유닛을 이동할 수 있다는 가정하에
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name,location,self.speed))

    # 모든 일반 유닛은 피해를 받을 수 있다.
    def damaged(self,damage):       # 여기서의 damage는 받는 데미지
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛
class AttackUnit(Unit): #(상속을 받는 클래스)
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name,location,self.damage))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)


# 마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 (일정 시간 동안 속도와 공격 속도를 증가) // 자기 체력의 10을 사용한다
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            self.damage += 5
            self.speed += 1
            print("{0} : 스팀팩을 사용합니다. (HP : {1} attack : {2} speed : {3})".format(self.name, self.hp, self.damage,
                                                                                 self.speed))
            time.sleep(3000)
            self.damage -= 5
            self.speed -= 1
            print("{0} : 스팀팩을 지속시간이 끝났습니다. (HP : {1} attack : {2} speed : {3})".format(self.name, self.hp, self.damage,
                                                                                       self.speed))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False  # 시즈 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:  # 개발되지 않았을 때
            return

        # 현재 시즈모드가 아닐 때 => 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 중인 상태 -> 시즈모드 해제
        else:
            print("{0}: 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 레이스(공중유닛 클로킹(투명화 스킬))
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",120 ,20 ,1)
        self.clocked = False # 클로킹모드

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 전환합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_end():
    print("Player : gg") # good game의 약자
    print("Player가 게임을 나갔습니다.")


# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 appand)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발하기
Tank.seize_developed = True
print("시즈모드 업그레이드가 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩 , 탱크 : 시즈모드, 레이스 : 클로킹)
for Unit in attack_units:
    if isinstance(unit,Marine): # 특정 인스턴스인지 확인(마린이면 마린인지 확인)
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료 (전투 패배)
game_end()