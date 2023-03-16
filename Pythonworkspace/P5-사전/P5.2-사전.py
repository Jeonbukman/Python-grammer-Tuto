# 사전 설정의 경우 중괄호 이용
# cabinet = {3:"유재석", 100:"김태호"} # key=3,100/ value=유,김
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # 변수에 5가 없어 프로그램이 종료
# print(cabinet.get(5)) # 값이 없으면 None 뱉고 다음거 출력
# print(cabinet.get(5, "사용 가능")) #5를 사용가능과 연결
# print("hi")

# print(3 in cabinet) # True 사전에 이 자료가 있는가 key in value
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님 (추가 및 업데이트)
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["c-20"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# #value 들만 출력 (값)
# print(cabinet.values())

# # 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#튜플
# 리스트와 다르게 수정, 추가 불가/ 대신 빠름/ 괄호 형태
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")  #고정된 값만 사용 가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby) #대신

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)