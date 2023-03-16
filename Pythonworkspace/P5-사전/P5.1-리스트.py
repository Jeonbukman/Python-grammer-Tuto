# 리스트 [] 순서를 가진 객체의 집합

# 지하철 칸별로 10명, 20명, 30명

# subway1 = "조세호"
# subway2 = "유재석"
# subway3 = "박명수"

subway = ["조세호","유재석","박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가ㅏ 다음 정류장에서 다음 칸에 탑승
# subway.append("하하")
# print(subway)

# # 정형돈을 조세호와 유재석 사이에 태움
# subway.insert(1, "정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) # 누가 빠졌는가
# print(subway) # 누가 남아있는가


# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort() # sort = 종류, 부류란 뜻/ 정렬 명령어
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1] # 확장용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)
