# #문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요""" # """ ~ """ 으로 변수로 삼을 열 지정 가능
# print(sentence3)

# #슬라이싱/ 필요한 만큼 잘라서 쓰기
# jumin = "990120-1234567"

# print("성별: " +jumin[7])
# print("연: " +jumin[0:2]) #[](콜롬) 쓸땐 0부터 n직전까지
# print("월: " +jumin[2:4])
# print("일: " +jumin[4:6])
# print("생년월일:" + jumin[:6]) # 처음부터 n직전까지
# print("뒤 7자리: "+jumin[7:]) # n부터 끝까지
# print("뒤 7자리 (뒤에부터): "+jumin[-7:]) #맨 뒤에서 n번째~ 끝까지

# #문자열 처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) # 0번째가 대문자인가? 확인
# print(len(python)) #변수의 길이 파악
# print(python.replace("Python", "Java"))#알파->베타,설정변수에 영향x

# index = python.index("n") #'index='는 변수 '.index()'는 명령어
# print(index) #목적변수(py)의 "x"가 몇번 째에 위치하는지 알려줌
# print(index)
# index = python.index("n", index +1)  # 5번째 n -> 15번째 n
# print(index) # 이전index가 찾은 문자(목표)의 다음 목표를 재탐색함

# print(python.find("java")) #값이 변수에 없으면 -1 반환
# # print(python.index("Java")) #index에서는 오류로 반환
# print("hi") #index로 오류내면 뒤에 출력x, find는 가능

# print(python.count("n")) #변수 내 값의 출현 횟수