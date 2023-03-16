# if 문
# 분기 / 상황별 코드 실행시키기
# weather = "비"
# weather ="미세먼지"
# weather="맑음"
# if 조건: (조건을 계속 비교하며 맞는 것을 내놓음)
#     실행 명령문 #/형식 (if 조건:)으로 끝맺고 다음칸에 실행 명령문 작성

# weather =input("오늘 날씨는 어때요?" ) # input=사용자 입력을 받는 문장 
# # 값을 입력하면 str형태로 변수에 적용됨
# # 오늘 날씨는 어때요? ㅁ->에 값 입력 (맑음)= 준비물 필요없어요

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요") # 조건에 맞지않으면 바로 끝남

# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요") # 그 무엇도 아닌경우/ 또한

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30 :
#     print("괜찮은 날씨에요")
# elif 0 <=temp and temp <10: # and가 연속되는 문장들일 경우 and생략 가능
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for 문
# print("대기번호 : 1")
# print("대기번호 : 2") 


# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no)) 
# 리스트 내의 값들을 차례대로 뱉음

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no)) 


# starbucks = [ "아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

