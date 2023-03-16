## 상속
# "class Attack(Unit):" 처럼 사용
# 부모 클래스의 내용을 자식 클래스에게 물려줌

#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def move(self, location): ## 넣어본것
        print("{0} : {1} 방향으로 이동합니다.".format(self.name, location))

#공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)
        self.damge = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damge))
        
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp-= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

    def move(self, location): ## 넣어본것
        print("{0} : {1} 방향으로 이동합니다.".format(self.name, location))
# # 불곰 # 공격유닛
# firebatt1 = AttackUnit("불곰", 50, 16)
# firebatt1.move("5시")  #바꾼것
# # 의무병 # 일반 유닛
# medic1 = Unit("메딕", 50) ##넣어본것
# medic1.move("12시")
# #공격 2번 받는다 가정
# firebatt1.damaged(25)
# firebatt1.damaged(25)

## 다중상속
# 여러곳에서 상속받아옴

# 수송기 : 공중 유닛, 공격불가
# 날 수 있는 기능의 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self,flying_speed)

# # 발키리 : 공중공격, 1타 14회
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시") #Flyable에서는 기능만 갖고 있어 멤버변수 추가