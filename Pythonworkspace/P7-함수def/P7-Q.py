# Quiz) 표준 체주을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# 내가 처음한 것 (지역변수식)
# def std_weight(height, gender):
#     if gender == "남자":
#         std_weight = round((height**2)*22,2)
#         height = int(height*100)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight))
#     else:
#         std_weight = round((height**2)*21, 2)
#         height = int(height*100)
#         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight))

# std_weight(1.75, "남자")
# std_weight(1.6, "여자")

# 나도코딩님의 답안 (전역변수식)
# def std_weight(height, gender):
#     if gender == "남자":
#           return (height**2) *22
#     else:
#          return (height**2) *21
    
# height = 175 
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))




