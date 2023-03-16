# # 표준 입출력
# print("Python","Java", "JavaScript", sep= " , ", end="? ") 
# # "sep="로 문자 사이 설정
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python","Java", file=sys.stdout) # 표준 출력
# print("Python","Java", file=sys.stderr) # 표준 에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
#     # 과목은 왼쪽정렬 8칸 확보, 점수는 4칸 확보 오른쪽 정렬

# 은행 대기순번표
#001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호:" + str(num).zfill(3)) 
#     #"zfill"은()만큼 확보, 빈칸을 0으로 채움

# answer =input("아무 값이나 입력하세요 :") #항상 문자열로 저장
# answer = 10 # 얘 살려두면 출력할때 str 해줘야됨
# print(type(answer)) #정수임에도 str안해도 됨, 변수=정수 설정 안한다면 가능
# print("입력하신 값은 "+ (answer) + "입니다")

# # 다양한 출력포멧
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로, 음수일땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(-100000000000))
# print("{0:+,}".format(100000000000))
# # 3자리 마다 콤마, 부호, 자릿수 확보하기
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))