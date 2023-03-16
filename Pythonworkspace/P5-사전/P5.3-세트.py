# 집합 (set)
# 중복 안됨, 순서 보장없음 / 세트와 달리 값만 나열
# my_set = {1,2,3,3,3}
# print(my_set) #{1,2,3}

# java = {"유재석", "김태호","양세찬"} #중괄호로 해도되고 또는
# python = set(["유재석", "박명수"]) # 리스트 만들어놓고 set으로 감쌈
 
# # 교집합 (자바와 파이썬을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (자바 또는 파이썬을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python)) 

# # 차집합 (java는 할 수 있는데 파이썬은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # 파이썬을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었음
# java.remove("김태호")
# print(java)

#자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))