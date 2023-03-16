## 클래스 / 붕어빵 틀, 연관이 있는 변수, 함수의 집합

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damge = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damge))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

## __init__ , 파이썬 생성자, 객체 만들때 자동 호출기 같은것
# 필요한 정보만큼 채워진 것들을 불러와 실행함

## 멤버변수 / self. 같은것 / 클래스 내에서 정의된 변수
# # 파이썬에서는 외부에서 객체를 만들어 쓸 수 있음
# # 클래스 외부에서 변수에 대해 확장 가능, 확장은 적용개체에서만 유지

# # 팬텀
# phantom = Unit("팬텀", 80, 5)
# print("유닛 이름: {0}, 공격력 : {1}\n".format(phantom.name, phantom.damge))
# # :을 통해 클래스 외부에서 멤버변수를 추가 할 수 있음

# # 마인드 컨트롤 : 상대방 유닛을 강탈
# phantom2 = Unit("팬텀",80,5)
# phantom2.clocking = True

# if phantom2.clocking == True:
#     print("{0}은 현재 클로킹 상태입니다.".format(phantom2.name))

## 메소드 
# 메소드 앞에는 항상 self. , 집어 넣는것

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damge))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damge = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#               .format(self.name, location, self.damge))
        
#     def damaged(self,damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp-=damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 불곰
# firebatt1 = AttackUnit("불곰", 50, 16)
# firebatt1.attack("5시")

# #공격 2번 받는다 가정
# firebatt1.damaged(25)
# firebatt1.damaged(25)



