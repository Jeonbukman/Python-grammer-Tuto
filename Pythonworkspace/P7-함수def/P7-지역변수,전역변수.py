#지역변수 (함수 내에서만/ 함수 호출시 제작, 끝나면 제거 )
# gun = 10 #함수 내에서 쓰지 못함

# def checkpoint(soldiers): #경계근무
#     gun = 20
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총: {0}".format(gun))

#전역변수 (프로그램 내 어디서든 부를수 있음)

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):   #return
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감   #/global
# gun = checkpoint_ret(gun, 2)          #/return
# print("남은 총: {0}".format(gun))