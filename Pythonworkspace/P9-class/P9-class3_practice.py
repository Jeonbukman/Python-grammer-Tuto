# super을 사용하며 다중상속을 할 때의 문제

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 수송선
dropship = FlyableUnit() # 먼저 상속 받는 쪽만 따름