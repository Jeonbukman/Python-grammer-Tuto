## 메소드 오버라이딩
# 자식 클래스의 메소드를 쓰고 싶을때 메소드를 새로 정의해 사용 = 오버라이딩

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location): 
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))
    
#공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp, speed)
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

# 공중 유닛, 공격불가
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
        AttackUnit.__init__(self, name, hp, 0, damage) # 공중 스피드 지정 /지상 스피드 0
        Flyable.__init__(self,flying_speed)

    def move(self, location): # move 재정의 해줌 / 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# # 벌처 : 지상 유닛, 기동성
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력 상, 공격력 상
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

# vulture.move("11시")
# battlecruiser.move("9시")

## pass
# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 완성된 것처럼 보이게 해둠

# # 보급고 : 8유닛 충원
# supply_depot = BuildingUnit("보급고", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

## super
# 먼저 상속받는 쪽만 따름
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) 
        super().__init__(name, hp, 0) #super(). 은 self를 안씀
        self.location = location

