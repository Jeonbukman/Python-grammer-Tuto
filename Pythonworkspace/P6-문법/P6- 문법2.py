# # 반복문 while / 조건을 만족 할 떄까지 반복 while(조건)

# customer = " 토르" # 조건까지만 반복하기
# index = 5
# while index >= 1:
#     print("{0},커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -=1
#     if index == 0:
#         print("커피는 폐기되었습니다.")

# customer = "아이언맨" # 조건에 따라 계속 반복하기
# index =1
# while True:
#     print("{0},커피가 준비 되었습니다. 호출 {1}회".format(customer,index))
#     index +=1 # 계속 반복되는 무한루프에 빠짐, 명령 실행창에서 control+c하면 멈춤

# customer ="토르" # 조건 만족까지 반복하기
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# # continue 와 break / while 문에서 사용
# absent = [2,5] #결석
# no_book = [7] # 책없음
# for student in range(1, 11): #1~10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))
# # continue는 변수값을 실행하지 않고 다음으로 넘기는 명령어
# # break은 반복값에 상관없이 탈출

# # 한 줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 => 101 102 103 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man","Thor","Groot"]
# students = [len(i)for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man","Thor","Groot"]
# students = [i.upper() for i in students]
# print(students)