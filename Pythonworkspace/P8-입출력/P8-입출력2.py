# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # write 쓰다(덮어쓰기)
# print("수학 : 0", file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # write에는 줄 바꿈이 없어 따로 해줘야함
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 한 줄 한 줄 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),)
# score_file.close() #줄바꿈 크게 하기 싫으면 end=""쓰기

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle / 데이터를 파일 형태로 저장
# import pickle # 항상 살려둘것
# profile_file = open("profile.pickle", "wb") # binary(2진법)/ 피클을 쓰기위해 필요
#                 # pickle에서는 따로 encoding을 해줄 필요 없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile) # 부르면 이 내용이 나와야 한다는 예시이지 중요한건 아님
# pickle.dump(profile, profile_file) # profile 을 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with / 파일을 열고 닫는 작업을 편하게 해줌
# import pickle
# with open("profile.pickle","rb") as profile_file: # file에 pickle정보를 저장
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있다")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
