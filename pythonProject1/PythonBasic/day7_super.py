# 일반유닛
class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
class FlyableUnit(Unit, Flyable):   # 여기서 Unit 클래스 와 Flyable클래스의 매개변수 위치를 바꾸면 앞클래스의 생성자가 실행됨
    def __init__(self):
        super().__init__()

# 드랍쉽
dropship = FlyableUnit() # 결과는 : Unit생성자

# 2개 이상의 부모클래스를 다중상속을 받을 때에는 순서상의 가장 먼저에 상속받는 클래스에 대해서만 init함수가 호출된다.
# 두 부모클래스의 생성자를 모두 상속받고 싶다면
# super.__init__()이 아닌 Unit.__init__(self) Flyable.__init__(self)로 상속을 받으면 된다.

class FlyableUnit2(Unit, Flyable):   # 여기서 Unit 클래스 와 Flyable클래스의 매개변수 위치를 바꾸면 앞클래스의 생성자가 실행됨
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit2() # Unit Flyabe 생성자 모두 상속